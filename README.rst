Tank
====

An educationnal python program

Install
~~~~~~~

Activate your preferred virtualenv and clone Tank::

  $ hg clone http://bitbucket.org/alexbrun/tank

Then install it in development mode::

  $ python setup.py develop

If you want to develop on it you should also install the dev tools::

  $ pip install nose
  $ pip install coverage

Testing your new implemention
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When implementing something new (or just after hacking in the source code) you
shoudld always implement your proper tests

The second thing you should always do is run the test suite to make sure
nothing is broken::

  $ nosetests -v --with-coverage --cover-html --cover-package=tank

This will give you a nice html output about what parts of the code are covered
or not.
