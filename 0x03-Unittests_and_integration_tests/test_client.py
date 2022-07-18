#!/usr/bin/env python3
"""
Implementing Unittest for client module
"""
import unittest
from typing import Dict
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """test GithubOrgClient class"""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, return_val: Dict, patched_json) -> None:
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
    def test_has_license(self, repo, license, res):
        """a function that test the has_license method"""
        self.assertEqual(GithubOrgClient.has_license(repo, license), res)

       
@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the GithubOrgClient class"""
    @classmethod
    def setUpClass(cls):
        """Sets up class fixtures"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """tests the public_repos method"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self):
        """tests the public_repos method with a license"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls):
        """Removes the class fixtures"""
        cls.get_patcher.stop()       


if __name__ == "__main__":
    unittest.main()
