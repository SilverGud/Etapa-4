from collections import MutableMapping, OrderedDict
import unittest


_allClasses = {}


class HierarchyException(Exception):
    pass


def lookupClass(name):
    return _allClasses[name]


class Method():
    """
    Se usa una tabla de símbolos lineal para
    almacenar los tipos de los parámetros.
    """

    def __init__(self, type, params=None):
        self.type = type
        self.params = SymbolTable()
        if params:
            for x, y in params:
                self.params[x] = y


class Klass():

    def __init__(self, name, inherits="Object"):
        self.name = name
        self.inherits = inherits
        if self.name != "Object":
            self.validHierarchy()

        self.attributes = SymbolTable()
        self.methods = SymbolTable()
        _allClasses[name] = self

    def validHierarchy(self):
        up = self.inherits
        while up != "Object":
            if up == self.name:
                raise HierarchyException
            up = _allClasses[up].inherits

    def addAttribute(self, name, type):
        try:
            self.lookupAttribute(name)
            raise KeyError(name)
        except KeyError:
            self.attributes[name] = type

    def addMethod(self, name, method):
        self.methods[name] = method

    def lookupAttribute(self, name):
        if name in self.attributes:
            return self.attributes[name]
        elif self.name == "Object":
            raise KeyError(name)
        else:
            return _allClasses[self.inherits].lookupAttribute(name)

    def lookupMethod(self, name):
        if name in self.methods:
            return self.methods[name]
        elif self.name == "Object":
            raise KeyError(name)
        else:
            return _allClasses[self.inherits].lookupMethod(name)

    def conforms(self, B):
        if B.name == 'Object':
            return False
        if B.name == self.name:
            return True
        else:
            return self.conforms(lookupClass(B.inherits))


class SymbolTable(MutableMapping):
    def __init__(self):
        self.dict = OrderedDict()

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        if key in self.dict:
            raise KeyError(key)
        self.dict[key] = value

    def __delitem__(self, key):
        del self.dict[key]

    def __iter__(self):
        return iter(self.dict)

    def __len__(self):
        return len(self.dict)

    def __repr__(self):
        return self.dict.__repr__()


class SymbolTableWithScopes(MutableMapping):
    def __init__(self, klass):
        self.dict_list = [{}]
        self.last = 0
        self.klass = klass

    def __getitem__(self, key):
        for i in reversed(range(self.last+1)):
            if key in self.dict_list[i].keys():
                return self.dict_list[i][key]
        return self.klass.lookupAttribute(key)
        raise KeyError(key)

    def __setitem__(self, key, value):
        if key in self.dict_list[self.last]:
            raise KeyError(key)
        self.dict_list[self.last][key] = value

    def __delitem__(self, key):
        del self.dict_list[self.last][key]

    def __iter__(self):
        return iter(self.dict_list[self.last])

    def __len__(self):
        return len(self.dict_list[self.last])

    def closeScope(self):
        self.dict_list.pop()
        self.last = self.last - 1

    def openScope(self):
        self.dict_list.append({})
        self.last = self.last + 1

    def __repr__(self):
        return self.dict_list.__repr__()


