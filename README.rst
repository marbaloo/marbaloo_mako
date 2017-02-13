Cherrypy Mako Template
======================

`Mako <http://www.makotemplates.org/>`_ template support for cherrypy.

Installation
------------
::

    pip install marbaloo_mako

Usage
-----

::

    # templates/dir1/index.mak
    <h1>Today: ${today}</h1>


::

    # app.py
    import os
    import marbaloo_mako
    from datetime import date
    cherrypy.tools.mako = marbaloo_mako.Tool()

    class Root(object):
        @cherrypy.expose
        @cherrypy.tools.mako(filename='/index.mak')
        def simple(self):
            return  {'today': date.today()}

    root_path = os.path.dirname(__file__)
    cherrypy.quickstart(Root(), '/', {
                                '/': {
                                    'tools.mako.on': True,
                                    'tools.mako.directories': [os.path.join(root_path, 'templates/dir1')]
                                }
                            })
