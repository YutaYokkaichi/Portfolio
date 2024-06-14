from django.urls import path
from .views import home, experience, education, future_insights

urlpatterns = [
    path('', home, name='home'),
    path('experience/', experience, name='experience'),
    path('education/', education, name='education'),
    path('future-insights/', future_insights, name='future_insights'),
]
