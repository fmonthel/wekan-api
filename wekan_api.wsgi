import os
import site
import sys


# Set current working directory
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
sys.path.insert(0, os.path.join(here, 'src'))

# Add the virtualenv's site-packages
site.addsitedir(os.path.join(here, 'env/local/lib/python2.7/site-packages'))

# Activate the virtualenv
activate_env = os.path.join(here, 'env/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

from wekan_api import app as application
