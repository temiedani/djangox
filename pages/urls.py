from django.urls import path
# from django.views.generic import TemplateView


from .views import HomePageView , AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    # path('about/', TemplateView.as_view(template_name="pages/about.html")),

]