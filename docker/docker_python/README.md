# Docker Python Script Example

Using a docker skillet, you can execute any python script, using any available libraries in the docker image. This
allows you to distribute custom tools and scripts, or use existing dockerized tools, as a skillet. Although
Panhandler allows you to install a virtualenv when using a python skillet, it may still be desirable to distribute
your python tooling as a docker image.

This example uses the standard alpine linux Python image to execute the script found in this directory. More 
interesting examples could use a custom docker image with all the requirements, libraries, and tools pre-installed.

## Example Script

There is also an example python script that shows how to use 
[Skilletlib](https://github.com/paloaltonetworks/skilletlib) to load and execute this skillet. 