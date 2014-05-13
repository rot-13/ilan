import haml
import mako.lookup

lookup = mako.lookup.TemplateLookup(
        directories=["./views"],
        preprocessor=haml.preprocessor
)

def get_template(name):
    return lookup.get_template(name)
