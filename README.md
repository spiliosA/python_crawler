# python_crawler
simple web crawler written in python
* execute with python 2.7 *

recursively iterates through internal links and prints out a dictionary of the following format :
```javascript
{
  link1 : 
    internal_links : {}
    external_urls  : {}
    images         : {}
  link2 : 
    internal_links : {}
    external_urls  : {}
    images         : {}
  ...
  }
```

In order to simplify the solution the following conventions were made:
- Some logical simplifications were made eg :
	- Images are only shown if they are in an img tag. In an ideal solution we could use regexps to try to match file extensions (jpg,png etc...). 
	- Separating internal from external links is based on whether or not the base url is included in the link.
- Usage of global variables. It is not always the best practice however, the size of the global variables is not expected to get too big and it gives flexibility especially because of the way python handles variables in recursion.
- Usage of a single file. The program could have been split down to logical parts. Eg. the MyHTMLParser could have been in a file on its own. However, since the size of the script was small I believe it is more readable to have everything in a single file.
- Output format. Might not be readable for someone who is not familiar to python dictionaries. However, python dictionaries can easily be converted to json thus the script could even be extended to an API.
