from JackTokenizer import JackTokenizer 
import os

tokenDict = {'SYMBOL': 'symbol', 'STRING_CONST': 'stringConstant', 
            'KEYWORD': 'keyword', 'INT_CONST': 'integerConstant', 
            'IDENTIFIER': 'identifier'}

statements = ['if', 'while', 'let', 'do', 'return']
operations = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']
unaryOps = ['+', '~']

class CompilationEngine():

    def __init__(self, file):
        self.fileToken = JackTokenizer(file)
        dirName, fileName = file.split('/')
        compFileName = dirName +'/My' + fileName[:-5] + '.xml'
        try:
            os.remove(compFileName)
        except:
            pass
        self.fout = open(compFileName, 'w')

    def advance(self):
        self.fileToken.advance()
    

    def tokenPrint(self):
        tokenType = tokenDict[self.fileToken.getTokenType()]
        self.fout.write(f'<{tokenType}>'
                       +f' {self.fileToken.getToken()} '
                       +f'</{tokenType}> \n')

    
    def compileClass(self):
        self.fout.write('<class>\n')
        while (self.fileToken.hasMoreTokens()):
            self.advance()
            token = self.fileToken.getToken()
            if (token == 'static' or token == 'field'):
                self.compileClassVarDec()
                continue
            elif (token == 'constructor' or token == 'function' or token == 'method'):
                self.compileSubroutineDec()
                continue
            elif (token == '}'):
                self.tokenPrint()
                break
            else:
                self.tokenPrint()
        self.fout.write('</class>\n')

    def compileClassVarDec(self):
        self.fout.write('<classVarDec>\n')
        while (self.fileToken.getToken() != ';'):
            self.tokenPrint()
            self.advance()
        self.tokenPrint()
        self.fout.write('</classVarDec>\n')

    def compileSubroutineDec(self):
        self.fout.write('<subroutineDec>\n')
        while (self.fileToken.getToken() != '}'):
            token = self.fileToken.getToken()

            if (token == '{'):
                self.compileSubroutineBody()
                break

            if (token == '('):
                self.tokenPrint()
                self.advance()
                self.compileParameterList()
                continue

            self.tokenPrint()
            self.advance()
        self.fout.write('</subroutineDec>\n')

    def compileParameterList(self):
        self.fout.write('<parameterList>\n')
        token = self.fileToken.getToken()
        while (token != ')'):
            self.tokenPrint()
            self.advance()
            token = self.fileToken.getToken()
        self.fout.write('</parameterList>\n')
        self.tokenPrint()
        self.advance()

    def compileSubroutineBody(self):
        self.fout.write('<subroutineBody>\n')
        token = self.fileToken.getToken()
        while (token != '}'):
            if (token == 'var'):
                self.compileVarDec()
                token = self.fileToken.getToken()
                continue

            if (token in statements):
                self.compileStatements()
                token = self.fileToken.getToken()
                continue

            self.tokenPrint()
            self.advance()
            token = self.fileToken.getToken()
        self.tokenPrint()
        self.fout.write('</subroutineBody>\n')


    def compileVarDec(self):
        self.fout.write('<varDec>\n')
        token = self.fileToken.getToken()
        while (token != ';'):
            self.tokenPrint()
            self.advance()
            token = self.fileToken.getToken()
        self.tokenPrint()
        self.advance()
        self.fout.write('</varDec>\n')




    def compileStatements(self):
        self.fout.write('<statements>\n')
        while (self.fileToken.getToken() in statements):
            token = self.fileToken.getToken()
            if token == 'if':
                self.compileIf()
            elif token == 'while':
                self.compileWhile()
            elif token == 'let':
                self.compileLet()
            elif token == 'do':
                self.compileDo()
            elif token == 'return':
                self.compileReturn()
            token = self.fileToken.getToken()
        self.fout.write('</statements>\n')
    
    def compileIf(self):
        self.fout.write('<ifStatement>\n')
        while (True):
            token = self.fileToken.getToken()
            if (token == '('):
                self.tokenPrint()
                self.advance()
                self.compileExpression()
                self.tokenPrint()
                self.advance()
                continue

            elif (token == '{'):
                self.tokenPrint()
                self.advance()
                self.compileStatements()
                self.tokenPrint()
                token = self.fileToken.getToken()
                continue

            elif (token == '}'):
                self.advance()
                token = self.fileToken.getToken()
                if (token == 'else'):
                    continue
                else:
                    break

            self.tokenPrint()
            self.advance()
            token = self.fileToken.getToken()
        self.fout.write('</ifStatement>\n')
        

    def compileWhile(self):
        self.fout.write('<whileStatement>\n')
        while (self.fileToken.getToken()!= '}'):
            token = self.fileToken.getToken()
            if (token == '('):
                self.tokenPrint()
                self.advance()
                self.compileExpression()
                self.tokenPrint()
                self.advance()
                continue

            if (token == '{'):
                self.tokenPrint()
                self.advance()
                self.compileStatements()
                continue

            self.tokenPrint()
            self.advance()
            token = self.fileToken.getToken()
        self.tokenPrint()
        self.advance()
        self.fout.write('</whileStatement>\n')


    def compileLet(self):
        self.fout.write('<letStatement>\n')
        while self.fileToken.getToken() != ';':
            token = self.fileToken.getToken()
            if self.fileToken.getTokenType() == 'IDENTIFIER':
                self.tokenPrint()
                self.advance() 
                if self.fileToken.getToken() == '[':
                    self.tokenPrint()
                    self.advance()
                    self.compileExpression()
                    self.tokenPrint()
                    self.advance()
                continue

            if token == '=':
                self.tokenPrint()
                self.advance()
                self.compileExpression()
                continue
            self.tokenPrint()
            self.advance()
        self.tokenPrint()
        self.advance()    
        self.fout.write('</letStatement>\n')


    def compileDo(self):
        self.fout.write('<doStatement>\n')
        while self.fileToken.getToken() != ';':
            if self.fileToken.getToken() == '(':
                self.tokenPrint()
                self.advance()
                self.compileExpressionList()
                self.tokenPrint()
                self.advance()
                continue
            self.tokenPrint()
            self.advance()
        self.tokenPrint()
        self.advance()    
        self.fout.write('</doStatement>\n')

    def compileReturn(self):
        self.fout.write('<returnStatement>\n')
        while self.fileToken.getToken() != ';':
            token = self.fileToken.getToken()
            if token != 'return':
                self.compileExpression()
                continue
            self.tokenPrint()
            self.advance()
        self.tokenPrint()
        self.advance()    
        self.fout.write('</returnStatement>\n')
            
    def compileExpression(self):
        self.fout.write('<expression>\n')
        self.compileTerm()
        if self.fileToken.getToken() in operations:
            self.tokenPrint()
            self.advance()
            self.compileTerm()
        self.fout.write('</expression>\n')


    def compileTerm(self):
        self.fout.write('<term>\n')
        token = self.fileToken.getToken()
        tokenType = self.fileToken.getTokenType()
        if tokenType == 'IDENTIFIER':
            self.tokenPrint()
            self.advance()
            token = self.fileToken.getToken()
            if token == '[':
                self.tokenPrint()
                self.advance()
                self.compileExpression()
                self.tokenPrint()
                self.advance()
            elif token == '.':
                self.tokenPrint()
                self.advance()
                self.tokenPrint()
                self.advance()
                self.tokenPrint()
                self.advance()
                self.compileExpressionList()
                self.tokenPrint()
                self.advance()
        elif token == '(':
            self.tokenPrint()
            self.advance()
            self.compileExpression()
            self.tokenPrint()
            self.advance()
        elif token in unaryOps or token in operations:
            self.tokenPrint()
            self.advance()
            self.compileTerm()
        else:
            self.tokenPrint()
            self.advance()
        self.fout.write('</term>\n')


    def compileExpressionList(self):
        self.fout.write('<expressionList>\n')
        token = self.fileToken.getToken()
        while token != ')':
            if token == ',':
                self.tokenPrint()
            else:
                self.compileExpression()
                token = self.fileToken.getToken()
                continue
            self.advance()
            token = self.fileToken.getToken()
        self.fout.write('</expressionList>\n')


    def close(self):
        self.fout.close()