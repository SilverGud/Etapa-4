from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser
import structure


class Listener1(CoolListener):
    typeTable = {}
    varTable = {}
    array_int = []
    array_string = []

    def __init__(self):
        structure.setBaseClasses()

    def exitInteger(self, ctx: CoolParser.IntegerContext):
        self.array_int.append(ctx.INTEGER())
        self.typeTable[ctx] = structure._allClasses["Int"]

    def exitString(self, ctx: CoolParser.StringContext):
        self.array_string.append(str(ctx.STRING()).replace('"', ""))
        self.typeTable[ctx] = structure._allClasses["String"]

    def exitBool(self, ctx: CoolParser.BoolContext):
        self.typeTable[ctx] = structure._allClasses["Bool"]
