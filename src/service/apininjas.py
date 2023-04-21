import requests


class APINinjasService:
    def __init__(self, api_key: str):
        self.api_key: str = api_key

    def get_facts(self, limit: int = 1) -> list[str]:
        print('INFO: Getting facts')
        headers = {"X-Api-Key": self.api_key}
        response = requests.get(url=f'https://api.api-ninjas.com/v1/facts?limit={str(limit)}',
                                headers=headers)
        if response.ok:
            print(f'SUCCESS: Got facts with status_code={response.status_code}')
            facts: list[str] = []
            for entry in response.json():
                facts.append(entry["fact"])
            return facts
        else:
            print(f'FAILURE: Failed to get facts with status_code={response.status_code}')
            return None
