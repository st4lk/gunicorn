# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license. 
# See the NOTICE for more information.


import os

if os.environ.get('release') != "true":

    minor_tag = "-dev"
    try:
        from gunicorn.util import popen3

        stdin, stdout, stderr = popen3("git rev-parse --short HEAD --")
        error = stderr.read()
        if not error:
            minor_tag = ".%s-git" % stdout.read()
    except OSError:        
        pass
else:
    minor_tag = ""
    

version_info = (0, 10, "1%s" % minor_tag)
__version__ = ".".join(map(str, version_info))
