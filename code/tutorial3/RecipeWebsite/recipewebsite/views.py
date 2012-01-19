from pyramid.view import view_config
from .models import RecipeSite
from pyramid.renderers import get_renderer

def master_template():
    renderer = get_renderer("templates/global.pt")
    master = renderer.implementation().macros['master']
    return master

@view_config(context=RecipeSite, renderer='templates/welcome.pt')
def my_view(request):
    return {'project':'RecipeWebsite'}

@view_config(renderer='templates/recipe.pt',name='recipe_view')
def recipe(request):
    return {master:master_template()}
