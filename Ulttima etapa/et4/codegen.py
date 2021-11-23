from antlr4 import *
from antlr.CoolLexer import *
from antlr.CoolParser import *
from antlr.CoolListener import *

import sys
from string import Template
import tm

import math

from listener import Listener1


class Output:
    def __init__(self):
        self.accum = ''

    def p(self, *args):
        if len(args) == 1:
            self.accum += '%s:\n' % args[0]
            return
        r = '    %s    ' % args[0]
        for a in args[1:-1]:
            r += ' %s' % str(a)

        if type(args[-1]).__name__ != 'int' and args[-1][0] == '#':
            for i in range(64 - len(r)):
                r += ' '
        r += str(args[-1])

        self.accum += r + '\n'

    def out(self):
        return self.accum


def global_data(o):
    k = dict(intTag=0, boolTag=0, stringTag=0)
    o.accum = asm.gdStr1 + asm.gdTpl1.substitute(k) + asm.gdStr2


def constants(o):
    for i in range(0, len(Listener1().array_int)):
        o.accum += asm.cTplInt.substitute(idx=i,
                                          tag=3, value=Listener1().array_int[i])

    for i in range(0, len(Listener1().array_string)):
        print(int((len(Listener1().array_string[i])+1)/4))
        size = 4 + int(math.ceil((len(Listener1().array_string[i])+1)/4))
        o.accum += asm.cTplStr.substitute(idx=i, tag=5, size=size, sizeIdx=i+len(
            Listener1().array_int), value=Listener1().array_string[i].replace('"', ""))
        o.accum += asm.cTplInt.substitute(idx=i+len(
            Listener1().array_int), tag=3, value=len(Listener1().array_string[i]))

    o.accum += asm.boolStr


def tables(o):
    o.p('class_nameTab')
    o.p('.word', 'str_const3')

    o.p('class_objTab')
    o.p('.word', 'Object_protObj')
    o.p('.word', 'Object_init')

    o.p('Object_dispTab')
    o.p('.word', 'Object.abort')
    o.p('.word', 'Object.type_name')
    o.p('.word', 'Object.copy')


def templates(o):
    o.accum += """
    .word   -1 
Object_protObj:
    .word   0 
    .word   3 
    .word   Object_dispTab 
"""
    o.accum += """
    .word   -1 
String_protObj:
    .word   4 
    .word   5 
    .word   String_dispTab 
    .word   int_const0 
    .word   0 
"""


def heap(o):
    o.accum += asm.heapStr


def global_text(o):
    o.accum += asm.textStr


def class_inits(o):
    pass


def genCode():
    o = Output()
    global_data(o)
    constants(o)
    tables(o)
    templates(o)
    heap(o)
    global_text(o)

    print(o.out())


if __name__ == '__main__':
    parser = CoolParser(CommonTokenStream(
        CoolLexer(FileStream("../resources/codegen/input/assignment-val.cool"))))
    walker = ParseTreeWalker()
    tree = parser.program()

    walker.walk(Listener1(), tree)

    genCode()
