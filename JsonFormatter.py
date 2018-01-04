import json
import sublime
import sublime_plugin

from JsonFormatterUtils import parse_json, serialize_json

class MinifyJsonCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = sublime.Region(0, self.view.size())

    json_string = self.view.substr(region)
    structure = json_parse(json_string)

    if not structure:
      self.view.window().status_message('Invalid json')
    else:
      minified_json_string = serialize_json(structure)
      self.view.replace(edit, region, minified_json_string)

class PrettifyJsonCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    pass

class PrettifyJsonAndSortKeysCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    pass
