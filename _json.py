#ndjson to json
import json

def convert_ndjson_to_json(input_file, output_file):
    with open(input_file, 'r') as ndjson_file:
        data = [json.loads(line) for line in ndjson_file]

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == '__main__':
    input_filename = 'jqtest.json'  # The NDJSON file you provided
    output_filename = 'output.json'  # The desired output JSON file

    convert_ndjson_to_json(input_filename, output_filename)
    print(f"Converted {input_filename} to {output_filename}")