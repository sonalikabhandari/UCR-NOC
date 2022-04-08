
from django.urls import path
from django.conf.urls import include,url
from audit_processes import views
from django.views.generic import TemplateView
from rest_framework import routers
# from .views import AuditDetailView
from .import views



router = routers.DefaultRouter()


# router.register('aletheia',aletheia_rancidViewSet, basename='rancid')

urlpatterns = [
    path('', include(router.urls)),
    # path('aletheia/', views.AuditDetailView.as_view(),name='rancid'),
    url(r'^aletheia/$', views.Aletheia, name='rancid'),
    url(r'^DailyPrep/$', views.DailyPrep, name='dailyprep'),
    url(r'^DailyUpdateRRD/$', views.DailyUpdate_RRD, name='duRRD'),
    url(r'^DailyUpdateRP95/$', views.DailyUpdate_RP95, name='duRP95'),
    url(r'^DailyUpdateWAE/$', views.DailyUpdate_WAE, name='duWAE'),
    url(r'^DailyUpdateUCR/$', views.DailyUpdate_UCR, name='duUCR'),
]
