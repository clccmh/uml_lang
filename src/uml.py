import math

class UmlObject:
  def __init__(self, name):
    self.name = name
    self.content = []
    self.left = None
    self.right = None
    self.up = None
    self.down = None

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

  LEFT  = 'LEFT'
  RIGHT = 'RIGHT'
  UP    = 'UP'
  DOWN  = 'DOWN'

  TO_RIGHT = {"<-" : "->"}
  TO_LEFT = {"->" : "<-"}
  TO_UP = {"->" : "^\n|", "<-" : "^\n|"}
  TO_DOWN = {"->" : "|\nV", "<-" : "|\nV"}

  def __init__(self, uml1, uml2, connector):
    self.uml1 = uml1
    self.uml2 = uml2
    self.connector = connector
    self.orientation = Connection.RIGHT if self.connector in Connection.TO_RIGHT.values() else Connection.LEFT
    self.orient()
    self.printed = False

  def orient(self):
    if self.uml1.right is None and self.uml2.left is None:
      self.uml1.right = self
      self.uml2.left = self
      self.convert_connector(Connection.RIGHT)
    elif self.uml1.left is None and self.uml2.right is None:
      self.uml1.left = self
      self.uml2.right = self
      self.convert_connector(Connection.LEFT)
    elif self.uml1.down is None and self.uml2.up is None:
      self.uml1.down = self
      self.uml2.up = self
      self.convert_connector(Connection.DOWN)
    elif self.uml1.up is None and self.uml2.down is None:
      self.uml1.up = self
      self.uml2.down = self
      self.convert_connector(Connection.UP)
    else:
      raise Exception('More than 4 connections to one object not yet supported.')

  def convert_connector(self, new_orientation):
    if new_orientation == self.orientation:
      return
    if new_orientation == Connection.LEFT:
      self.connector = Connection.TO_LEFT[self.connector]
    elif new_orientation == Connection.RIGHT:
      self.connector = Connection.TO_RIGHT[self.connector]
    elif new_orientation == Connection.UP:
      self.connector = Connection.TO_UP[self.connector]
    elif new_orientation == Connection.DOWN:
      self.connector = Connection.TO_DOWN[self.connector]
    self.orientation = new_orientation

  def __str__(self):
    self.printed = True

    if self.orientation == Connection.RIGHT:
      if self.uml1.left is not None and not self.uml1.left.printed:
        one = str(self.uml1.left)  
      else: 
        one = self.uml1
      if self.uml2.right is not None and not self.uml2.right.printed:
        two = str(self.uml2.right) 
      else:
        two = self.uml2
      return horizontal_combine(horizontal_combine(one, self.connector), two)

    elif self.orientation == Connection.LEFT:
      if self.uml1.right is not None and not self.uml1.right.printed:
        one = str(self.uml1.right)
      else:
        one = self.uml1
      if self.uml2.left is not None and not self.uml2.left.printed:
        two = str(self.uml2.left)
      else:
        two = self.uml2

      return horizontal_combine(horizontal_combine(two, self.connector), one)
    else:
      return "UP and DOWN not yet supported"


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

  # There is an extra line being left at the end by the above.
  # The following negates this problem
  return output[:-1]
    
    
