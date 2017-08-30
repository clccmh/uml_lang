import math

class UmlObject:
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


class Connection:
  def __init__(self, uml1, uml2, connector):
    self.uml1 = uml1
    self.uml2 = uml2
    self.connector = connector

  def __str__(self):
    return str(self.uml1) + "\n" + str(self.connector) + "\n" + str(self.uml2)
