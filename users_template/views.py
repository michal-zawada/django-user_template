from django.views.generic import TemplateView

class LoggedIn(TemplateView):
	template_name='logged_in.html'

class LoggedOut(TemplateView):
	template_name='logged_out.html'


class HomePage(TemplateView):
	template_name='index.html'