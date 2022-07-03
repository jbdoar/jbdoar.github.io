import os
import sys

import markdown

# load html style stuff
with open('style.html', 'r') as f:
    style = f.read()

# loop through the markdown directory
filenames = os.listdir('markdown')

for file in filenames:
    # read the markdown file and convert to html
    with open(os.path.join('markdown', file), 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    # make corresponding html file
    # write style and html into it
    with open(file.replace('.md', '.html'), 'w') as g:
        g.write(style)
        g.write(html)
