import GrammarLexer, GrammarParser, Visitor
from antlr4 import InputStream, CommonTokenStream
import sys

def parse_file(filename):
    with open(filename, 'r') as f:
        text = '\n'.join(f.readlines())
    chars = InputStream(text)
    lexer = GrammarLexer.GrammarLexer(chars)
    tokens = CommonTokenStream(lexer)
    parser = GrammarParser.GrammarParser(tokens)

    parser.buildParseTrees = True
    tree = parser.prog()
    Visitor.Visitor(filename.split('.')[0]).visit(tree)

parse_file('stdlib.twl')
parse_file(sys.argv[1])