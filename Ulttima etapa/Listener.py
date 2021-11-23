from antlr4 import *
from antlr.CoolParser import CoolParser
from antlr.CoolListener import CoolListener
from myexceptions import *


class Listener(CoolListener):

    def enterAtribute(self, ctx: CoolParser.AtributeContext):
        if ctx.ID().getText() == "self":
            raise SelfVariableException
