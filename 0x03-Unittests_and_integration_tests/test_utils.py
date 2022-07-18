#!/usr/bin/env python3
"""
Implementing unittest and also parameterized it
"""
import unittest
from typing import Mapping, Dict, Sequence, Union
from parameterized import parameterized


from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """tests access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expect: Union[Sequence, int]
    ):
        """test access_nested_map function returns"""
        self.assertEqual(access_nested_map(nested_map, path), expect)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            expect: Exception
    ):
        """test access_nested_map function exception rasises"""
        self.assertRaises(expect, access_nested_map(nested_map, path))


if __name__ == "__main__":
    unittest.main()