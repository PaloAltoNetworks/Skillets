from skilletlib.skilletLoader import SkilletLoader

sl = SkilletLoader()
skillet = sl.load_skillet_from_path('.')

context = dict()
context['service_ip'] = '1.2.3.4'

output = skillet.execute(context)

template = output.get('template', None)

if template is None:
    print('Could not render template')
    exit(1)

print(template)
