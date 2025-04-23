import requests


class XIVAPI:
    BASE = "https://v2.xivapi.com/api"

    def search(self, query, sheets, fields=None, language="en"):
        search_url = self.BASE + "/search"
        fields = ",".join(fields) if fields else None
        params = {
            "query": query,
            "sheets": sheets,
        }
        if fields:
            params["fields"] = fields
        return requests.get(
            search_url,
            params=params,
        ).json()

    def search_next(self, next, fields):
        fields = ",".join(fields) if fields else None
        params = {"cursor": next}
        if fields:
            params["fields"] = fields
        search_url = self.BASE + "/search"
        return requests.get(search_url, params=params).json()

    def sheet(self, fields=None, sheet="Item"):
        url = self.BASE + f"/sheet/{sheet}"
        params = {}
        if fields:
            params["fields"] = ",".join(fields)
        return requests.get(url, params=params).json()


def fetch_item():
    fields = ["Name", "BaseParam", "BaseParamValue"]
    client = XIVAPI()
    query = 'Name~"of Crafting"'
    gathering_items = []
    search = client.search(query=query, sheets=["Item"], fields=fields)
    gathering_items.extend(create_data_dict(search, fields))
    next = search["next"]
    while next:
        search = client.search_next(next=next, fields=fields)
        next = search["next"] if "next" in search.keys() else None
        gathering_items.extend(create_data_dict(search, fields))
    with open("gathering.txt", "w+") as f:
        f.write(str(gathering_items))


def create_data_dict(search, fields):
    arr = []
    for entry in search["results"]:
        data = {
            "row_id": entry["row_id"],
        }
        data.update({field: entry["fields"][field] for field in fields})
        data["BaseParam"] = [
            param["fields"]["Name"]
            for param in data["BaseParam"]
            if param["fields"]["Name"]
        ]
        arr.append(data)
    return arr


fetch_item()
