"""URL routing for the chapters application."""

from django.conf.urls import url

from django.views.generic import TemplateView
from . import views

app_name = "chapters"
urlpatterns = [
    # eg: /chapters/
    url(
        r"^$",
        views.IndexView.as_view(),
        name="index"
    ),
    url(
        r"^iframeinteractive/(?P<interactive_slug>[-\w]+)/$",
        TemplateView.as_view(template_name="chapters/interactives/iframe-base.html"),
        name="iframe_interactive"
    ),
    # eg: /chapters/interactives/sorting-algorithms/
    url(
        r"^interactives/(?P<interactive_slug>[-\w]+)/$",
        views.InteractiveView.as_view(),
        name="interactive"
    ),
    # eg: /chapters/glossary/
    url(
        r"^glossary/$",
        views.GlossaryList.as_view(),
        name="glossary"
    ),
    # eg: /chapters/glossary/json/
    url(
        r"^glossary/json/$",
        views.glossary_json,
        name="glossary_json"
    ),
    # eg: /chapters/algorithms/
    url(
        r"^(?P<chapter_slug>[-\w]+)/$",
        views.ChapterView.as_view(),
        name="chapter"
    ),

]
