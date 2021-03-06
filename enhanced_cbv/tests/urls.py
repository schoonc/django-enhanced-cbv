from django.conf.urls.defaults import *

from enhanced_cbv.tests.views import (AuthorsArticlesView,
     AuthorsArticlesModelsView, AuthorsInlinesView, AuthorsListFilteredView, )


urlpatterns = patterns('',

    # FormSetsView
    (r'^edit/formsets/$',
        AuthorsArticlesView.as_view()),
    (r'^edit/modelformsets/$',
        AuthorsArticlesModelsView.as_view()),
    (r'^edit/inlineformsets/$',
        AuthorsInlinesView.as_view()),
    (r'^list/filtered/$',
        AuthorsListFilteredView.as_view()),
)
