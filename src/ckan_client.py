import requests

class CKANClient:
    BASE_URL = "https://www.dati.gov.it/opendata/api/3/action"

    def __init__(self):
        self.session = requests.Session()

    def _handle_response(self, response):
        """
        Handles the HTTP response, raising custom errors for failed API calls.
        """
        try:
            response.raise_for_status()
        except requests.HTTPError as http_err:
            # Provide more detailed error messages
            error_message = f"HTTP Error: {http_err.response.status_code} - {http_err.response.reason}\nDetails: {http_err.response.text}"
            raise RuntimeError(error_message) from http_err
        except Exception as err:
            raise RuntimeError(f"An unexpected error occurred: {err}") from err

        # Check if the API returned an error
        json_response = response.json()
        if not json_response.get("success", False):
            error_message = json_response.get("error", {}).get("message", "Unknown API error occurred.")
            raise RuntimeError(f"API Error: {error_message}")

        return json_response.get("result", None)

    def package_list(self):
        """Fetches a list of all datasets."""
        endpoint = f"{self.BASE_URL}/package_list"
        response = self.session.get(endpoint)
        return self._handle_response(response)

    def package_show(self, dataset_id):
        """Fetches metadata for a specific dataset."""
        endpoint = f"{self.BASE_URL}/package_show"
        params = {"id": dataset_id}
        response = self.session.get(endpoint, params=params)
        return self._handle_response(response)

    def current_package_list_with_resources(self, limit, offset=0):
        """Fetches a list of datasets with their associated resources."""
        endpoint = f"{self.BASE_URL}/current_package_list_with_resources"
        params = {"limit": limit, "offset": offset}
        response = self.session.get(endpoint, params=params)
        return self._handle_response(response)

    def organization_list(self):
        """Fetches a list of all organizations."""
        endpoint = f"{self.BASE_URL}/organization_list"
        response = self.session.get(endpoint)
        return self._handle_response(response)

    def organization_show(self, org_id):
        """Fetches metadata for a specific organization."""
        endpoint = f"{self.BASE_URL}/organization_show"
        params = {"id": org_id}
        response = self.session.get(endpoint, params=params)
        return self._handle_response(response)

    def package_search_by_holder_name(self, holder_name, facet_limit=-1):
        """Searches for datasets by holder name."""
        endpoint = f"{self.BASE_URL}/package_search"
        params = {
            "facet.field": '["holder_name"]',
            "facet.limit": facet_limit,
            "fq": f'holder_name:"{holder_name}"'
        }
        response = self.session.get(endpoint, params=params)
        return self._handle_response(response)
