import cherrypy
import marbaloo_mako
from cherrypy.test import helper
import os
from datetime import date


class CPTest(helper.CPWebCase):

    def setup_server():
        cherrypy.tools.mako = marbaloo_mako.Tool()

        class Root(object):
            @cherrypy.expose
            @cherrypy.tools.mako(filename='/simple.mak')
            def simple(self):
                return {}

            @cherrypy.expose
            @cherrypy.tools.mako(filename='/unicode.mak')
            def unicode(self):
                return {}

            @cherrypy.expose
            @cherrypy.tools.mako(filename='/advanced.mak')
            def advanced(self):
                return {'today': date.today()}

        root_path = os.path.dirname(__file__)
        cherrypy.tree.mount(Root(), '/', {
                                '/': {
                                    'tools.mako.on': True,
                                    'tools.mako.directories': [os.path.join(root_path, 'templates/dir1'),
                                                               os.path.join(root_path, 'templates/dir2')]
                                }
                            })
    setup_server = staticmethod(setup_server)

    def test_simple(self):
        self.getPage("/simple")
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'text/html;charset=utf-8')
        self.assertBody('<h1>hello world</h1>')

    def test_unicode(self):
        self.getPage("/unicode")
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'text/html;charset=utf-8')
        self.assertBody(('Hallo wêreld, Здравей, свят, 世界您好, Ahoj světe, Γεια σου κόσμε, שלום לך עולם, '
                         'हैलो वर्ल्डm ハローワールド,  , หวัดดีชาวโลก, Привіт, народ, سلام دنيا, Chào thế giới'
                         ))

    def test_advanced(self):
        self.getPage("/advanced")
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'text/html;charset=utf-8')
        self.assertBody('<span>today: %s</span>' % date.today())
