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

from datetime import datetime

from django.test import TestCase

from models import Section, Subsection, Card

class SectionTestCase(TestCase):
    def setUp(self):
        pass

    def test_empty_section(self):
        """
        Making tests with empty or incomplete Section objects.
        """

        sec = Section.objects.create()
        self.assertEquals(str(sec), "")
        self.assertEquals(sec.title, "")
        self.assertIsInstance(sec, Section)
        self.assertIsInstance(sec.creation_time, datetime)
        self.assertIsInstance(sec.last_modified, datetime)
        self.assertIsNone(sec.box)
        self.assertIsNone(sec.short)
        self.assertIsNone(sec.created_by)
        self.assertTrue(sec.enable)

    def test_simple_section(self):
        """
        Creating a simple section, put some values and test its persistence.
        """

        sec = Section(title="title text", short="short")
        sec.save()
        self.assertEquals(sec.title, "title text")
        self.assertEquals(sec.short, "short")
        sec.delete()

class SubsectionTestCase(TestCase):
    def setUp(self):
        pass

    def test_empty_subsection(self):
        """
        Making tests with empty or incomplete Subsection objects.
        """

        sub = Subsection.objects.create()
        self.assertEquals(str(sub), "")
        self.assertEquals(sub.title, "")
        self.assertIsInstance(sub, Subsection)
        self.assertIsInstance(sub.creation_time, datetime)
        self.assertIsInstance(sub.last_modified, datetime)
        self.assertIsNone(sub.section)
        self.assertIsNone(sub.short)
        self.assertIsNone(sub.created_by)
        self.assertTrue(sub.enable)

    def test_simple_subsection(self):
        """
        Creating a simple subsection, put some values and test its persistence.
        """

        sub = Subsection(title="title text", short="short")
        sub.save()
        self.assertEquals(sub.title, "title text")
        self.assertEquals(sub.short, "short")
        sub.delete()

    def test_subsection_with_cards(self):
        """
        Create a subsection, some cards and test their relationship.
        """

        sub = Subsection(title="test title")
        c = range(10)
        for i in range(10):
            c[i] = Card(front=i)
            c[i].sub = sub
            c[i].save()

        for i in range(10):
            self.assertEquals(c[i].sub.title, "test title")

class CardTestCase(TestCase):
    def setUp(self):
        pass

    def test_empty_card(self):
        """
        Making tests with empty or incomplete Card objects.
        """

        card = Card.objects.create()
        self.assertEquals(str(card), "")
        self.assertEquals(card.front, "")
        self.assertIsInstance(card, Card)
        self.assertIsInstance(card.creation_time, datetime)
        self.assertIsInstance(card.last_modified, datetime)
        self.assertIsNone(card.back)
        self.assertIsNone(card.label)
        self.assertIsNone(card.created_by)
        self.assertTrue(card.enable)

    def test_simple_card(self):
        """
        Creating a simple card, put some values and test its persistence.
        """

        card = Card(front="front text", back="back text", label="card label")
        card.save()
        self.assertEquals(card.front, "front text")
        self.assertEquals(card.back, "back text")
        self.assertEquals(card.label, "card label")
        card.delete()

