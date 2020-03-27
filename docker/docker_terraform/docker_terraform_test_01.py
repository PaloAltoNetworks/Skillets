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

# Skilletlib includes the SkilletLoader class that is used to load and validate skillets from the filesystem
# as well as from git repositories
from skilletlib.skilletLoader import SkilletLoader

# instantiate the class - no parameters are needed, though an optional path can be specified which will
# recursively load all skillets found in that directory
sl = SkilletLoader()

# This method will load the first skillet found in the path specified
skillet = sl.load_skillet_from_path('.')

# Skillet variables are overridden in the context. Any items in this dict that have the same 'name' as a
# variable defined in the skillet will be used to render the skillet snippets and metadata
context = dict()

# in this case, we will set the version
context['terraform_version'] = '0.11.13'

# Once the context is set up, call the 'execute' method.
out = skillet.execute(context)

# The output will always be a json formatted string
print(out)

# In this case, the output returned is:
# {
#   'snippets': {
#     'terraform_test': {
#       'results': 'success',
#       'raw': 'Terraform v0.11.13\n\nYour version of Terraform is out of date! The latest version\nis 0.12.24. You can update by downloading from www.terraform.io/downloads.html\n'
#     }
#   },
#   'outputs': {}
# }

# Return data will always be a dictionary with the 'snippets' and 'outputs' keys. Snippets contains a dict of each
# snippet that was executed in the skillet along with it's 'results' and 'raw' output. Outputs will be any captured
# outputs as defined in the skillet
