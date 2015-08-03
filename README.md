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

In order to simplify the solution the following convention were made:
- Images are only shown if they are in an img tag. In an ideal solotion we could use regexps to try to match file extensions (jpg,png etc...). In general the script is written to work with 'http://wiprodigital.com'
- Usage of global variables might not be ideal. However the size of the global variables is not expected to get too big and it gives flexibility especially because of the way python handles variables in recursion.
- Usage of a single file. The program could have been split down to logical parts. Eg. the MyHTMLParser could have been in a file on its own. However, since the size of the script was small I believe it is more readable to have everything in a single file.
- Output format. Might not be readable for someone who is not familiar to python dictionaries. However, python dictionaries can easily be converted to json thus the script could even be extended to an API.
