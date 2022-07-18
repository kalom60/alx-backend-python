#!/usr/bin/env python3
"""
Implementing Unittest for client module
"""
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """tests the public_repos method"""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [{"id": 7697149, "name": "episodes.dart"}]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                ["episodes.dart"],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
