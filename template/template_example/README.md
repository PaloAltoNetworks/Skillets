# Template Example

Template are a very simple type of skillet that makes it easy to render configuration files, REST payloads, 
set commands, third party network device configurations, etc. 

# Snippet Definition

Template type skillets require the following attributes present in the snippet metadata section:

* name - The name of this snippet
* file - The jinja2 template to load and render using the provided context

Template skillets only use the first defined snippet.


