# website
The personal website

Trying to keep it at (c)lean as possible
Structure is something like...

* Site content is written into markdown files located in the markdown directory.
* Each markdown file is rendered to HTML and placed in the html directory.
* Each HTML file is also prepended with the HTML contained in style.html. Style is cribbed from  bettermotherfuckingwebsite.com.
* render.py looks at the markdown directory and converts all the markdown files into HTML, every time. 
