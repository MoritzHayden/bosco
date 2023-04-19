import requests

# Call the fun fact API and return a list of facts
def get_fun_facts(api_key: str, limit: int = 1):
    print('INFO: Calling Fun fact API')
    headers = {"X-Api-Key": api_key}
    response = requests.get(f'https://api.api-ninjas.com/v1/facts?limit={str(limit)}', headers=headers)
    facts = []
    if response.ok:
        for fact in response.json():
            facts.append(fact["fact"])
        print(f'SUCCESS: Fun fact API request succeeded with status_code={response.status_code}')
    else:
        print(f'FAILURE: Fun fact API request failed with status_code={response.status_code}')
    return facts
