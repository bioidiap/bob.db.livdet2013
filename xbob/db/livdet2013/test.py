#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# David Yambay <yambayda@gmail.com>
# Fri Mar 14 14:44:31 CET 2014
#
# Copyright (C) 2011-2012 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A few checks at the LivDet 2013 database.
"""

import os, sys
import unittest
from . import Database
import bob

class LivDet2013TestCase(unittest.TestCase):
  """Performs various tests on the LivDet 2013 fingerprint liveness database."""

  def test01_biometrika(self):
    db = Database()
    f = db.objects(protocols='Biometrika', classes='spoof', groups='train')
    self.assertEqual(len(f), 1000)
    f = db.objects(protocols='Biometrika', classes='spoof', groups='test')
    self.assertEqual(len(f), 1000)
    f = db.objects(protocols='Biometrika', classes='live', groups='train')
    self.assertEqual(len(f), 1000)
    f = db.objects(protocols='Biometrika', classes='live', groups='test')
    self.assertEqual(len(f), 1000)

  def test02_crossmatch(self):

    db = Database()
    f = db.objects(protocols='CrossMatch', classes='spoof', groups='train')
    self.assertEqual(len(f), 1000)
    f = db.objects(protocols='CrossMatch', classes='spoof', groups='test')
    self.assertEqual(len(f), 1000)
    f = db.objects(protocols='CrossMatch', classes='live', groups='train')
    self.assertEqual(len(f), 1250)
    f = db.objects(protocols='CrossMatch', classes='live', groups='test')
    self.assertEqual(len(f), 1250)

  def test03_italdata(self):

    db = Database()
    f = db.objects(protocols='Italdata', classes='spoof', groups='train')
    self.assertEqual(len(f), 1000)
    f = db.objects(protocols='Italdata', classes='spoof', groups='test')
    self.assertEqual(len(f), 1000)
    f = db.objects(protocols='Italdata', classes='live', groups='train')
    self.assertEqual(len(f), 1000)
    f = db.objects(protocols='Italdata', classes='live', groups='test')
    self.assertEqual(len(f), 1000)

  def test04_swipe(self):

    db = Database()
    f = db.objects(protocols='Swipe', classes='spoof', groups='train')
    self.assertEqual(len(f), 979)
    f = db.objects(protocols='Swipe', classes='spoof', groups='test')
    self.assertEqual(len(f), 1000)
    f = db.objects(protocols='Swipe', classes='live', groups='train')
    self.assertEqual(len(f), 1221)
    f = db.objects(protocols='Swipe', classes='live', groups='test')
    self.assertEqual(len(f), 1153)

  def test05_full(self):

    db = Database()
    f = db.objects(classes='spoof', groups='train')
    self.assertEqual(len(f), 3979)
    f = db.objects(classes='spoof', groups='test')
    self.assertEqual(len(f), 4000)
    f = db.objects(classes='live', groups='train')
    self.assertEqual(len(f), 4471)
    f = db.objects(classes='live', groups='test')
    self.assertEqual(len(f), 4403)

  def test06_repeated(self):

    db = Database()
    f = db.objects()
    all_stems = set([k.stem for k in f])
    self.assertEqual(len(f), len(all_stems))
