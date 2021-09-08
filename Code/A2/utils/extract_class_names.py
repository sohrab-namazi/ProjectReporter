from antlr4 import *
from utils.get_java_files import get_files
from utils.path import Path

from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class ClassNameListener(JavaParserLabeledListener):

    def __init__(self):
        self.class_names = []

    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        # print("Enter Class : " + ctx.IDENTIFIER().getText())
        self.class_names.append(ctx.IDENTIFIER().getText())

    def exitClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        pass
        # print("Exit Class : " + ctx.IDENTIFIER().getText())
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
        listener = ClassNameListener()
        walker = ParseTreeWalker()
        walker.walk(listener=listener, t=tree)
        return listener.class_names

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
            listener = ClassNameListener()
            walker = ParseTreeWalker()
            walker.walk(listener=listener, t=tree)

        result = self.class_names.copy()
        self.class_names.clear()
        return result


if __name__ == '__main__':
    class_name_listener = ClassNameListener()
    print(class_name_listener.run())
