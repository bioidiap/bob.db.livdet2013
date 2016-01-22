.. vim: set fileencoding=utf-8 :
.. Andre Anjos <andre.anjos@idiap.ch>
.. Mon 18 Jan 2016 16:31:16 CET

.. image:: https://travis-ci.org/bioidiap/bob.db.livdet2013.svg?branch=master
   :target: https://travis-ci.org/bioidiap/bob.db.livdet2013
.. image:: https://coveralls.io/repos/bioidiap/bob.db.livdet2013/badge.svg?branch=master
   :target: https://coveralls.io/r/bioidiap/bob.db.livdet2013
.. image:: https://img.shields.io/badge/github-master-0000c0.png
   :target: https://github.com/bioidiap/bob.db.livdet2013/tree/master
.. image:: http://img.shields.io/pypi/v/bob.db.livdet2013.png
   :target: https://pypi.python.org/pypi/bob.db.livdet2013
.. image:: http://img.shields.io/pypi/dm/bob.db.livdet2013.png
   :target: https://pypi.python.org/pypi/bob.db.livdet2013


=========================================
Livdet 2013 Fingerprint Liveness Database
=========================================

The Livdet 2013 `Fingerprint Liveness Database <http://livdet.org>`_
[Ghiani2013]_ is a fingerprint liveness database which consists of four
sub-sets, which contain live and fake fingerprint images from four capture
devices. Images have been collected by a consensual approach and using
different materials for the artificial reproduction of the fingerprint
(gelatine, silicone, play-doh, ecoflex, body double, wood glue).


Data Set
--------

=== ============ ================= =========== ============ ============== ==============
 #    Scanner          Model        Res (dpi)   Image size   Live samples   Fake samples
=== ============ ================= =========== ============ ============== ==============
 1   Biometrika   FX2000               569        312X372        2000           2000
 2   Italdata     ET10                 500        640X480        2000           2000
 3   Crossmatch   L SCAN GUARDIAN      500        640X480        2500           2000
 4   Swipe                             96                        2374           1979
=== ============ ================= =========== ============ ============== ==============


The actual raw data for the database should be downloaded from the original
URL. This package only contains the `Bob <http://www.idiap.ch/software/bob/>`_
accessor methods to use the DB directly from python, with our certified
protocols.


References
----------

.. [Ghiani2013] L. Ghiani, D. Yambay, V. Mura, S. Tocco, G.L. Marcialis, F. Roli, and S.  Schuckers, LivDet 2013 -  Fingerprint Liveness Detection Competition 2013, 6th IAPR/IEEE Int. Conf. on Biometrics, June, 4-7, 2013, Madrid (Spain).
