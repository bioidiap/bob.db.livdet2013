#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""A few checks at the LivDet 2013 database.
"""

import os, sys
import unittest
from . import Database

class LivDet2013TestCase(unittest.TestCase):
  """Performs various tests on the LivDet 2013 fingerprint liveness database."""

  def test01_biometrika(self):
    db = Database()
    f = db.objects(protocols='Biometrika', classes='spoof', groups='train')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(protocols='Biometrika', classes='spoof', groups='test')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(protocols='Biometrika', classes='live', groups='train')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), True)
    f = db.objects(protocols='Biometrika', classes='live', groups='test')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), True)

  def test02_crossmatch(self):

    db = Database()
    f = db.objects(protocols='CrossMatch', classes='spoof', groups='train')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(protocols='CrossMatch', classes='spoof', groups='test')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(protocols='CrossMatch', classes='live', groups='train')
    self.assertEqual(len(f), 1250)
    for k in f: self.assertEqual(k.is_live(), True)
    f = db.objects(protocols='CrossMatch', classes='live', groups='test')
    self.assertEqual(len(f), 1250)
    for k in f: self.assertEqual(k.is_live(), True)

  def test03_italdata(self):

    db = Database()
    f = db.objects(protocols='Italdata', classes='spoof', groups='train')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(protocols='Italdata', classes='spoof', groups='test')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(protocols='Italdata', classes='live', groups='train')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), True)
    f = db.objects(protocols='Italdata', classes='live', groups='test')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), True)

  def test04_swipe(self):

    db = Database()
    f = db.objects(protocols='Swipe', classes='spoof', groups='train')
    self.assertEqual(len(f), 979)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(protocols='Swipe', classes='spoof', groups='test')
    self.assertEqual(len(f), 1000)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(protocols='Swipe', classes='live', groups='train')
    self.assertEqual(len(f), 1221)
    for k in f: self.assertEqual(k.is_live(), True)
    f = db.objects(protocols='Swipe', classes='live', groups='test')
    self.assertEqual(len(f), 1153)
    for k in f: self.assertEqual(k.is_live(), True)

  def test05_full(self):

    db = Database()
    f = db.objects(classes='spoof', groups='train')
    self.assertEqual(len(f), 3979)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(classes='spoof', groups='test')
    self.assertEqual(len(f), 4000)
    for k in f: self.assertEqual(k.is_live(), False)
    f = db.objects(classes='live', groups='train')
    self.assertEqual(len(f), 4471)
    for k in f: self.assertEqual(k.is_live(), True)
    f = db.objects(classes='live', groups='test')
    self.assertEqual(len(f), 4403)
    for k in f: self.assertEqual(k.is_live(), True)

  def test06_repeated(self):

    db = Database()
    f = db.objects()
    all_stems = set([k.stem for k in f])
    self.assertEqual(len(f), len(all_stems))
