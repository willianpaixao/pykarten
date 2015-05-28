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

from django.contrib.auth.models import User
from django.db import models

class Box(models.Model):
    """
    Box model.
    A single attribute, named title resumes the Box. It will contains one or
    more sections.
    """

    created_by = models.ForeignKey(User, related_name="box_created_by",
            null=True, on_delete=models.SET_NULL)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=512)
    public = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "boxes"

    def __unicode__(self):
        if not self.title:
            return ""
        return self.title

    def get_absolute_url(self):
        return reverse('box_edit', kwargs={'pk': self.pk})

class Section(models.Model):
    """
    Section model.
    The section is the first abstraction of categorization for the cards. It
    contains a long and short name called title and short respectfully.
    """

    created_by = models.ForeignKey(User, related_name="sec_created_by",
            null=True, on_delete=models.SET_NULL)
    box = models.ForeignKey(Box, null=True, on_delete=models.SET_NULL)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    short = models.CharField(max_length=512, blank=True, null=True)
    title = models.CharField(max_length=512)
    enable = models.BooleanField(default=True)

    def __unicode__(self):
        if not self.title:
            return ""
        return self.title

    def get_absolute_url(self):
        return reverse('sec_edit', kwargs={'pk': self.pk})

class Subsection(models.Model):
    created_by = models.ForeignKey(User, related_name="sub_created_by",
            null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    short = models.CharField(max_length=512, blank=True, null=True)
    title = models.CharField(max_length=512, blank=True)
    enable = models.BooleanField(default=True)

    def __unicode__(self):
        if not self.title:
            return ""
        return self.title

    def get_absolute_url(self):
        return reverse('sub_edit', kwargs={'pk': self.pk})

class Card(models.Model):
    """
    Most important class of this whole program.
    The card is the singular unit of information. It contains a front and back
    texts. Is grouped in subsections, tagged by a label and can be disabled from
    compiling. It has always a author called user.
    """

    created_by = models.ForeignKey(User, related_name="card_created_by",
            null=True, on_delete=models.SET_NULL)
    subsection = models.ForeignKey(Subsection, blank=True, null=True,
            on_delete=models.SET_NULL)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    front = models.TextField()
    back = models.TextField(blank=True, null=True)
    enable = models.BooleanField(default=True)
    label = models.CharField(max_length=512, blank=True, null=True)

    def __unicode__(self):
        if not self.front:
            return ""
        return self.front

    def get_absolute_url(self):
        return reverse('card_edit', kwargs={'pk': self.pk})

