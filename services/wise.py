import requests

from fastapi import HTTPException
from decouple import config


class WiseService:
    def __init__(self):
        self.main_url = "..."
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config('WISE_TOKEN')}",
        }
        self.profile_id = self._get_profile_id()

    def _get_profile_id(self):
        url = self.main_url + "/v1/profiles"
        resp = requests.get(url, headers=self.headers)

        if resp.status_code == 200:
            resp = resp.json()
            return [a["id"] for a in resp if a["type"] == "personal"][0]
        else:
            print(resp)
            raise HTTPException(
                status_code=500,
                detail="Payment provider is not available at the moment",
            )
