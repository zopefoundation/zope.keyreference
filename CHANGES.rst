=======
CHANGES
=======

4.0.0 (unreleased)
--------------------

- Added support for testing on Travis.


4.0.0a2 (2013-02-25)
--------------------

- Make sure that the ``SimpleKeyReference`` implementation (used for testing)
  also implements rich comparison properly.


4.0.0a1 (2013-02-22)
--------------------

- Added support for Python 3.3.

- Replaced deprecated ``zope.component.adapts`` usage with equivalent
  ``zope.component.adapter`` decorator.

- Replaced deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropped support for Python 2.4 and 2.5.


3.6.4 (2011-11-30)
------------------

- Fix tests broken by removal of ``zope.testing`` from test dependencies:
  avoid the ``ZODB3`` module that needs it.

3.6.3 (2011-11-29)
------------------

- Prefer the standard libraries doctest module to the one from ``zope.testing``.

3.6.2 (2009-09-15)
------------------

- Made the tests pass with ZODB3.9, which changed the repr() of the persistent
  classes.

3.6.1 (2009-02-01)
------------------

- Load keyreferences, pickled by old zope.app.keyreference even
  if its not installed anymore (so don't break if one updates a
  project that don't directly depends on zope.app.keyreference).

3.6.0 (2009-01-31)
------------------

- Rename ``zope.app.keyreference`` to ``zope.keyreference``.