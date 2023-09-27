from bs4 import BeautifulSoup

def extract_visible_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script, style, and other non-visible elements
    for script in soup(["script", "style", "meta", "link", "head", "noscript"]):
        script.extract()

    return " ".join(soup.stripped_strings)

# Sample usage
html_string = """
<html>
    <head>
        <title>This is the title</title>
    </head>
    <body>
        <h1>Welcome to the page</h1>
        <p>This is a paragraph.</p>
        <script>alert('This is a script');</script>
    </body>
</html>
"""

visible_text = extract_visible_text(html_string)
print(visible_text)
