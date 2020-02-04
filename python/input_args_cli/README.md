# Python3 Input Args Example

Each python script can take input from the user in two possible ways: either via Commandline arguments or via
environment variables. This example shows how to use cli arguments. 


## Variables 

In this example, the user is prompted to enter 3 values:

* username
* password
* secret

All three of these values will then be passed into our python script via cli arguments. 

```yaml

snippets:
  - name: script
    file: input_from_cli.py
    input_type: cli

```

The 'input_type: cli' attribute instructs panhandler to call the python script with the long form variable names
as cli arguments.

```python

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Example Username", type=str)
    parser.add_argument("-p", "--password", help="Example Password", type=str)
    parser.add_argument("-s", "--secret", help="Example Secret", type=str)

```


The script itself needs to be written in such a way as to take these inputs vai the cli. In this case, we are using the
'argparse' library to simplify this task.