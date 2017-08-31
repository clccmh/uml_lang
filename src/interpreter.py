from token import Token
import uml
from uml import UmlObject, Connection

class Interpreter(object):
  def __init__(self, txt):
    self.txt = txt
    self.pos = 0
    self.current_token = None
    self.current_char = self.txt[self.pos]
    self.last_token = None

  def error(self, additional_text = None):
    if additional_text == None:
      raise Exception('Error parsing input')
    else:
      raise Exception('Error parsing input\n' + additional_text)

  def is_whitespace(self, char):
    return char == " " or char == "\t"

  def advance(self):
    self.pos += 1
    if self.pos > len(self.txt) - 1:
      self.current_char = None
    else:
      self.current_char = self.txt[self.pos]

  def whitespace(self):
    result = ''
    while self.current_char and self.is_whitespace(self.current_char):
      result += self.current_char
      self.advance()
    return result

  def class_token(self):
    result = ''
    while self.current_char and not self.is_whitespace(self.current_char) and self.current_char != "\n":
      result += self.current_char
      self.advance()
    return result

  def class_subitem(self):
    result = ''
    while self.current_char and self.current_char != "\n":
      result += self.current_char
      self.advance()
    return result

  def get_next_token(self):
    result = None
    if self.current_char is not None:
      if self.current_char == "\n":
        result = Token(Token.EOL, "\n")
        self.advance()
      elif self.is_whitespace(self.current_char):
        if self.last_token and self.last_token.type == Token.EOL:
          result = Token(Token.INDENT, self.whitespace())
        else:
          result = Token(Token.WHITESPACE, self.whitespace())
      elif self.last_token and self.last_token.type == Token.INDENT:
        result = Token(Token.CLASS_SUBITEM, self.class_subitem())
      else:
        temp = self.class_token()
        if temp in Token.CONNECTORS:
          result = Token(Token.CONNECTOR, temp)
        else:
          result = Token(Token.CLASS, temp)

    self.last_token = result
    if result:
      return result
    else:
      return Token(Token.EOF, None)

    # We are going to skip this part right now
    # self.error()

  def eat(self, token_type):
    self.current_token = self.get_next_token()
    if self.current_token.type != token_type:
      self.error(str(self.current_token))
    else:
      return self.current_token

  def expr(self):
    self.current_token = self.get_next_token()
    objects = {}
    connections = []
    last_class = None;
    while self.current_token.type is not Token.EOF:
      if self.current_token.type == Token.CLASS:
        if self.current_token.value not in objects:
          uml_obj = UmlObject(self.current_token.value)
          objects[self.current_token.value] = uml_obj
          last_class = uml_obj
        else:
          class1 = objects[self.current_token.value]
          self.eat(Token.WHITESPACE)
          connector = self.eat(Token.CONNECTOR).value
          self.eat(Token.WHITESPACE)
          class2 = self.eat(Token.CLASS)
          if class2.value not in objects:
            self.error(str(class2) + " not defined.")
          class2 = objects[class2.value]
          connections.append(Connection(class1, class2, connector))
          
      if self.current_token.type == Token.CLASS_SUBITEM:
        if last_class:
          last_class.add_content_item(self.current_token.value)
        else:
          self.error()

      self.current_token = self.get_next_token()

    for val in connections:
      if not val.printed:
        print(val)

