from src.ckan_client import CKANClient

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
