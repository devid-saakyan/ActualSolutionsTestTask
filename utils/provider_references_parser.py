import ijson
import json

input_file = "../2025-03-05_pl-2in-hr23_Aetna-Health-Inc.---Georgia.json"
output_file = "provider_references.json"

with open(input_file, 'rb') as f, open(output_file, 'w', encoding='utf-8') as out:
    out.write("[\n")
    items = ijson.items(f, 'provider_references.item')
    first = True
    for item in items:
        if not first:
            out.write(",\n")
        else:
            first = False
        json.dump(item, out)

    out.write("\n]")
