import sys
import math
from enum import Enum

class uml_object:

  def __init__(self, name):
    self.name = name
    self.content = []


  def add_content_item(self, item):
    self.content.append(item)


  def get_width(self):
    width = len(self.name)
    for item in self.content:
      if len(item) > width:
        width = len(item)
    return width


  def __str__(self):
    width = self.get_width()
    string = "|" + "-" * (width+2) + "|\n"
    string += "| " + " " * math.floor((width - len(self.name))/2) + self.name + " " * math.ceil((width - len(self.name))/2) + " |\n" + "|" + "=" * (width + 2) +  "|"
    for item in self.content:
      string += "\n| " + item.lstrip() + " " * (width - len(item.lstrip())) + " |\n" + "|" + "-" * (width + 2) + "|"
    return  string


def depth(line):
  if line[0] != " ":
    return 0
  else:
    return 1


def is_comment(line):
  return line[0] == "#"


def parse(data):
  objects = []
  for line in data.split("\n"):
    if line:
      if not is_comment(line):
        if depth(line) == 0:
          objects.append(uml_object(line))
        if depth(line) == 1:
          objects[-1].add_content_item(line)

  return objects


def main():
  file = open(sys.argv[1], "r")
  data = file.read()
  objects = parse(data)
  for obj in objects:
    print(obj)
    print("\n\n\n")

main()

