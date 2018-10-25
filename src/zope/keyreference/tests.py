##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Tests for the unique id utility.
"""
import doctest
import re
import unittest
from zope.testing import renormalizing


class MockDatabase(object):
    database_name = ''


class MockJar(object):

    def __init__(self):
        self._db = MockDatabase()

    def db(self):
        return self._db


class MockPersistent(object):
    _p_oid = 1
    _p_jar = MockJar()

    def __hash__(self):
        # SimpleKeyReference depends on hash
        return hash(self._p_oid)


class TestKeyReferenceToPersistent(unittest.TestCase):

    def makeOne(self, obj):
        from zope.keyreference.persistent import KeyReferenceToPersistent
        return KeyReferenceToPersistent(obj)

    def test__cmp__(self):

        persistent = MockPersistent()

        eq1 = self.makeOne(persistent)
        eq2 = self.makeOne(persistent)

        self.assertEqual(eq1, eq2)
        self.assertEqual(0, eq1.__cmp__(eq2))
        self.assertEqual(0, eq1.__cmp__(eq1))
        self.assertEqual(0, eq2.__cmp__(eq1))

        # But if they have different key_type_id, they
        # only compare based on that.
        eq2.key_type_id = 'aaa'
        self.assertNotEqual(eq1, eq2)

        persistent_gt = MockPersistent()
        persistent_gt._p_oid = 2

        gt = self.makeOne(persistent_gt)
        __traceback_info__ = hash(gt), hash(eq1), hash(persistent._p_oid)
        self.assertGreater(gt, eq1)
        self.assertGreaterEqual(gt, eq1)
        self.assertNotEqual(gt, eq1)
        self.assertEqual(1, gt.__cmp__(eq1))

        self.assertLess(eq1, gt)
        self.assertLessEqual(eq1, gt)
        self.assertEqual(-1, eq1.__cmp__(gt))


    def test__call__(self):
        persistent = MockPersistent()
        obj = self.makeOne(persistent)

        self.assertIs(persistent, obj())

class TestSimpleKeyReference(TestKeyReferenceToPersistent):

    def makeOne(self, obj):
        from zope.keyreference.testing import SimpleKeyReference
        return SimpleKeyReference(obj)


checker = renormalizing.RENormalizing([
    # Python 3 adds module name to exceptions.
    (re.compile("zope.keyreference.interfaces.NotYet"),
     r"NotYet"),
    ])


def test_multi_databases():
    """
    >>> from ZODB.MappingStorage import DB
    >>> import transaction
    >>> from BTrees.OOBTree import OOBucket

    >>> databases = {}

    >>> db1 = DB(databases=databases, database_name='1')
    >>> db2 = DB(databases=databases, database_name='2')

    >>> conn1 = db1.open()
    >>> conn1.root()['ob'] = OOBucket()

    >>> conn2 = conn1.get_connection('2')
    >>> conn2.root()['ob'] = OOBucket()

    >>> conn1.root()['ob']._p_oid == conn2.root()['ob']._p_oid
    True

    >>> transaction.commit()

    >>> from zope.keyreference.persistent import KeyReferenceToPersistent

    >>> key1 = KeyReferenceToPersistent(conn1.root()['ob'])
    >>> key2 = KeyReferenceToPersistent(conn2.root()['ob'])

    >>> key1 != key2, key2 > key1, hash(key1) != hash(key2)
    (True, True, True)

"""

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite('persistent.txt', checker=checker),
        doctest.DocTestSuite(),
        unittest.defaultTestLoader.loadTestsFromName(__name__),
    ))
