import json
import sublime
import sublime_plugin

def get_regions(view):
  regions = tuple(filter(lambda r: not r.empty(), view.sel()))

  if len(regions) > 0:
    return regions

  return (sublime.Region(0, view.size()),)

def parse_json(json_string):
  try:
    return json.loads(json_string)
  except ValueError:
    return None

def serialize_json(structure, indent=None, item_separator=',', key_separator=':', sort_keys=False):
  return json.dumps(structure, ensure_ascii=False, indent=indent, separators=(item_separator, key_separator), sort_keys=False)

class MinifyJsonCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    regions = reversed(get_regions(self.view))

    for region in regions:
      json_string = self.view.substr(region)
      structure = parse_json(json_string)

      if not structure:
        self.view.window().status_message('Invalid json')
      else:
        minified_json_string = serialize_json(structure)
        self.view.replace(edit, region, minified_json_string)

class PrettifyJsonCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    regions = reversed(get_regions(self.view))

    for region in regions:
      json_string = self.view.substr(region)
      structure = parse_json(json_string)

      if not structure:
        self.view.window().status_message('Invalid json')
      else:
        minified_json_string = serialize_json(structure, indent=2, item_separator=', ', key_separator=': ')
        self.view.replace(edit, region, minified_json_string)

class PrettifyJsonAndSortKeysCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    regions = reversed(get_regions(self.view))

    for region in regions:
      json_string = self.view.substr(region)
      structure = parse_json(json_string)

      if not structure:
        self.view.window().status_message('Invalid json')
      else:
        minified_json_string = serialize_json(structure, indent=2, item_separator=', ', key_separator=': ', sort_keys=True)
        self.view.replace(edit, region, minified_json_string)
