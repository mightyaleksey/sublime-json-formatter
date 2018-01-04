import sys
import unittest

import sublime_lib_mock
import sublime_plugin_lib_mock
sys.modules['sublime'] = sublime_lib_mock
sys.modules['sublime_plugin'] = sublime_plugin_lib_mock

from JsonFormatter import parse_json, serialize_json

class UtilsTests(unittest.TestCase):
  def test_cyrillic_parsing(self):
    structure = parse_json('{"cyrillic":"Дизайн системы"}')
    self.assertEqual(structure, {'cyrillic': 'Дизайн системы'})

  def test_cyrillic_stringifying(self):
    string = serialize_json({'cyrillic': 'Дизайн системы'})
    self.assertEqual(string, '{"cyrillic":"Дизайн системы"}')

  def test_null_value_parsing(self):
    structure = parse_json('{"null":null}')
    self.assertEqual(structure, {'null': None})

  def test_null_value_stringifying(self):
    string = serialize_json({'null': None})
    self.assertEqual(string, '{"null":null}')

if __name__ == '__main__':
  UtilsTests.main()
