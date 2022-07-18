#!/usr/bin/env python3
"""Unittest client module"""
import unittest
from unittest.mock import patch
from typing import Dict
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test GithubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("utils.get_json")
    def test_org(self, web: str, patched_json):
        """test the org method"""
        url = GithubOrgClient(web)
        url.org


if __name__ == "__main__":
    unittest.main()
