import ijson
import json
import time

input_file = "../2025-03-05_pl-2in-hr23_Aetna-Health-Inc.---Georgia.json"
providers_file = "provider_references.json"
network_file = "in_network.json"

with open(input_file, 'rb') as f:
    parser = ijson.parse(f)
    print(parser)
    in_provider = False
    in_network = False

    providers = []
    network = []

    for prefix, event, value in parser:
        time.sleep(0.1)
        print(prefix, event, value)
        if prefix == 'provider_references' and event == 'start_array':
            in_provider = True
            current = []
        elif prefix == 'in_network' and event == 'start_array':
            in_network = True
            current = []

        elif (in_provider or in_network) and event == 'end_array':
            if in_provider:
                providers = current
                in_provider = False
            elif in_network:
                network = current
                in_network = False
            current = []

        elif (in_provider or in_network) and event == 'start_map':
            current_obj = {}
        elif (in_provider or in_network) and event == 'end_map':
            current.append(current_obj)
        elif (in_provider or in_network) and event in ('string', 'number', 'boolean', 'null'):
            key = prefix.split('.')[-1]
            current_obj[key] = value

with open(providers_file, "w", encoding="utf-8") as pf:
    json.dump(providers, pf, indent=2)

with open(network_file, "w", encoding="utf-8") as nf:
    json.dump(network, nf, indent=2)
