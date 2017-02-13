import cherrypy
from mako.lookup import TemplateLookup


class Tool(cherrypy.Tool):
    _lookups = {}

    def __init__(self):
        cherrypy.Tool.__init__(self, 'before_handler',
                               self.callable,
                               priority=20)

    def callable(self,
                 filename=None,
                 directories=None,
                 module_directory=None,
                 collection_size=-1):
        if filename is None or directories is None:
            return
        # Find the appropriate template lookup.
        key = (tuple(directories), module_directory)

        try:
            lookup = self._lookups[key]
        except KeyError:
            lookup = TemplateLookup(directories=directories,
                                    module_directory=module_directory,
                                    collection_size=collection_size,
                                    input_encoding='utf8')
            self._lookups[key] = lookup
        cherrypy.request.lookup = lookup
        # Replace the current handler.
        cherrypy.request.template = template = lookup.get_template(filename)
        inner_handler = cherrypy.serving.request.handler

        def wrapper(*args, **kwargs):
            context = inner_handler(*args, **kwargs)
            response = template.render(**context)
            return response

        cherrypy.serving.request.handler = wrapper




