#!/usr/bin/env python3
"""
Implementing Unittest for client module
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test GithubOrgClient class"""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch("client.get_json")
    def test_org(self, org, return_val, patched_json):
        """ test the org method """
        patched_json.return_value = return_val
        url = GithubOrgClient(org)
        test = url.org
        self.assertEqual(test, patched_json.return_value)
        patched_json.assert_called_once()

    def test_public_repos_url(self):
        """test _public_repos_url method"""
        with patch('client.GithubOrgClient.org') as web:
            web_res = {"repos_url": "https://api.github\
                    .com/orgs/abc/repos"}
            GithubOrgClient._public_repos_url

    @patch("client.get_json")
    def test_public_repos(self, mock_patched_json):
        """tests the public_repos method"""
        mock_patched_json.return_value = [{"name": "episodes.dart"}]
        with patch.object(
                GithubOrgClient,
                "_public_repos_url",
                new_callable=PropertyMock,
                return_value="https://api.github.com/"
        ) as mock_repo:
            test_client = GithubOrgClient("episodes.dart")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["episodes.dart"])
            mock_patched_json.assert_called_once
            mock_repo.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expect):
        """tests has_license method"""
        test_client = GithubOrgClient("google")
        test_return = test_client.has_license(repo, license)
        self.assertEqual(expect, test_return)


if __name__ == "__main__":
    unittest.main()
