import json
import sublime
import sublime_plugin

class JsonFormatterUtils:
  @staticmethod
  def parse_json(string):
    return json.loads(string)

  @staticmethod
  def serialize_json(structure, indent=None, item_separator=',', key_separator=':', sort_keys=False):
    return json.dumps(structure, ensure_ascii=False, indent=indent, separators=(item_separator, key_separator), sort_keys=False)

  def parse_region(self, region):
    string = self.view.substr(region)

    try:
      return (self.parse_json(string), region)
    except ValueError as err:
      raise err

  def regions(self):
    regions = [region for region in self.view.sel() if not region.empty()]

    if len(regions) > 0:
      return regions

    # create a region from the contents of file in case all regions are empty
    return [sublime.Region(0, self.view.size())]


class MinifyJsonCommand(JsonFormatterUtils, sublime_plugin.TextCommand):
  def run(self, edit):
    try:
      structures = tuple(map(self.parse_region, self.regions()))

      for structure, region in tuple(reversed(structures)):
        string = self.serialize_json(structure)
        self.view.replace(edit, region, string)

    except ValueError as err:
      sublime.status_message(str(err))


class PrettifyJsonCommand(JsonFormatterUtils, sublime_plugin.TextCommand):
  def run(self, edit):
    try:
      structures = tuple(map(self.parse_region, self.regions()))

      for structure, region in tuple(reversed(structures)):
        string = self.serialize_json(structure, indent=2, item_separator=', ', key_separator=': ')
        self.view.replace(edit, region, string)

    except ValueError as err:
      sublime.status_message(str(err))


class PrettifyJsonAndSortKeysCommand(JsonFormatterUtils, sublime_plugin.TextCommand):
  def run(self, edit):
    try:
      structures = tuple(map(self.parse_region, self.regions()))

      for structure, region in tuple(reversed(structures)):
        string = self.serialize_json(structure, indent=2, item_separator=', ', key_separator=': ', sort_keys=True)
        self.view.replace(edit, region, string)

    except ValueError as err:
      sublime.status_message(str(err))
