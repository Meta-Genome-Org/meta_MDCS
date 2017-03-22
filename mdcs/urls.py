"""mdcs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include("core_main_app.urls")),
    url(r'^home/', include("mdcs_home.urls")),
    url(r'^', include("core_website_app.urls")),
    url(r'^curate/', include("core_curate_app.urls")),
    url(r'^composer/', include("core_composer_app.urls")),
    url(r'^', include("core_parser_app.urls")),
    url(r'^explore/example/', include("core_explore_example_app.urls")),
    url(r'^federated_search/', include("core_explore_federated_search_app.urls")),
    url(r'^dashboard/', include("core_dashboard_app.urls")),
    url(r'^oai_pmh/', include("core_oaipmh_harvester_app.urls")),
]