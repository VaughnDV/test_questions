from unittest import TestCase

def increment_dictionary_values(d, i):
    e = d.copy()  # Prevent changes the dictionary passed
    for k, v in e.items():
        e[k] = v + i
    return e
    
class TestIncrementDictionaryValues(TestCase):
    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)
