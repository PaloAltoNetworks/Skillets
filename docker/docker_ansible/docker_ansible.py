# Copyright (c) 2020, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Authors: Nathan Embery

from skilletlib import SkilletLoader

# use skilletLoader from skilletlib to load and execute the skillet
sl = SkilletLoader()

# our skillet is located in the same directory
skillet = sl.load_skillet_from_path('.')

# each skillet can specify what items are customizable. 
# Create a context dictionary to hold our customized variables for this execution.
context = dict()
context['username'] = 'admin'
context['password'] = 'admin'
context['ip_address'] = '10.10.10.10'

# This Ansible playbook may take a very long time. Use the 'execute_async' method to poll for the output as it happens
# As with the execute method, we pass in our context object
# The primary different is 'execute_async' returns a generator that we can iterate over to get the output as it happens
# from the docker container
for l in skillet.execute_async(context):
    print(l)

# when using 'execute_async' you then call 'get_results' to get the normal output that would get form just calling
# 'execute'
out = skillet.get_results()

# Now we can do something interesting with our output
print(out)
