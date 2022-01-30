"""PortfolioProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pages import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.homepage),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_ROOT+'/images/favicon.ico')),
    path('portfolio-admin/', admin.site.urls),
    path('home/',views.homepage),
    path('profile/',views.profile),
    path('portfolio/',views.profile),
    path('contact/',views.contact),
    path('fields/',views.fields),
    path('resumes', views.resumes),
    path('text_to_speech_demo', views.text_to_speech_demo),
    path('article_finder', views.article_radar),
    path('article_results', views.article_results),
    path('form-improvements', views.form_improvements),
    path('projects/', views.projects),
    path('projects/ceres-demo', views.ceres_demo),

    path('projects/ceres/<int:ceres_report_id>/ceres-report', views.ceres_report_view),
    path('projects/ceres/update', views.ceres_report_update),

    path('projects/score-pred', views.scorepred),
    path('projects/image_classifier', views.imageclass),
    path('projects/doctrina', views.doctrina),
    path('projects/email-generator', views.emailgenerator),
    
    path('projects/ceres-demo', views.ceres_demo),
    path('projects/ceres', views.ceres_demo),
    path('projects/text_to_speech_demo', views.text_to_speech_demo),
    path('projects/article_finder', views.article_radar),
    path('projects/article_results', views.article_results),
    path('bi-final', views.bi_final),
    path('projects/bi-final', views.bi_final),
    path('tester', views.tester),


    path('projects/vehicle_detector', views.vehicle_detector),
    path('projects/flappybird', views.flappybird),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += staticfiles_urlpatterns()