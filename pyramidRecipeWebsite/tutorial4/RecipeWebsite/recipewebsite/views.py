from pyramid.view import view_config
from .models import RecipeSite
from pyramid.renderers import get_renderer
from pyramid.decorator import reify

#def master_template():
#    renderer = get_renderer("templates/global.pt")
#    master = renderer.implementation().macros['master']
#    return master


class SiteViews(object):

    def __init__(self, request):
        self.request = request
        renderer = get_renderer("templates/global.pt")
        self.master_template = renderer.implementation().macros['master']


    @reify
    def company_name(self):
        return "Alteroo"

    @view_config(renderer='templates/welcome.pt')
    def index_view(self):
         return {'page_title':'Home'}

    @view_config(renderer='templates/recipe.pt')
    def recipe_view(self):
        return {'page_title':'Recipe'}

