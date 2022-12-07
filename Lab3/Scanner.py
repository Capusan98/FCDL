import re
from SymbolTable import SymbolTable


class Scanner:


    def __init__(self):
        self.operators = ["+", "-", "*", "/", "%", "=", "==", "<", "<=", ">=", ">", "<>", "&&", "||", "!", ">>", "<<"]
        self.separators = [":", ";", " ", "\n", "\t", "[", "]", "{", "}"]
        self.reserved_words = ["ceva", "altceva", "cevadaca", "totceva", "start", "stop", "cevaint", "cevascris",
                               "cevacitit"]

        self.pif = []
        self.outcome = ""
        self.st = SymbolTable()
        self.outcome = []

    def isPartOfOperator(self, char):
        for op in self.operators:
            if char in op:
                return True
        return False

    def isSeparator(self, char):
        if char in self.separators:
            return True
        return False

    def isReservedWord(self, word):
        if word in self.reserved_words:
            return True
        return False

    def isIdenfifier(self, word):
        return re.search('^[A-Za-z_][A-Za-z0-9_]*', word)

    def isConstant(self, word):
        return re.search('^\d+$', word)

    def scanFile(self, fileName):
        file = open(fileName, 'r')
        lineCount = 0

        for line in file:
            lineCount = lineCount + 1
            index = 0
            token = ''

            while index < len(line):
                if self.isSeparator(line[index]) or self.isPartOfOperator(line[index]):

                    if token != '':
                        if not(self.isReservedWord(token)):
                            if self.isIdenfifier(token) or self.isConstant(token):
                                pos = self.st.add(token)
                                self.pif.append([token, pos])
                            else:
                                self.outcome = (f'lexical error at line {lineCount} '+token)
                        else:
                            self.pif.append([token, -1])

                    token = ''

                else:
                    token = token + line[index]

                index = index + 1
        if len(self.outcome) == 0:
            self.outcome = "lexically correct"

        print(self.outcome)

    def print_to_files(self, fileName):
            pif_file = open("PIF_" + fileName + ".out", "w")
            pif_file.write("Token | Position\n")
            for element in self.pif:
                pif_file.write(element[0] + " | " + str(element[1]) + "\n")
            pif_file.close()

            st_file = open("ST_" + fileName + ".out", "w")
            st_file.write("Symbol Table(sorted list)\n "+str(self.st))
            st_file.close()
