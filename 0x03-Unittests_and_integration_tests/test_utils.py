#!/usr/bin/env python3
"""
Implementing unittest and also parameterized it
"""
import unittest
from typing import Dict, Tuple, Union
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
            nested_map: Dict,
            path: Tuple,
            expect: Union[Dict, int]
    ):
        """test access_nested_map function returns"""
        self.assertEqual(access_nested_map(nested_map, path), expect)
