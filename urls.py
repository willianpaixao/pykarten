"""
PYKARTEN is a web app for creating and exporting flashcards.
PYKARTEN  Copyright (C) 2014  Willian Paixao <willian@ufpa.br>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#from rest_framework import routers

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from views import *

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)
#router.register(r'box', BoxViewSet)
#router.register(r'sec', SectionViewSet)
#router.register(r'sub', SubsectionViewSet)
#router.register(r'cards', CardViewSet)

urlpatterns = patterns('karte.views',

    url(r'api/', include(router.urls)),

    url(r'box/$', login_required(BoxListView.as_view()),
        name="box_list"),
    url(r'box/add/$', login_required(BoxCreateView.as_view()),
        name="box_create"),
    url(r'box/(?P<pk>\d+)/$', login_required(BoxDetailView.as_view()),
        name="box"),
    url(r'box/(?P<pk>\d+)/edit/$', login_required(BoxUpdateView.as_view()),
        name="box_update"),
    url(r'box/(?P<pk>\d+)/delete/$', login_required(BoxDeleteView.as_view()),
        name="box_delete"),

    url(r'sec/$', login_required(SectionListView.as_view()),
        name="sec_list"),
    url(r'sec/add/$', login_required(SectionCreateView.as_view()),
        name="sec_create"),
    url(r'sec/(?P<pk>\d+)/$', login_required(SectionDetailView.as_view()),
        name="sec"),
    url(r'sec/(?P<pk>\d+)/edit/$', login_required(SectionUpdateView.as_view()),
        name="sec_update"),
    url(r'sec/(?P<pk>\d+)/delete/$', login_required(SectionDeleteView.as_view()),
        name="sec_delete"),

    url(r'sub/$', login_required(SubsectionListView.as_view()),
        name="sub_list"),
    url(r'sub/add/$', login_required(SubsectionCreateView.as_view()),
        name="sub_create"),
    url(r'sub/(?P<pk>\d+)/$', login_required(SubsectionDetailView.as_view()),
        name="sub"),
    url(r'sub/(?P<pk>\d+)/edit/$',
        login_required(SubsectionUpdateView.as_view()),
        name="sub_update"),
    url(r'sub/(?P<pk>\d+)/delete/$',
        login_required(SubsectionDeleteView.as_view()),
        name="sub_delete"),

    url(r'card/$', login_required(CardListView.as_view()),
        name="card_list"),
    url(r'card/add/$', login_required(CardCreateView.as_view()),
        name="card_create"),
    url(r'card/(?P<pk>\d+)/$', login_required(CardDetailView.as_view()),
        name="card"),
    url(r'card/(?P<pk>\d+)/edit/$', login_required(CardUpdateView.as_view()),
        name="card_update"),
    url(r'card/(?P<pk>\d+)/delete/$', login_required(CardDeleteView.as_view()),
        name="card_delete"),
)

