
import sys
import os
import re


class JackTokenizer:
    def __init__(self, jack_file):
        self.jack_file = open(jack_file, 'r')
        self.num_chars = len(open(jack_file, 'r').read()) + len(open(jack_file, 'r').readlines())
        self.read_chars = 0
        self.tokens = []
        self.token_types = []

        # self.keywords = ["class", "constructor", "function", "method", "field", \
        #                  "static", "var", "int", "char", "boolean", "void", "true", \
        #                  "false", "null", "this", "let", "do", "if", "else", "while", \
        #                  "return"
        #                 ]
        # self.symbols = ["{", "}", "(", ")", "[", "]", ".", ",", ";", "+", "-", "*", "/", "&", "|", "<", ">", "=", "~"]
        # self.integer_constants = "\d{1,5}"
        # self.string_constants = "\"(\S*\s*)*\""
        # _identifier = "\w+"
        # _space = "\n|\t| "

        self.keyword_regex = r'class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this|let|do|if|else|while|return'
        self.symbol_regex = r'\{|\}|\(|\)|\[|\]|\.|\,|\;|\+|\-|\*|\/|\&|\||\<|\>|\=|\~'
        self.integer_regex = r'\d{1,5}'
        self.string_regex = '\".*\"'
        self.identifier_regex = r'\w+'



    def hasMoreTokens(self):
        return self.read_chars < self.num_chars

    def advance(self):
        # print(self.jack_file.read(1))
        # self.read_chars+=1

        # char = self.jack_file.read(1)
        # if char not in [' ', '\n']:
        #     print(char)
        # self.read_chars+=1

        while True:
            # print("SEEKINGAT", self.read_chars)
            self.jack_file.seek(self.read_chars, 0)
            line = self.jack_file.readline()
            if len(line)==0:
                self.read_chars = self.num_chars
                return
            self.read_chars += len(line)
            # print("LINE",line.encode('utf-8'), self.read_chars)

            if line.strip().startswith('//'):
                continue

            if line =='\n':
                # self.read_chars -= 1
                continue

            if line.strip().startswith('/*'):
                while not line.strip().endswith('*/'):
                    line = self.jack_file.readline()
                    self.read_chars += (len(line) +1)
                # line = self.jack_file.readline() # for the line with */
                # self.read_chars += len(line)
                # print("CHECK_END_COMMENT", line.encode('utf-8'), self.read_chars)
                continue
            break

        # print(line.encode('utf-8'), self.read_chars, "MADEIT")
        line = line.strip()
        if ('//') in line:
            line = line[:line.index('//')]
        if len(line)==0:
            return
        # print(line.encode('utf-8'), self.read_chars, "MADEIT")

        line_tokens = []
        positions = []
        token_types = []

        p = re.compile(self.keyword_regex)
        for m in p.finditer(line):
            if m.group()=='int' and line[m.start()-2:m.end()]=='print':
                continue
            line_tokens.append(m.group())
            token_types.append("keyword")
            positions.append(m.start())

        p = re.compile(self.symbol_regex)
        for m in p.finditer(line):
            line_tokens.append(m.group())
            token_types.append("symbol")
            positions.append(m.start())

        p = re.compile(self.integer_regex)
        for m in p.finditer(line):
            line_tokens.append(m.group())
            token_types.append("integerConstant")
            positions.append(m.start())

        p = re.compile(self.string_regex)
        for m in p.finditer(line):
            line_tokens.append(m.group()[1:-1])
            token_types.append("stringConstant")
            positions.append(m.start())

        p = re.compile(self.identifier_regex)
        for m in p.finditer(line):
            if re.match(self.keyword_regex, m.group()) is None and \
                   re.match(self.symbol_regex, m.group()) is None and \
                   re.match(self.integer_regex, m.group()) is None and \
                   re.match(self.string_regex, m.group()) is None :
                if '"' in line and m.start()>line.index('"') and m.end()<len(line)-line[::-1].index('"'):
                    continue
                line_tokens.append(m.group())
                token_types.append("identifier")
                positions.append(m.start())

        # for token in re.findall(self.keyword_regex, line):
        #     # print("keywordTOKEN", token)
        #     line_tokens.append(token)
        #     token_types.append("keyword")
        #     positions.append(line.index(token))
        #
        # for token in re.findall(self.symbol_regex, line):
        #     # print("symbolTOKEN", token)
        #     line_tokens.append(token)
        #     token_types.append("symbol")
        #     positions.append(line.index(token))
        #
        # for token in re.findall(self.integer_regex, line):
        #     # print("integerConstantTOKEN", token)
        #     line_tokens.append(token)
        #     token_types.append("integerConstant")
        #     positions.append(line.index(token))
        #
        # for token in re.findall(self.string_regex, line):
        #     # print("stringConstantTOKEN", token)
        #     line_tokens.append(token)
        #     token_types.append("stringConstant")
        #     positions.append(line.index(token))
        #
        # for token in re.findall(self.identifier_regex, line):
        #     if re.match(self.keyword_regex, token) is None and \
        #        re.match(self.symbol_regex, token) is None and \
        #        re.match(self.integer_regex, token) is None and \
        #        re.match(self.string_regex, token) is None :
        #         # print("identifierTOKEN", token)
        #         line_tokens.append(token)
        #         token_types.append("identifier")
        #         positions.append(line.index(token))
        # print("RES", line_tokens, token_types, positions)
        indices = sorted(range(len(positions)), key=positions.__getitem__)
        for idx in indices:
            token = line_tokens[idx]
            token_type = token_types[idx]
            self.tokens.append(token)
            self.token_types.append(token_type)


    def tokenType(self):
        pass

    def keyWord(self):
        pass

    def symbol(self):
        pass

    def identifier(self):
        pass

    def intVal(self):
        pass

    def stringVal(self):
        pass


