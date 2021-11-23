from antlr.CoolLexer import *
from antlr.CoolParser import *
from antlr4 import *

from letListener import LetListener


def main(file):
    parser = CoolParser(CommonTokenStream(CoolLexer(FileStream(file))))
    tree = parser.program()

    walker = ParseTreeWalker()
    letchecker = LetListener()
    walker.walk(letchecker, tree)


if __name__ == '__main__':
    main("./resources/semantic/input/letself.cool")
