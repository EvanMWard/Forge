from api import XIVAPI


def fetch_item():
    client = XIVAPI()
    query = 'Name~"of Gathering"'
    gathering_items = []
    search = client.search(query=query, sheets=["Item"], fields=["Name"])
    print(search)
    gathering_items.extend(
        [
            {"row_id": entry["row_id"], "name": entry["fields"]["Name"]}
            for entry in search["results"]
        ]
    )
    next = search["next"]
    while next:
        search = client.search_next(next=next, fields=["Name"])
        next = search["next"] if "next" in search.keys() else None
        gathering_items.extend(
            [
                {"row_id": entry["row_id"], "name": entry["fields"]["Name"]}
                for entry in search["results"]
            ]
        )
    with open("gathering.txt", "w+") as f:
        f.write(str(gathering_items))
    print(len(gathering_items))
