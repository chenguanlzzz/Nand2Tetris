from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine
import sys, os, glob

tokenDict = {'SYMBOL': 'symbol', 'STRING_CONST': 'stringConstant', 
            'KEYWORD': 'keyword', 'INT_CONST': 'integerConstant', 
            'IDENTIFIER': 'identifier'}

def main():
    files = glob.glob(sys.argv[1] + '/*.jack')
    for file in files:
        # dirLength = len(sys.argv[1])+1
        # fileName = sys.argv[1] + "/My" + file[dirLength:-5] + 'T.xml'

        '''
        fileName = sys.argv[1] + "/My" + file[dirLength:-5] + '.xml'
        try:
            os.remove(fileName)
        except:
            pass
        '''

        '''
        # Tokenize the file
        fileToken = JackTokenizer(file)
        fout = open(fileName, 'w')
        fout.write('<tokens>\n')
        while fileToken.hasMoreTokens():
            fileToken.advance()
            if not fileToken.hasMoreTokens():
                break
            tokenType = tokenDict[fileToken.getTokenType()]
            fout.write(f'<{tokenType}>'
                       +f' {fileToken.getToken()} '
                       +f'</{tokenType}> \n')

        fout.write('</tokens>\n')
        fout.close()
        '''

        # Compile for parser
        jackParser = CompilationEngine(file)
        jackParser.compileClass()
        jackParser.close()


            




    

    

if __name__ == "__main__":
    main()