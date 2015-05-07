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

import logging

from rest_framework import viewsets

from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from models import Box, Section, Subsection, Card
from serializers import UserSerializer, GroupSerializer
from serializers import BoxSerializer, SectionSerializer, SubsectionSerializer, CardSerializer

class BoxListView(ListView):
    model = Box
    paginate_by = 10

    def get_queryset(self):
        q = super(BoxListView, self).get_queryset()
        q = q.order_by('last_modified').reverse()
        return q

class BoxDetailView(DetailView):
    model = Box

    def get_context_data(self, **kwargs):
        context = super(BoxDetailView, self).get_context_data(**kwargs)
        context['sec'] = Section.objects.filter(box=self.kwargs['pk'])
        return context

class BoxCreateView(CreateView):
    model = Box
    fields = ['title', 'public'] 
    success_url = reverse_lazy('box_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(BoxCreateView, self).form_valid(form)

class BoxUpdateView(UpdateView):
    model = Box
    fields = ['title', 'public']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('box_list')

class BoxDeleteView(DeleteView):
    model = Box
    success_url = reverse_lazy('box_list')

class SectionListView(ListView):
    model = Section
    paginate_by = 10

    def get_queryset(self):
        q = super(SectionListView, self).get_queryset()
        q = q.order_by('last_modified').reverse()
        return q

class SectionDetailView(DetailView):
    model = Section

    def get_context_data(self, **kwargs):
        context = super(SectionDetailView, self).get_context_data(**kwargs)
        context['sub'] = Subsection.objects.filter(section=self.kwargs['pk'])
        return context

class SectionCreateView(CreateView):
    model = Section
    fields = ['box', 'title', 'short', 'enable']
    success_url = reverse_lazy('sec_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(SectionCreateView, self).form_valid(form)

class SectionUpdateView(UpdateView):
    model = Section
    fields = ['box', 'title', 'short', 'enable'] 
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('sec_list')

class SectionDeleteView(DeleteView):
    model = Section
    success_url = reverse_lazy('sec_list')

class SubsectionListView(ListView):
    model = Subsection
    paginate_by = 10

    def get_queryset(self):
        q = super(SubsectionListView, self).get_queryset()
        q = q.order_by('last_modified').reverse()
        return q

class SubsectionDetailView(DetailView):
    model = Subsection

    def get_context_data(self, **kwargs):
        context = super(SubsectionDetailView, self).get_context_data(**kwargs)
        context['card'] = Card.objects.filter(subsection=self.kwargs['pk'])
        return context

class SubsectionCreateView(CreateView):
    model = Subsection
    fields = ['section', 'title', 'short', 'enable'] 
    success_url = reverse_lazy('sub_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(SubsectionCreateView, self).form_valid(form)

class SubsectionUpdateView(UpdateView):
    model = Subsection
    fields = ['section', 'title', 'short', 'enable'] 
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('sub_list')

class SubsectionDeleteView(DeleteView):
    model = Subsection
    success_url = reverse_lazy('sub_list')

class CardListView(ListView):
    model = Card
    paginate_by = 10

    def get_queryset(self):
        q = super(CardListView, self).get_queryset()
        q = q.order_by('last_modified').reverse()
        return q

class CardDetailView(DetailView):
    model = Card

    def get_context_data(self, **kwargs):
        context = super(CardDetailView, self).get_context_data(**kwargs)
        return context

class CardCreateView(CreateView):
    model = Card
    fields = ['subsection', 'front', 'back', 'enable', 'label']
    success_url = reverse_lazy('card_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CardCreateView, self).form_valid(form)

class CardUpdateView(UpdateView):
    model = Card
    fields = ['subsection', 'front', 'back', 'enable', 'label'] 
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('card_list')

class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy('card_list')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class SubsectionViewSet(viewsets.ModelViewSet):
    queryset = Subsection.objects.all()
    serializer_class = SubsectionSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

