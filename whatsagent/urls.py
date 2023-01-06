from django.urls import path
from whatsagent.api.views import user_signup

urlpatterns = [
    path('api/signup/', user_signup)
]
