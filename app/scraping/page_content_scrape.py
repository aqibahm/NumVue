from bs4 import BeautifulSoup as bs
from bs4.element import Comment
import urllib.request
from langchain.document_loaders import AsyncHtmlLoader
import lxml.html as lh
import pprint

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(url):
    loader = AsyncHtmlLoader(url)
    raw_html = loader.load()
    bs_html = bs(str(raw_html), 'html.parser')
    article = bs_html.findAll("div", {"class": "article-container"})
    # visible_texts = filter(tag_visible, texts)
    # return u" ".join(t.strip() for t in visible_texts)
    return article

def extract_visible_text(html_content):
    soup = bs(str(html_content), 'html.parser')

    # Remove script, style, and other non-visible elements
    for script in soup(["script", "style", "meta", "link", "head", "noscript"]):
        script.extract()

    return " ".join(soup.stripped_strings)

def decode_escapes(s):
    return bytes(s, "utf-8").decode("unicode_escape")

manim_example_doc = "https://docs.manim.community/en/stable/reference/manim.animation.animation.html"
manim_example_doc_body_text = text_from_html(manim_example_doc)

manim_example_doc_visible_text = extract_visible_text(manim_example_doc_body_text)
print(manim_example_doc_visible_text)
print("Returned data of type: ", type(manim_example_doc_visible_text))

decoded_string = decode_escapes(manim_example_doc_visible_text)

# Write to file
with open('manim_example_doc_output.txt', 'w') as f:
    f.write(decoded_string)