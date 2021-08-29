Symbol = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*',
        '/', '&', '|', '<', '>', '=', '~']

SymbolTransfer = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}

Keyword = ['class', 'method', 'function', 'constructor', 'int', 'boolean', 
    'char','void', 'var', 'static', 'field', 'let', 'do', 'if', 'else',
    'while', 'return', 'true', 'false', 'null', 'this']

Integer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



class JackTokenizer():
    def __init__(self, file):
        fin = open(file, 'r')
        self.lines = fin.readlines()
        fin.close()
        self.curLine = 0
        self.lenLines = len(self.lines)
        self.token = ''
        self.curChar = 0
        self.tokenType = ''

    def hasMoreTokens(self):
        if self.curLine < self.lenLines:
            return True
        return False

    def advance(self):
        while self.hasMoreTokens():
            line = self.lines[self.curLine].lstrip()
            commentIndex = line.find('//')
            APIcommentIndex = line.find('/*')
            APIcommentIndex2 = line.find('*')

            # Delete the comment part
            if commentIndex > 0:
                line = line[:commentIndex-1]
            line = line.strip(' \t\r')

            # check the line is newline or the comment line or the API comment?
            if line == '\n' or commentIndex == 0 or APIcommentIndex == 0 or APIcommentIndex2 == 0 or self.curChar >= len(line):
                self.curLine += 1
                self.curChar = 0
                continue
                
            # Continue to find token until it is not a space or new line
            token = line[self.curChar]
            while token == ' ':
                self.curChar += 1
                token = line[self.curChar]
            if token == '\n':
                self.curLine += 1
                self.curChar = 0
                continue
            self.curChar += 1

            # If token is symbol
            if token in Symbol:
                self.token = token
                self.tokenType = 'SYMBOL'
                break

            # If token is string
            if token == '"':
                while(line[self.curChar] != '"'):
                    token += line[self.curChar]                
                    self.curChar += 1
                self.token = token[1:]
                self.tokenType = 'STRING_CONST'
                self.curChar += 1
                break

            # while next character is not a space
            while line[self.curChar] != ' ':
                nextChr = line[self.curChar]

                # If the next char is new line 
                if nextChr == '\n':
                    self.curLine += 1
                    self.curChar = 0
                    break

                # If the next char is symbol
                if nextChr in Symbol:
                    break

                token += nextChr
                self.curChar += 1

            self.token = token
            # If the token is a keyword
            if token in Keyword:
                self.tokenType = 'KEYWORD'
                break
            # If the token is a integer
            if token[0] in Integer:
                self.tokenType = 'INT_CONST'
                break
            # If the token is identifier
            self.tokenType = 'IDENTIFIER'
            break

    def getTokenType(self):
        return self.tokenType
    
    def getToken(self):
        token = self.token
        if token in SymbolTransfer:
            token = SymbolTransfer[token]
        return token


