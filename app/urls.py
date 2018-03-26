from django.conf.urls import url

from .views import activation_list, profile_list, submissions_list ,brand_list


urlpatterns = [
    url(r'^activations$', activation_list, name='activation_list'),
    url(r'^activations/submissions$', submissions_list, name='submissions_list'),
    url(r'^activations/submissions-with-brands$', brand_list, name='brand_list'),
    url(r'^profiles$', profile_list, name='profile_list'),
]