class PruebasDeEstructura(unittest.TestCase):
    def setUp(self):
        self.k = [Klass("A"), Klass("B", "A"),
                  Klass("C", "B"), Klass("Z", "B")]

    def test1(self):
        self.k[0].addAttribute("a", "Integer")
        self.assertTrue(self.k[0].lookupAttribute("a") == "Integer")

    def test2(self):
        self.k[0].addAttribute("a", "Integer")
        self.assertTrue(self.k[1].lookupAttribute("a") == "Integer")
        self.assertTrue(self.k[2].lookupAttribute("a") == "Integer")
        self.k[1].addAttribute("b", "String")
        self.assertTrue(self.k[2].lookupAttribute("b") == "String")

    def test3(self):
        with self.assertRaises(KeyError):
            self.k[3].lookupAttribute("z")

    def test4(self):
        m1 = Method("Integer")
        m2 = Method("String", [("a", "Integer"), ("b", "Boolean")])
        self.k[0].addMethod("test", m1)
        self.k[1].addMethod("test2", m2)
        self.assertTrue(self.k[0].lookupMethod("test") == m1)
        self.assertTrue(self.k[2].lookupMethod("test") == m1)
        self.assertTrue(self.k[1].lookupMethod("test2") == m2)

    def test5(self):
        with self.assertRaises(HierarchyException):
            z = Klass("A", "C")

    def test6(self):
        self.assertTrue(lookupClass("A") == self.k[0])

    def test7(self):
        self.assertTrue(self.k[0].conforms(self.k[2]))
        self.assertFalse(self.k[2].conforms(self.k[1]))


class PruebasConTablaLineal(unittest.TestCase):
    def setUp(self):
        self.st = SymbolTable()

    def tearDown(self):
        self.st = None

    def test1(self):
        self.assertFalse('a' in self.st.keys())

    def test2(self):
        self.st['hola'] = 'mundo1'
        self.assertTrue('hola' in self.st.keys())
        self.assertTrue(self.st['hola'] == 'mundo1')

    def test3(self):
        with self.assertRaises(KeyError):
            self.st['hola']

    def test4(self):
        self.st['hola'] = 'mundo'
        with self.assertRaises(KeyError):
            self.st['hola'] = 'mundo'


class PruebasConScopes(unittest.TestCase):
    def setUp(self):
        k = Klass("Object", None)
        self.st = SymbolTableWithScopes(k)

    def tearDown(self):
        self.st = None

    def test1(self):
        self.assertFalse('a' in self.st.keys())

    def test2(self):
        self.st['hola'] = 'mundo1'
        self.assertTrue('hola' in self.st.keys())
        self.assertTrue(self.st['hola'] == 'mundo1')

    def test3(self):
        self.st['hola'] = 'mundo2'
        self.assertTrue('mundo2' in self.st.values())

    def test4(self):
        self.st['hola'] = 'mundo3'
        self.assertEquals('mundo3', self.st['hola'])

    def test5(self):
        with self.assertRaises(KeyError):
            self.st['hola']

    def test6(self):
        self.st.openScope()
        self.st['hola'] = 'mundo1'
        self.st.closeScope()
        self.assertFalse('hola' in self.st)

    def test7(self):
        self.st['hola'] = 'scope0'
        self.st.openScope()
        self.st['hola'] = 'scope1'
        self.st.openScope()
        self.st['hola'] = 'scope2'
        self.assertEquals(self.st['hola'], 'scope2')
        self.st.closeScope()
        self.assertEquals(self.st['hola'], 'scope1')
        self.st.closeScope()
        self.assertEquals(self.st['hola'], 'scope0')


def setBaseClasses():
    k = Klass('Object')
    k.addMethod('abort', Method('Object'))
    k.addMethod('type_name', Method('Object'))
    k.addMethod('copy', Method('SELF_TYPE'))
    _allClasses['Object'] = k
    k = Klass('IO')
    k.addMethod('out_string', Method('SELF_TYPE', [('x', 'String')]))
    k.addMethod('out_int', Method('SELF_TYPE', [('x', 'Int')]))
    k.addMethod('in_string', Method('String'))
    k.addMethod('in_int', Method('Int'))
    _allClasses['IO'] = k
    k = Klass('Int')
    _allClasses['Int'] = k
    k = Klass('String')
    k.addMethod('length', Method('Int'))
    k.addMethod('concat', Method('String', [('s', 'String')]))
    k.addMethod('substr', Method('String', [('i', 'Int'), ('l', 'Int')]))
    _allClasses['String'] = k
    k = Klass('Bool')
    _allClasses['Bool'] = k


if __name__ == '__main__':
    unittest.main(verbosity=2)
