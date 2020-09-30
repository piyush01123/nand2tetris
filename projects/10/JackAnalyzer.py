
import sys
import os
import re


class JackTokenizer:
    def __init__(self, jack_filename):
        self.jack_file = open(jack_filename, 'r')
        self.num_chars = len(open(jack_filename, 'r').read()) + len(open(jack_filename, 'r').readlines())
        self.read_chars = 0
        self.tokens = []
        self.token_types = []
        self.keyword_regex = r'class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this|let|do|if|else|while|return'
        self.symbol_regex = r'\{|\}|\(|\)|\[|\]|\.|\,|\;|\+|\-|\*|\/|\&|\||\<|\>|\=|\~'
        self.integer_regex = r'\d{1,5}'
        self.string_regex = '\".*\"'
        self.identifier_regex = r'\w+'

    def hasMoreTokens(self):
        return self.read_chars < self.num_chars

    def advance(self):
        while True:
            self.jack_file.seek(self.read_chars, 0)
            line = self.jack_file.readline()
            if len(line)==0:
                self.read_chars = self.num_chars
                return
            self.read_chars += len(line)
            if line.strip().startswith('//'):
                continue
            if line =='\n':
                continue
            if line.strip().startswith('/*'):
                while not line.strip().endswith('*/'):
                    line = self.jack_file.readline()
                    self.read_chars += (len(line) +1)
                continue
            break
        line = line.strip()
        if '//' in line:
            line = line[:line.index('//')]
        if len(line)==0:
            return
        # print(line.encode('utf-8'), self.read_chars, "MADEIT")
        self.line_tokens, self.line_token_types, self.positions = [], [],[]
        self.parseTokens(line)

    def parseTokens(self, line):
        self.parseKeyords(line)
        self.parseSymbols(line)
        self.parseIntVals(line)
        self.parseStringVal(line)
        self.parseIdentifiers(line)
        indices = sorted(range(len(self.positions)), key=self.positions.__getitem__)
        for idx in indices:
            token = self.line_tokens[idx]
            token_type = self.line_token_types[idx]
            self.tokens.append(token)
            self.token_types.append(token_type)

    def parseKeyords(self, line):
        p = re.compile(self.keyword_regex)
        for m in p.finditer(line):
            if m.group()=='int' and line[m.start()-2:m.end()]=='print':
                continue
            self.line_tokens.append(m.group())
            self.line_token_types.append("keyword")
            self.positions.append(m.start())

    def parseSymbols(self, line):
        p = re.compile(self.symbol_regex)
        for m in p.finditer(line):
            self.line_tokens.append(m.group())
            self.line_token_types.append("symbol")
            self.positions.append(m.start())

    def parseIntVals(self, line):
        p = re.compile(self.integer_regex)
        for m in p.finditer(line):
            self.line_tokens.append(m.group())
            self.line_token_types.append("integerConstant")
            self.positions.append(m.start())

    def parseStringVal(self, line):
        p = re.compile(self.string_regex)
        for m in p.finditer(line):
            self.line_tokens.append(m.group()[1:-1])
            self.line_token_types.append("stringConstant")
            self.positions.append(m.start())

    def parseIdentifiers(self, line):
        p = re.compile(self.identifier_regex)
        for m in p.finditer(line):
            if re.match(self.keyword_regex, m.group()) is None and \
                   re.match(self.symbol_regex, m.group()) is None and \
                   re.match(self.integer_regex, m.group()) is None and \
                   re.match(self.string_regex, m.group()) is None :
                if '"' in line and m.start()>line.index('"') and m.end()<len(line)-line[::-1].index('"'):
                    continue
                self.line_tokens.append(m.group())
                self.line_token_types.append("identifier")
                self.positions.append(m.start())


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


class JackTokenizerStream:
    def __init__(self, jack_filename):
        tknzr = JackTokenizer(jack_filename)
        while tknzr.hasMoreTokens():
            tknzr.advance()
        self.tokens = tknzr.tokens
        self.token_types = tknzr.token_types
        self.idx = 0
    def hasMoreTokens(self):
        return self.idx < len(self.tokens)
    def advance(self):
        self.idx += 1
        self.token = self.tokens[self.idx-1]
    def tokenType(self):
        return self.token_types[self.idx-1]
    def keyWord(self):
        if self.tokenType()=="keyword":
            return self.token
    def symbol(self):
        if self.tokenType()=="symbol":
            return self.token
    def identifier(self):
        if self.tokenType()=="identifier":
            return self.token
    def intVal(self):
        if self.tokenType()=="integerConstant":
            return self.token
    def stringVal(self):
        if self.tokenType()=="stringConstant":
            return self.token
    def writeToken(self):
        spl_tokens = {'<':'&lt;', '>':'&gt;', '"':'&quot;', '&':'&amp;'}
        if self.token in spl_tokens.keys():
            return "<{}> {} </{}>".format(self.tokenType(),spl_tokens[self.token],self.tokenType())
        else:
            return "<{}> {} </{}>".format(self.tokenType(),self.token,self.tokenType())


def test_tokenizer_stream(jack_filename):
    tokenizer = JackTokenizerStream(jack_filename)
    token_xml = open(jack_filename.replace('.jack', 'T.xml'), 'w')
    token_xml.write("<tokens>\n")
    while tokenizer.hasMoreTokens():
        tokenizer.advance()
        token_xml.write(tokenizer.writeToken())
        token_xml.write('\n')
    token_xml.write('</tokens>')
    token_xml.close()


class CompilationEngine:
    def __init__(self, jack_filename):
        self.tokenizer = JackTokenizerStream(jack_filename)

    def compileClass(self):
        self.write_output('<class>')
        self.tokenizer.advance()
        assert self.tokenizer.keyWord() == 'class'
        self.write_output('</class>')

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

    def write_XML(self, xml_file):
        self.xml_file = xml_file
        self.compileClass()

    def write_output(self, str_to_write):
        self.xml_file.write(str_to_write)
        self.xml_file.write('\n')


def test_analyzer(jack_filename):
    compilation_engine = CompilationEngine(jack_filename)
    compiled_xml_file = open(jack_filename.replace('.jack', '.xml'), 'w')
    compilation_engine.write_XML(compiled_xml_file)
    compiled_xml_file.close()


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
        # test_tokenizer(jack_filename)
        # test_tokenizer_stream(jack_filename)
        test_analyzer(jack_filename)


if __name__=="__main__":
    main()