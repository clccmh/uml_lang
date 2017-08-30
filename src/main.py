import sys
from interpreter import Interpreter


def main():
  with open(sys.argv[1], "r") as file:
    interpreter = Interpreter(file.read())
    interpreter.expr()


if __name__ == '__main__':
  main()

