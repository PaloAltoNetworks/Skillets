# Docker Ansible Example

Using a docker skillet, you can execute any Ansible project, using any available libraries in the docker image. This
allows you to distribute custom tools and scripts, or use existing dockerized tools, as a skillet. This is especially
important when using Ansible which can potentially have many dependencies that are specific to the playbook at hand.

Using a docker skillet, you can create a single docker image that contains all your dependencies and distribute
that with your Ansible project using the Skillet metadata file. 


## Example Script

There is also an example python script that shows how to use 
[Skilletlib](https://github.com/paloaltonetworks/skilletlib) to load and execute this skillet. 