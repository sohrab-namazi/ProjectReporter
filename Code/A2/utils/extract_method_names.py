from antlr4 import *
from utils.get_java_files import get_files
from utils.path import Path

from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class MethodNameListener(JavaParserLabeledListener):

    def __init__(self):
        self.method_names = []

    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        # print("Enter Method : " + ctx.IDENTIFIER().getText())
        self.method_names.append(ctx.IDENTIFIER().getText())

    def exitMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        pass
        # print("Exit Method : " + ctx.IDENTIFIER().getText())
        # self.class_names.append(ctx.IDENTIFIER().getText())

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
        listener = MethodNameListener()
        walker = ParseTreeWalker()
        walker.walk(listener=listener, t=tree)

        return listener.method_names

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
            listener = MethodNameListener()
            walker = ParseTreeWalker()
            walker.walk(listener=listener, t=tree)
        return self.method_names


if __name__ == '__main__':
    method_listener = MethodNameListener()
    print(method_listener.run())
