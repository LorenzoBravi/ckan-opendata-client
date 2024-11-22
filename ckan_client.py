import requests

class CKANClient:
    BASE_URL = "https://www.dati.gov.it/opendata/api/3/action"

    def __init__(self):
        self.session = requests.Session()

    def package_list(self):
        """Ottiene la lista di tutti i dataset."""
        endpoint = f"{self.BASE_URL}/package_list"
        response = self.session.get(endpoint)
        response.raise_for_status()
        return response.json().get('result', [])

    def package_show(self, dataset_id):
        """Ottiene i metadati di un dataset specifico."""
        endpoint = f"{self.BASE_URL}/package_show"
        params = {"id": dataset_id}
        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        return response.json().get('result', {})

    def current_package_list_with_resources(self, limit, offset=0):
        """Ottiene una lista di dataset con risorse."""
        endpoint = f"{self.BASE_URL}/current_package_list_with_resources"
        params = {"limit": limit, "offset": offset}
        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        return response.json().get('result', [])

    def organization_list(self):
        """Ottiene la lista delle organizzazioni."""
        endpoint = f"{self.BASE_URL}/organization_list"
        response = self.session.get(endpoint)
        response.raise_for_status()
        return response.json().get('result', [])

    def organization_show(self, org_id):
        """Ottiene i dettagli di una specifica organizzazione."""
        endpoint = f"{self.BASE_URL}/organization_show"
        params = {"id": org_id}
        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        return response.json().get('result', {})

    def package_search_by_holder_name(self, holder_name, facet_limit=-1):
        """Cerca i dataset associati a una specifica amministrazione."""
        endpoint = f"{self.BASE_URL}/package_search"
        params = {
            "facet.field": '["holder_name"]',
            "facet.limit": facet_limit,
            "fq": f'holder_name:"{holder_name}"'
        }
        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        return response.json().get('result', {})