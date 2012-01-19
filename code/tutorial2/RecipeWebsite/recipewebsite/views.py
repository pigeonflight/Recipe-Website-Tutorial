from pyramid.view import view_config
from .models import RecipeSite

@view_config(context=RecipeSite, renderer='templates/welcome.pt')
def my_view(request):
    return {'project':'RecipeWebsite'}
