#!/usr/bin/env python3
"""
Implementing unittest and also parameterized it
"""
import unittest
from unittest.mock import patch
from typing import Mapping, Dict, Sequence, Any
from parameterized import parameterized


from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """tests access_nested_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expect: Any
    ):
        """test access_nested_map method returns"""
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
        """test access_nested_map method exception rasises"""
        self.assertRaises(expect, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """tests get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Dict):
        """tests get_json method return with mock"""
        with patch("utils.requests") as req:
            req.json = payload
            get_json(url)


if __name__ == "__main__":
    unittest.main()
