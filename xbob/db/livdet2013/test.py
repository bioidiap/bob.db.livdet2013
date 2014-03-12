#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Ivana Chingovska <ivana.chingovska@idiap.ch>
# Tue Feb 21 11:44:31 CET 2012
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

"""A few checks at the NUAA database.
"""

import os, sys
import unittest
from . import Database
import bob

class NUAADatabaseTest(unittest.TestCase):
  """Performs various tests on the NUAA spoofing attack database."""

  """
  def test01_query(self):
    db = Database()
    f = db.files(versions='raw', cls='real', groups='train')
    self.assertEqual(len(set(f.values())), 1743) # total number of Clients in the training set
    f = db.files(versions='raw', cls='attack', groups='train')
    self.assertEqual(len(set(f.values())), 1748) # total number of Imposters in the training set
    f = db.files(versions='raw', cls='real', groups='test')
    self.assertEqual(len(set(f.values())), 3362) # total number of Clients in the test set
    f = db.files(versions='raw', cls='attack', groups='test')
    self.assertEqual(len(set(f.values())), 5761) # total number of Imposters in the test set
    
    f = db.files(versions='detected_face')
    for k,v in f.items():
      self.assertTrue( (v.find('Detectedface') != -1) )
  """
  
  
  def filtering(self, exp_number, v=None, c=None, g=None, cno=None, gl=None, cond=None, sess=None):
    db = Database()
    f = db.files(versions=v, cls=c, groups=g)
    ff = db.filter_files(f, client_no=cno, glasses=gl, conditions=cond, session=sess)
    self.assertEqual(len(set(ff.values())), exp_number) # number of session 02 images into the test set is 0
  

  """
  def test02_filtering1(self):
    self.filtering(0, v='raw', c='real', g='test', sess='02') # number of session 02 images into the test set is 0
  

  def test03_filtering2(self):
    self.filtering(1744, v='raw', g='train', sess='01') # number of session 01 images into the training set

  def test04_filtering3(self):
    self.filtering(468, v='detected_face', c='attack', g='test', cno='0016') # number of client 0016 images into the test set

  def test05_filtering4(self):
    self.filtering(0, v='normalized_face', c='real', gl='00', cno='0015') # number of client 0015 images without glasses = 0
  """

  """
  def test06_query2(self):
    DEF_DB_DIR = ''
    db = Database()
    f = db.files(directory=DEF_DB_DIR, versions='normalized_face', cls='real', groups='train', extension='.bmp')
    for k,v in f.items():
      self.assertTrue( (v.find(DEF_DB_DIR) != -1) )
      self.assertTrue( (v.find('.bmp') != -1) )
      self.assertTrue( (v.find('NormalizedFace') != -1) )
  """
 
  """
  def test07_cross_valid(self): # testing the cross-validation subsets
    db = Database()
    files_train_real = db.files(versions='raw', cls='real', groups='train')
    files_train_attack = db.files(versions='raw', cls='attack', groups='train')
    '''
    db.cross_valid_gen(len(files_train_real.items()), len(files_train_attack.items()), 10)
    '''
    subsets_real, subsets_attack = db.cross_valid_read()
    self.assertEqual(len(subsets_real), 10)
    self.assertEqual(len(subsets_attack), 10)
    for i in range(0,10):
      self.assertTrue(len(subsets_real[i]) in (174, 175))
      self.assertTrue(len(subsets_attack[i]) in (174, 175))

    files_real_val, files_real_train = db.cross_valid_foldfiles(version='raw', cls='real', fold_no=1)
    self.assertTrue(len(files_real_val) in (174, 175)) # number of samples in validation subset of real accesses
    self.assertTrue(len(files_real_train) in (1568, 1569)) # number of samples in training subset of real accesses
    files_attack_val, files_attack_train = db.cross_valid_foldfiles(version='detected_face', cls='attack', fold_no=3, directory='xxx', extension='.jpg')
    self.assertTrue(len(files_attack_val) in (174, 175)) # number of samples in validation subset of attacks
    self.assertTrue(len(files_attack_train) in (1573, 1574)) # number of samples in training subset of attacks
  """  

  def test08_dumplist(self):
    from bob.db.script.dbmanage import main
    self.assertEqual(main('nuaa dumplist --self-test'.split()), 0)

  def test09_checkfiles(self):
    from bob.db.script.dbmanage import main
    self.assertEqual(main('nuaa checkfiles --self-test'.split()), 0)
  
  def test10_manage_files(self):

    from bob.db.script.dbmanage import main

    self.assertEqual(main('nuaa files'.split()), 0)

  def test11_query3(self):
    db = Database()
    fobj = db.objects(versions='raw', cls='real', groups='train')
    self.assertEqual(len(fobj), 1743) # total number of Clients in the training set
    fobj = db.objects(versions='raw', cls='attack', groups='train')
    self.assertEqual(len(fobj), 1748) # total number of Imposters in the training set
    fobj = db.objects(versions='raw', cls='real', groups='test')
    self.assertEqual(len(fobj), 3362) # total number of Clients in the test set
    fobj = db.objects(versions='raw', cls='attack', groups='test')
    self.assertEqual(len(fobj), 5761) # total number of Imposters in the test set
    fobj = db.objects(versions='raw', cls='attack', groups='train', client_no='0001', glasses='01', session='01')
    self.assertEqual(len(fobj), 0) # total number of Imposters in the training set

  def test12_cross_valid_obj(self): # testing the cross-validation subsets
    db = Database()
    obj_train_real = db.objects(versions='raw', cls='real', groups='train')
    obj_train_attack = db.objects(versions='raw', cls='attack', groups='train')
    '''
    db.cross_valid_gen(len(files_train_real.items()), len(files_train_attack.items()), 10)
    '''
    subsets_real, subsets_attack = db.cross_valid_read()
    self.assertEqual(len(subsets_real), 10)
    self.assertEqual(len(subsets_attack), 10)
    for i in range(0,10):
      self.assertTrue(len(subsets_real[i]) in (174, 175))
      self.assertTrue(len(subsets_attack[i]) in (174, 175))

    obj_real_val, obj_real_train = db.cross_valid_foldobjects(version='raw', cls='real', fold_no=1)
    self.assertTrue(len(obj_real_val) in (174, 175)) # number of samples in validation subset of real accesses
    self.assertTrue(len(obj_real_train) in (1568, 1569)) # number of samples in training subset of real accesses
    obj_attack_val, obj_attack_train = db.cross_valid_foldobjects(version='detected_face', cls='attack', fold_no=3)
    self.assertTrue(len(obj_attack_val) in (174, 175)) # number of samples in validation subset of attacks
    self.assertTrue(len(obj_attack_train) in (1573, 1574)) # number of samples in training subset of attacks
