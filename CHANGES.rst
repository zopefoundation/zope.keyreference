=========
 Changes
=========

5.0.0 (2022-03-25)
==================

- Remove ``__cmp__`` methods. Since the implementation of the rich
  comparison methods (``__eq__``, etc) in 4.0a1, the interpreter won't
  call ``__cmp__``, even on Python 2. See `issue 10
  <https://github.com/zopefoundation/zope.keyreference/issues/10>`_.

- Add support for Python 3.8, 3.9, and 3.10.

- Drop support for Python 3.4.


4.2.0 (2018-10-26)
==================

- Add support for Python 3.5, 3.6, and 3.7.

- Drop support for Python 2.6 and 3.3.


4.1.0 (2014-12-27)
==================

- Add support for PyPy (PyPy3 blocked on PyPy3-compatible ``zodbpickle``).

- Add support for Python 3.4.


4.0.0 (2014-12-20)
==================

- Add support for testing on Travis.


4.0.0a2 (2013-02-25)
====================

- Ensure that the ``SimpleKeyReference`` implementation (used for testing)
  also implements rich comparison properly.


4.0.0a1 (2013-02-22)
====================

- Add support for Python 3.3.

- Replace deprecated ``zope.component.adapts`` usage with equivalent
  ``zope.component.adapter`` decorator.

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.


3.6.4 (2011-11-30)
==================

- Fix tests broken by removal of ``zope.testing`` from test dependencies:
  avoid the ``ZODB3`` module that needs it.

3.6.3 (2011-11-29)
==================

- Prefer the standard libraries doctest module to the one from ``zope.testing``.

3.6.2 (2009-09-15)
==================

- Make the tests pass with ZODB3.9, which changed the repr() of the persistent
  classes.

3.6.1 (2009-02-01)
==================

- Load keyreferences, pickled by old zope.app.keyreference even
  if its not installed anymore (so don't break if one updates a
  project that don't directly depends on zope.app.keyreference).

3.6.0 (2009-01-31)
==================

- Rename ``zope.app.keyreference`` to ``zope.keyreference``.
