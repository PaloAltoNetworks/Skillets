from skilletlib.skilletLoader import SkilletLoader
import os

# set debug flag in the environment
os.environ['SKILLET_DEBUG'] = "True"

# create skilletLoader object to find and load our skillet
sl = SkilletLoader()

# load the skillet found in this directory
skillet = sl.load_skillet_from_path('.')

# set up our context dict - not used in this case, but can be used to pass variables to your skillet
context = dict()
context['api_key'] = 'YOUR PRISMA ACCESS KEY HERE'

# execute the skillet and return the data
out = skillet.execute(context)

# do something with the output here
print('Skillet return data:')

print(out)

print('And all done')
