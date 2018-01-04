import json

def parse_json(json_string):
  try:
    return json.loads(json_string)
  except ValueError:
    return None

def serialize_json(structure, indent=None, item_separator=',', key_separator=':', sort_keys=False):
  return json.dumps(structure, ensure_ascii=False, indent=indent, separators=(item_separator, key_separator), sort_keys=False)
