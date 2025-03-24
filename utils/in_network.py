import ijson
import json
from decimal import Decimal

input_file = '2025-03-05_pl-2in-hr23_Aetna-Health-Inc.---Georgia.json'
output_file = 'in_network.json'

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


with open(input_file, 'rb') as f_in, open(output_file, 'w') as f_out:
    f_out.write('[\n')
    parser = ijson.items(f_in, 'in_network.item')

    first = True
    for item in parser:
        if not first:
            f_out.write(',\n')
        f_out.write(json.dumps(item, default=decimal_default))
        first = False

    f_out.write('\n]')
