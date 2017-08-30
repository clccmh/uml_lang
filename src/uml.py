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
    return horizontal_combine(horizontal_combine(self.uml1, self.connector), self.uml2)


def horizontal_combine(one, two):
  one = str(one).split("\n")
  two = str(two).split("\n")

  index = 0
  output = ""
  lone = len(one)
  ltwo = len(two)

  while index < lone or index < ltwo:
    output += one[index] if index < lone else " " * len(one[0])
    output += "  "
    output += two[index] if index < ltwo else " " * len(two[0])
    output += "\n"
    index += 1

  return output
    
    
