import os
import re
import sys

import markdown

def convert_imtag(text):
    for md in re.findall('\!.*?\)', text):
        alt = md[md.find('[')+1 : md.find(']')]
        url = md[md.find('https://') : md.find("\"")]
        html = f"<img src=\"{url}\" alt=\"{alt}\" title=\"{alt}\" width=100% height=auto>"
        text = text.replace(md, html)
    return text

# clear the docs directory
cwd = os.getcwd()
os.chdir('docs')
for file in os.listdir():
    os.remove(file)
os.chdir(cwd)

# load html style stuff
with open('template.html', 'r') as f:
    template = f.read()

# loop through the markdown directory
filenames = os.listdir('markdown')

for file in filenames:
    # read the markdown file and convert to html
    with open(os.path.join('markdown', file), 'r') as f:
        text = f.read()
        text = convert_imtag(text)
        html = markdown.markdown(text)
    # make corresponding html file
    # write style and html into it
    with open(os.path.join('docs', file.replace('.md', '.html')), 'w') as g:
        g.write(template)
        g.write(html)
