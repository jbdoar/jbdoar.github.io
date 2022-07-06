# website
Personal website

Trying to keep it as (c)lean as possible. Minimal formatting, flat file structure, and so on.

Project structure goes something like...

* Site content is written into markdown files located in the markdown directory.
* render.py takes each markdown file and renders it as HTML in the docs directory.
* Each HTML file is also prepended with the HTML contained in template.html.
That part is cribbed from [this website](http://bettermotherfuckingwebsite.com/).
