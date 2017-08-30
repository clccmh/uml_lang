from token import Token

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
    if self.current_token.type == token_type:
      self.current_token = self.get_next_token()
    else:
      self.error(str(self.current_token.value))

  def expr(self):
    result = self.get_next_token()
    while result.type is not Token.EOF:
      if result.type != Token.EOL and result.type != Token.WHITESPACE and result.type != Token.INDENT:
        print(result)
      result = self.get_next_token()

