import ijson
import json

CHUNK_SIZE = 1000
chunk_id = 0
chunk = []

with open("in_network.json", "r") as f:
    objects = ijson.items(f, "item")
    for idx, item in enumerate(objects, 1):
        chunk.append(item)
        if idx % CHUNK_SIZE == 0:
            with open(f"chunks/in_network_chunk_{chunk_id}.json", "w") as out:
                json.dump(chunk, out, default=str)
            chunk = []
            chunk_id += 1

    if chunk:
        with open(f"chunks/in_network_chunk_{chunk_id}.json", "w") as out:
            json.dump(chunk, out, default=str)