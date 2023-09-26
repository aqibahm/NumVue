from langchain.document_loaders import AsyncHtmlLoader
from bs4 import BeautifulSoup as bs
import lxml.html as lh
import pprint
import yaml

def fetch_webpage(urls: list):
    loader = AsyncHtmlLoader(urls)
    docs = loader.load()
    soup = bs(str(docs), features = "lxml")
    prettyHTML = soup.prettify()

    return prettyHTML

def read_file_to_list(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

def insert_into_dict(d, parts, last):
    if not parts:
        return

    # Base case: if only one part is left, assign the last part as value to this key
    if len(parts) == 1:
        d[parts[0]] = last
        return

    # If the key doesn't exist or if it's a string, create a new dictionary for this key
    if parts[0] not in d or isinstance(d[parts[0]], str):
        d[parts[0]] = {}

    # Recursive call to handle the rest of the parts
    insert_into_dict(d[parts[0]], parts[1:], last)

def build_hierarchy(root, strings):
    # Extract the hyperlink that leads to this page:
    hyperlink = root

    result_dict = {}
    for s in strings:
        hyperlink = root + s
        # Split string at the last "."
        main_str, last_part = s.rsplit('.', 1)
        parts = main_str.split('.')
        insert_into_dict(result_dict, parts, {"link": hyperlink})

    return result_dict

def replace_terminal_elements(d, old_value, new_value):
    for key, value in d.items():
        if isinstance(value, dict):
            replace_terminal_elements(value, old_value, new_value)
        elif value == old_value:
            d[key] = new_value

urls = ["https://docs.manim.community/en/stable/"]
manim_hrefs = "manim_hrefs.txt"
returned_html = fetch_webpage(urls)
soup = bs(returned_html, 'html.parser')

# Extract only the href values starting with "reference":
links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("reference")]

# Write the prettified HTML to a .txt file
with open(manim_hrefs, 'w', encoding='utf-8') as file:
    for link in links:
        write_string = link + "\n"
        file.write(write_string)

print("Hyperlinks on Manim Community Docs homepage stored in ", manim_hrefs , ".")


# We want to get a hierarchical directory structure containing
# the contents from each of the extracted hyperlinks.

# Instead of focusing on the page structure itself,
# ideal to look into extracting nested data as an element tree.

# Open manim_hrefs.html:
# Example usage
# Extracting data from an example webpage to examine its structure:
root = "https://docs.manim.community/en/stable/"
page = "reference_index/animations.html"

result = read_file_to_list(manim_hrefs)
# pprint.pprint(result)

result = build_hierarchy(root, result)
# pprint.pprint(result)

# Write the nested dictionary as a YAML file.
with open('manim_docs.yaml', 'w') as outfile:
    yaml.dump(result, outfile, default_flow_style=False)

# Analyzing each webpage's structure:
# 1. Load first element from manim_hrefs.
manim_example_doc = "https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html"
loader = AsyncHtmlLoader(manim_example_doc)
docs = loader.load()

doc_page = bs(str(docs), features = "lxml")

print("\n\n\n\n =======================================")
print("Data fetched from Manim Community Docs: ")
print("=======================================")

print(doc_page)

for each in doc_page.a:
    print(each)

# Parse the html content:


