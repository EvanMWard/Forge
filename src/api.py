import requests


class XIVAPI:
    BASE = "https://v2.xivapi.com/api"

    def search(
        self,
        # version=one,
        query,
        sheets,
        # cursor,
        # limit,
        # schema,
        fields=None,
        # transient,
        language="en",
    ):
        search_url = self.BASE + "/search"
        fields = ",".join(fields) if fields else None
        return requests.get(
            search_url,
            params={
                "query": query,
                "sheets": sheets,
                "fields": fields if fields else [],
            },
        ).json()

    def search_next(self, next, fields):
        params = {"cursor": next, "fields": fields}
        search_url = self.BASE + "/search"
        return requests.get(search_url, params=params).json()

    def sheet(self, fields=None, sheet="Item"):
        url = self.BASE + f"/sheet/{sheet}"
        params = {}
        if fields:
            params["fields"] = ",".join(fields)
        print()
        return requests.get(url, params=params).json()
