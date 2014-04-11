=========================================
Livdet 2013 Fingerprint Liveness Database
=========================================

The Livdet 2013 Fingerprint Liveness Database is a fingerprint liveness database which consists of four sub-sets, which contain live and fake fingerprint images from four capture devices. Images have been collected by a consensual approach and using different materials for the artificial reproduction of the fingerprint (gelatine, silicone, play-doh, ecoflex, body double, wood glue).

DATA SET
 	Scanner 	Model 	        Res (dpi) 	Image size 	Live samples 	Fake samples
1 	Biometrika 	FX2000       	569 	    312X372 	2000 	        2000
2 	Italdata 	ET10 	        500 	    640X480 	2000 	        2000
3 	Crossmatch 	L SCAN GUARDIAN 500 	    640X480 	2500 	        2000
4 	Swipe 		                96 		                2374 	        1979


The actual raw data for the database should be downloaded from the original
URL. This package only contains the `Bob <http://www.idiap.ch/software/bob/>`_
accessor methods to use the DB directly from python, with our certified
protocols.

References::

1. L. Ghiani, D. Yambay, V. Mura, S. Tocco, G.L. Marcialis, F. Roli, and S. Schuckers, LivDet 2013 -  Fingerprint Liveness Detection Competition 2013, 6th IAPR/IEEE Int. Conf. on Biometrics, June, 4-7, 2013, Madrid (Spain).

You would normally not install this package unless you are maintaining it. What
you would do instead is to tie it in at the package you need to **use** it.
There are a few ways to achieve this:

1. You can add this package as a requirement at the ``setup.py`` for your own
   `satellite package
   <https://github.com/idiap/bob/wiki/Virtual-Work-Environments-with-Buildout>`_
   or to your Buildout ``.cfg`` file, if you prefer it that way. With this
   method, this package gets automatically downloaded and installed on your
   working environment, or

2. You can manually download and install this package using commands like
   ``easy_install`` or ``pip``.

The package is available in two different distribution formats:

1. You can download it from `PyPI <http://pypi.python.org/pypi>`_, or

2. You can download it in its source form from `its git repository
   <https://github.com/bioidiap/xbob.db.nuaa>`_. When you download the
   version at the git repository, you will need to run a command to recreate
   the backend SQLite file required for its operation. This means that the
   database raw files must be installed somewhere in this case. With option
   ``a`` you can run in `dummy` mode and only download the raw data files for
   the database once you are happy with your setup.

You can mix and match points 1/2 and a/b above based on your requirements. Here
are some examples:

Modify your setup.py and download from PyPI
===========================================

That is the easiest. Edit your ``setup.py`` in your satellite package and add
the following entry in the ``install_requires`` section (note: ``...`` means
`whatever extra stuff you may have in-between`, don't put that on your
script)::

    install_requires=[
      ...
      "xbob.db.nuaa",
    ],

Proceed normally with your ``boostrap/buildout`` steps and you should be all
set. That means you can now import the namespace ``xbob.db.nuaa`` into your scripts.

Modify your buildout.cfg and download from git
==============================================

You will need to add a dependence to `mr.developer
<http://pypi.python.org/pypi/mr.developer/>`_ to be able to install from our
git repositories. Your ``buildout.cfg`` file should contain the following
lines::

  [buildout]
  ...
  extensions = mr.developer
  auto-checkout = *
  eggs = bob
         ...
         xbob.db.nuaa

  [sources]
  xbob.db.nuaa = git https://github.com/bioidiap/xbob.db.nuaa.git
  ...
