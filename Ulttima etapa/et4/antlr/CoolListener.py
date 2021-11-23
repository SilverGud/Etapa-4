# Generated from c:\Users\oscar\Documents\Tec\Compiladores\Ulttima etapa\et4\antlr\Cool.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoolParser import CoolParser
else:
    from CoolParser import CoolParser

# This class defines a complete listener for a parse tree produced by CoolParser.
class CoolListener(ParseTreeListener):

    # Enter a parse tree produced by CoolParser#program.
    def enterProgram(self, ctx:CoolParser.ProgramContext):
        pass

    # Exit a parse tree produced by CoolParser#program.
    def exitProgram(self, ctx:CoolParser.ProgramContext):
        pass


    # Enter a parse tree produced by CoolParser#klass.
    def enterKlass(self, ctx:CoolParser.KlassContext):
        pass

    # Exit a parse tree produced by CoolParser#klass.
    def exitKlass(self, ctx:CoolParser.KlassContext):
        pass


    # Enter a parse tree produced by CoolParser#method.
    def enterMethod(self, ctx:CoolParser.MethodContext):
        pass

    # Exit a parse tree produced by CoolParser#method.
    def exitMethod(self, ctx:CoolParser.MethodContext):
        pass


    # Enter a parse tree produced by CoolParser#atribute.
    def enterAtribute(self, ctx:CoolParser.AtributeContext):
        pass

    # Exit a parse tree produced by CoolParser#atribute.
    def exitAtribute(self, ctx:CoolParser.AtributeContext):
        pass


    # Enter a parse tree produced by CoolParser#formal.
    def enterFormal(self, ctx:CoolParser.FormalContext):
        pass

    # Exit a parse tree produced by CoolParser#formal.
    def exitFormal(self, ctx:CoolParser.FormalContext):
        pass


    # Enter a parse tree produced by CoolParser#add.
    def enterAdd(self, ctx:CoolParser.AddContext):
        pass

    # Exit a parse tree produced by CoolParser#add.
    def exitAdd(self, ctx:CoolParser.AddContext):
        pass


    # Enter a parse tree produced by CoolParser#new.
    def enterNew(self, ctx:CoolParser.NewContext):
        pass

    # Exit a parse tree produced by CoolParser#new.
    def exitNew(self, ctx:CoolParser.NewContext):
        pass


    # Enter a parse tree produced by CoolParser#sub.
    def enterSub(self, ctx:CoolParser.SubContext):
        pass

    # Exit a parse tree produced by CoolParser#sub.
    def exitSub(self, ctx:CoolParser.SubContext):
        pass


    # Enter a parse tree produced by CoolParser#mult.
    def enterMult(self, ctx:CoolParser.MultContext):
        pass

    # Exit a parse tree produced by CoolParser#mult.
    def exitMult(self, ctx:CoolParser.MultContext):
        pass


    # Enter a parse tree produced by CoolParser#isvoid.
    def enterIsvoid(self, ctx:CoolParser.IsvoidContext):
        pass

    # Exit a parse tree produced by CoolParser#isvoid.
    def exitIsvoid(self, ctx:CoolParser.IsvoidContext):
        pass


    # Enter a parse tree produced by CoolParser#lt.
    def enterLt(self, ctx:CoolParser.LtContext):
        pass

    # Exit a parse tree produced by CoolParser#lt.
    def exitLt(self, ctx:CoolParser.LtContext):
        pass


    # Enter a parse tree produced by CoolParser#while.
    def enterWhile(self, ctx:CoolParser.WhileContext):
        pass

    # Exit a parse tree produced by CoolParser#while.
    def exitWhile(self, ctx:CoolParser.WhileContext):
        pass


    # Enter a parse tree produced by CoolParser#eq.
    def enterEq(self, ctx:CoolParser.EqContext):
        pass

    # Exit a parse tree produced by CoolParser#eq.
    def exitEq(self, ctx:CoolParser.EqContext):
        pass


    # Enter a parse tree produced by CoolParser#call.
    def enterCall(self, ctx:CoolParser.CallContext):
        pass

    # Exit a parse tree produced by CoolParser#call.
    def exitCall(self, ctx:CoolParser.CallContext):
        pass


    # Enter a parse tree produced by CoolParser#div.
    def enterDiv(self, ctx:CoolParser.DivContext):
        pass

    # Exit a parse tree produced by CoolParser#div.
    def exitDiv(self, ctx:CoolParser.DivContext):
        pass


    # Enter a parse tree produced by CoolParser#neg.
    def enterNeg(self, ctx:CoolParser.NegContext):
        pass

    # Exit a parse tree produced by CoolParser#neg.
    def exitNeg(self, ctx:CoolParser.NegContext):
        pass


    # Enter a parse tree produced by CoolParser#not.
    def enterNot(self, ctx:CoolParser.NotContext):
        pass

    # Exit a parse tree produced by CoolParser#not.
    def exitNot(self, ctx:CoolParser.NotContext):
        pass


    # Enter a parse tree produced by CoolParser#at.
    def enterAt(self, ctx:CoolParser.AtContext):
        pass

    # Exit a parse tree produced by CoolParser#at.
    def exitAt(self, ctx:CoolParser.AtContext):
        pass


    # Enter a parse tree produced by CoolParser#le.
    def enterLe(self, ctx:CoolParser.LeContext):
        pass

    # Exit a parse tree produced by CoolParser#le.
    def exitLe(self, ctx:CoolParser.LeContext):
        pass


    # Enter a parse tree produced by CoolParser#let.
    def enterLet(self, ctx:CoolParser.LetContext):
        pass

    # Exit a parse tree produced by CoolParser#let.
    def exitLet(self, ctx:CoolParser.LetContext):
        pass


    # Enter a parse tree produced by CoolParser#block.
    def enterBlock(self, ctx:CoolParser.BlockContext):
        pass

    # Exit a parse tree produced by CoolParser#block.
    def exitBlock(self, ctx:CoolParser.BlockContext):
        pass


    # Enter a parse tree produced by CoolParser#if.
    def enterIf(self, ctx:CoolParser.IfContext):
        pass

    # Exit a parse tree produced by CoolParser#if.
    def exitIf(self, ctx:CoolParser.IfContext):
        pass


    # Enter a parse tree produced by CoolParser#case.
    def enterCase(self, ctx:CoolParser.CaseContext):
        pass

    # Exit a parse tree produced by CoolParser#case.
    def exitCase(self, ctx:CoolParser.CaseContext):
        pass


    # Enter a parse tree produced by CoolParser#base.
    def enterBase(self, ctx:CoolParser.BaseContext):
        pass

    # Exit a parse tree produced by CoolParser#base.
    def exitBase(self, ctx:CoolParser.BaseContext):
        pass


    # Enter a parse tree produced by CoolParser#assign.
    def enterAssign(self, ctx:CoolParser.AssignContext):
        pass

    # Exit a parse tree produced by CoolParser#assign.
    def exitAssign(self, ctx:CoolParser.AssignContext):
        pass


    # Enter a parse tree produced by CoolParser#parens.
    def enterParens(self, ctx:CoolParser.ParensContext):
        pass

    # Exit a parse tree produced by CoolParser#parens.
    def exitParens(self, ctx:CoolParser.ParensContext):
        pass


    # Enter a parse tree produced by CoolParser#object.
    def enterObject(self, ctx:CoolParser.ObjectContext):
        pass

    # Exit a parse tree produced by CoolParser#object.
    def exitObject(self, ctx:CoolParser.ObjectContext):
        pass


    # Enter a parse tree produced by CoolParser#integer.
    def enterInteger(self, ctx:CoolParser.IntegerContext):
        pass

    # Exit a parse tree produced by CoolParser#integer.
    def exitInteger(self, ctx:CoolParser.IntegerContext):
        pass


    # Enter a parse tree produced by CoolParser#string.
    def enterString(self, ctx:CoolParser.StringContext):
        pass

    # Exit a parse tree produced by CoolParser#string.
    def exitString(self, ctx:CoolParser.StringContext):
        pass


    # Enter a parse tree produced by CoolParser#bool.
    def enterBool(self, ctx:CoolParser.BoolContext):
        pass

    # Exit a parse tree produced by CoolParser#bool.
    def exitBool(self, ctx:CoolParser.BoolContext):
        pass



del CoolParser