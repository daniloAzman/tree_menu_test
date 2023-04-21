from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    """
    Render the index page.
    """
    template_name = 'index.html'