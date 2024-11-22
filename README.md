# CKAN API Client

This repository contains a Python client class to interact with the [CKAN API](https://docs.ckan.org/en/latest/api/index.html) for the Italian OpenData portal ([dati.gov.it](https://www.dati.gov.it/opendata/)). The class provides an easy way to query datasets, retrieve metadata, and access catalog information.

---

## Features

- **Retrieve all datasets**: List all available datasets from the catalog.
- **Fetch dataset metadata**: Get detailed metadata for a specific dataset.
- **List datasets with resources**: Retrieve datasets and their associated resources with pagination support.
- **List organizations**: Get a list of all organizations contributing to the catalog.
- **Fetch organization details**: Retrieve detailed information about a specific organization.
- **Search datasets by holder name**: Query datasets based on the administrative holder.

---

## Requirements

- Python 3.7 or later
- `requests` library (install via `pip install requests`)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ckan-api-client.git
   cd ckan-api-client

2. Install dependencies:
   ```bash
    pip install -r requirements.txt

---

## API Methods

   ```bash
    from ckan_client import CKANClient

    client = CKANClient()

    # Retrieve the list of all datasets
    datasets = client.package_list()
    print(f"Available datasets: {datasets}")

    # Fetch details of the first dataset in the list
    if datasets:
        dataset_details = client.package_show(datasets[0])
        print(f"Details for dataset '{datasets[0]}': {dataset_details}")

    # Get a list of datasets with resources (limit 10)
    datasets_with_resources = client.current_package_list_with_resources(limit=10)
    print(f"Datasets with resources: {datasets_with_resources}")

    # List all organizations
    organizations = client.organization_list()
    print(f"Organizations: {organizations}")

    # Fetch details of the first organization in the list
    if organizations:
        org_details = client.organization_show(organizations[0])
        print(f"Details for organization '{organizations[0]}': {org_details}")

    # Search datasets by holder name (example: "ACI")
    search_results = client.package_search_by_holder_name("ACI")
    print(f"Search results for holder 'ACI': {search_results}")
