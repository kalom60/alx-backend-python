#!/usr/bin/env python3
"""
Implementing Unittest for client module
"""
import unittest
from unittest.mock import patch
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

    def test_public_repos_url(self):
        """test _public_repos_url method"""
        with patch('client.GithubOrgClient.org') as web:
            web_res = {"repos_url": "https://api.github\
                    .com/orgs/abc/repos"}
            GithubOrgClient._public_repos_url

    @patch('utils.get_json')
    def test_public_repos(self, patched_json):
        """test public_repos method"""
        patched_json_res = {"name": "episodes.dart"}
        with patch('client.GithubOrgClient._public_repos_url') as repos:
            repos.return_value = ["episodes.dart"]
            GithubOrgClient.public_repos


if __name__ == "__main__":
    unittest.main()
