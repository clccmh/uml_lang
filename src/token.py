
class Token(object):
  # Token types
  EOL           = 'EOL'
  EOF           = 'EOF'
  CLASS         = 'CLASS'
  CLASS_SUBITEM = 'CLASS_SUBITEM'
  INDENT        = 'INDENT'
  CONNECTOR     = 'CONNECTOR'
  QUANTITY      = 'QUANTITY'
  WHITESPACE    = 'WHITESPACE'

  CONNECTORS = ["->", "<-"]

  def __init__(self, type, value):
    self.type = type
    self.value = value

  def __str__(self):
    return "(Type: " + self.type + "\t\tValue: " + repr(self.value) + ")"
