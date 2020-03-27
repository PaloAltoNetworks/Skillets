from skilletlib.skilletLoader import SkilletLoader

sl = SkilletLoader()
skillet = sl.load_skillet_from_path('.')
out = skillet.execute(dict())
print(out)

# output in this case:
# {'snippets': {'shell_execute': {'results': 'success', 'raw': 'This is an example shell script!\nYour script argument was argument_01\n'}}, 'outputs': {}}

# To get the raw output only, you can pull it from the output
print(out['snippets']['shell_execute']['raw'])

