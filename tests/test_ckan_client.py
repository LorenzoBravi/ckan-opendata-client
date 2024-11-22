import unittest
from unittest.mock import patch, Mock
from src.ckan_client import CKANClient

class TestCKANClient(unittest.TestCase):
    def setUp(self):
        """Set up the CKANClient for tests."""
        self.client = CKANClient()

    @patch("requests.Session.get")
    def test_package_list_success(self, mock_get):
        """Test successful retrieval of the package list."""
        mock_response = Mock()
        mock_response.json.return_value = {"success": True, "result": ["dataset1", "dataset2"]}
        mock_get.return_value = mock_response

        result = self.client.package_list()
        self.assertEqual(result, ["dataset1", "dataset2"])

    @patch("requests.Session.get")
    def test_package_list_failure(self, mock_get):
        """Test failure case for the package list."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("HTTP Error")
        mock_get.return_value = mock_response

        with self.assertRaises(RuntimeError):
            self.client.package_list()

    @patch("requests.Session.get")
    def test_package_show_success(self, mock_get):
        """Test successful retrieval of package details."""
        mock_response = Mock()
        mock_response.json.return_value = {"success": True, "result": {"id": "dataset1", "name": "Dataset 1"}}
        mock_get.return_value = mock_response

        result = self.client.package_show("dataset1")
        self.assertEqual(result, {"id": "dataset1", "name": "Dataset 1"})

    @patch("requests.Session.get")
    def test_package_show_invalid_id(self, mock_get):
        """Test retrieval with an invalid dataset ID."""
        mock_response = Mock()
        mock_response.json.return_value = {"success": False, "error": {"message": "Dataset not found"}}
        mock_get.return_value = mock_response

        with self.assertRaises(RuntimeError) as context:
            self.client.package_show("invalid-id")
        self.assertIn("Dataset not found", str(context.exception))

    @patch("requests.Session.get")
    def test_current_package_list_with_resources(self, mock_get):
        """Test retrieval of datasets with resources."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "success": True,
            "result": [{"id": "dataset1", "resources": []}, {"id": "dataset2", "resources": []}]
        }
        mock_get.return_value = mock_response

        result = self.client.current_package_list_with_resources(limit=10)
        self.assertEqual(len(result), 2)

    @patch("requests.Session.get")
    def test_organization_list(self, mock_get):
        """Test retrieval of organizations."""
        mock_response = Mock()
        mock_response.json.return_value = {"success": True, "result": ["org1", "org2"]}
        mock_get.return_value = mock_response

        result = self.client.organization_list()
        self.assertEqual(result, ["org1", "org2"])

    @patch("requests.Session.get")
    def test_organization_show(self, mock_get):
        """Test retrieval of organization details."""
        mock_response = Mock()
        mock_response.json.return_value = {"success": True, "result": {"id": "org1", "name": "Organization 1"}}
        mock_get.return_value = mock_response

        result = self.client.organization_show("org1")
        self.assertEqual(result, {"id": "org1", "name": "Organization 1"})

    @patch("requests.Session.get")
    def test_package_search_by_holder_name(self, mock_get):
        """Test searching datasets by holder name."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "success": True,
            "result": {"count": 1, "results": [{"id": "dataset1", "holder_name": "ACI"}]}
        }
        mock_get.return_value = mock_response

        result = self.client.package_search_by_holder_name("ACI")
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["results"][0]["holder_name"], "ACI")

if __name__ == "__main__":
    unittest.main()
