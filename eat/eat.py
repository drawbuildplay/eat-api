"""WSGI App for WSGI Containers

This app should be used by external WSGI
containers. For example:

    $ gunicorn eat.app:app

NOTE: As for external containers, it is necessary
to put config files in the standard paths. There's
no common way to specify / pass configuration files
to the WSGI app when it is called from other apps.
"""

import routes

app = routes.Routes().app
