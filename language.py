import GrammarLexer, GrammarParser, Visitor
from antlr4 import InputStream, CommonTokenStream
import sys
import pathlib
import os

path = pathlib.Path(__file__).parent.resolve()
runpath = os.getcwd()

def parse_file(path, filename):
    with open(f'{str(path)}/{filename}', 'r') as f:
        text = '\n'.join(f.readlines())
    chars = InputStream(text)
    lexer = GrammarLexer.GrammarLexer(chars)
    tokens = CommonTokenStream(lexer)
    parser = GrammarParser.GrammarParser(tokens)

    parser.buildParseTrees = True
    tree = parser.prog()
    Visitor.Visitor(os.path.splitext(os.path.basename(filename))[0], str(path) + '/' + os.path.dirname(filename)).visit(tree)

stdlib_files = [
    'stdlib.twl',
    'math.twl'
]

for f in stdlib_files:
    parse_file(path, f)
parse_file(runpath, sys.argv[1])