class CompilationEngine:
    def __init__(self, jack_file, xml_file):
        self.jack_file = jack_file
        self.xml_file = xml_file

    def compileClass(self):
        pass

    def compileClassVarDec(self):
        pass

    def compileSubroutine(self):
        pass

    def compileParameterList(self):
        pass

    def compileVarDec(self):
        pass

    def compileStatements(self):
        pass

    def compileDo(self):
        pass

    def compileLet(self):
        pass

    def compileWhile(self):
        pass

    def compileReturn(self):
        pass

    def compileIf(self):
        pass

    def compileExpression(self):
        pass

    def compileTerm(self):
        pass

    def compileExpressionList(self):
        pass


def test_tokenizer(jack_filename):
    tokenizer = JackTokenizer(jack_filename)
    while tokenizer.hasMoreTokens():
        tokenizer.advance()

    token_xml = open(jack_filename.replace('.jack', 'T.xml'), 'w')
    token_xml.write("<tokens>\n")
    for tok,tok_typ in zip(tokenizer.tokens, tokenizer.token_types):
        if tok=='<':
            token_xml.write("<{}> {} </{}>\n".format(tok_typ,'&lt;',tok_typ))
        elif tok=='>':
            token_xml.write("<{}> {} </{}>\n".format(tok_typ,'&gt;',tok_typ))
        elif tok=='"':
            token_xml.write("<{}> {} </{}>\n".format(tok_typ,'&quot;',tok_typ))
        elif tok=='&':
            token_xml.write("<{}> {} </{}>\n".format(tok_typ,'&amp;',tok_typ))
        else:
            token_xml.write("<{}> {} </{}>\n".format(tok_typ,tok,tok_typ))
    token_xml.write('</tokens>')
    token_xml.close()


def write_xml(jack_filename):
    xml_filename = jack_filename.replace('.jack', '.xml')

    jack_file.close()
    xml_file.close()


def main():
    if len(sys.argv) != 2:
        raise ValueError("Need 1 argument.")

    if os.path.isfile(sys.argv[1]):
        jack_filenames = [sys.argv[1]]
    elif os.path.isdir(sys.argv[1]):
        jack_dirname = sys.argv[1]
        jack_filenames = [os.path.join(jack_dirname, f) for f in os.listdir(jack_dirname) if f.endswith('.jack')]
    else:
        raise ValueError("No file/dir with arg")

    for jack_filename in jack_filenames:
        test_tokenizer(jack_filename)
        # write_xml(jack_filename)

if __name__=="__main__":
    main()
