# python_crawler
simple web crawler written in python

recursively iterates through internal links and prints out a dictionary of the following format :

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
