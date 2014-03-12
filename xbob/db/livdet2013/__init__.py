#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Ivana Chingovska <ivana.chingovska@idiap.ch>
# Wed Feb 15 12:57:28 CET 2012

"""
The NUAA database is a spoofing attack database which consists of real accesses
and only printed photo attacks. There are three versions of the database:
version composed of raw images, version composed of the cropped faces detected
in the images and version composed of 64x64 normalized faces detected in the
images. There are only train and test set defined.

References:

  1. X. Tan, Y. Li, J. Liu, L. Jiang: "Face Liveness Detection from a Single
  Image with Sparse Low Rank Bilinear Discriminative Model", Proceedings of
  11th European Conference on Computer Vision (ECCV'10), Crete, Greece,
  September 2010; p.9-11
"""

import os
import six
from .models import *

class Database(object):

  protocols = ('Biometrika','CrossMatch','Italdata','Swipe')
  groups = ('train', 'test')
  classes = ('live', 'spoof')

  def __init__(self):
    from .driver import Interface
    from pkg_resources import resource_filename
    self.info = Interface()
    self.location = resource_filename(__name__, '')


  def objects(self, protocols=None, groups=None, classes=None):
    """Returns a list of unique :py:class:`.File` objects for the specific query by the user.

    Keyword Parameters:

    protocols
      The '

    groups
      One of the protocolar subgroups of data as specified in the tuple groups,
      or a tuple with several of them.  If you set this parameter to an empty
      string or the value None, we use reset it to the default which is to get
      all.

    classes
      Either "spoof", "live" or any combination of those (in a tuple). Defines
      the class of data to be retrieved.  If you set this parameter to an empty
      string or the value None, we use reset it to the default, ("live",
      "spoof").




    Returns: A list of :py:class:`.File` objects.

    """

    def check_validity(l, obj, valid, default):
      """Checks validity of user input data against a set of valid values"""
      if not l: return default
      elif isinstance(l, six.string_types): return check_validity((l,), obj, valid, default)
      for k in l:
        if k not in valid:
          raise RuntimeError('Invalid %s "%s". Valid values are %s, or lists/tuples of those' % (obj, k, valid))
      return l

    # check if protocols are valid
    VALID_PROTOCOLS = Database.protocols
    protocols = check_validity(protocols, "protocol", VALID_PROTOCOLS, VALID_PROTOCOLS)

    # check if groups set are valid
    VALID_GROUPS = Database.groups
    groups = check_validity(groups, "group", VALID_GROUPS, VALID_GROUPS)

    # 
    VALID_CLASSES = Database.classes
    classes = check_validity(classes, "class", VALID_CLASSES, VALID_CLASSES)

    retval = []

    for p in protocols:
      for g in groups:
        for c in classes:
          file_list = os.path.join(self.location,p,g,c+'.txt')
          retval += [File(k.strip()) for k in open(file_list, 'r').readlines() if k.strip()]

    return retval

