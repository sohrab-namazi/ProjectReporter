from antlr4 import *
from utils.get_java_files import get_files
from utils.path import Path

from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class VariableNameListener(JavaParserLabeledListener):

    def __init__(self):
        self.variable_names = []

    def enterVariableDeclaratorId(self, ctx: JavaParserLabeled.VariableDeclaratorIdContext):
        # print("Enter Class Variable : " + ctx.IDENTIFIER().getText())
        self.variable_names.append(ctx.IDENTIFIER().getText())

    def exitVariableDeclaratorId(self, ctx: JavaParserLabeled.VariableDeclaratorIdContext):
        pass
        # print("Exit Class Variable : " + ctx.IDENTIFIER().getText())
        # self.variable_names.append(ctx.IDENTIFIER().getText())

    def run_file(file_path):
        try:
            stream = FileStream(file_path)
        except UnicodeDecodeError:
            print("This file can not be decoded:\n" + file_path + "\n")
            return
        lexer = JavaLexer(stream)
        tokens = CommonTokenStream(lexer)
        Parser = JavaParserLabeled(tokens)
        tree = Parser.compilationUnit()
        listener = VariableNameListener()
        walker = ParseTreeWalker()
        walker.walk(listener=listener, t=tree)
        return listener.variable_names

    def run(self):
        files = get_files(Path.project_path)
        for file_path in files:
            try:
                stream = FileStream(file_path)
            except UnicodeDecodeError:
                print("This file can not be decoded:\n" + file_path + "\n")
                continue
            lexer = JavaLexer(stream)
            tokens = CommonTokenStream(lexer)
            Parser = JavaParserLabeled(tokens)
            tree = Parser.compilationUnit()
            listener = VariableNameListener()
            walker = ParseTreeWalker()
            walker.walk(listener=listener, t=tree)
        return self.variable_names


if __name__ == '__main__':
    variable_listener = VariableNameListener()
    print(variable_listener.run())
