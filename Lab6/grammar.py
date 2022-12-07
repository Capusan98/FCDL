class Grammar:
    def __init__(self, file_name):
        self.non_terminal_symbols = list()
        self.terminal_symbols = list()
        self.productions = dict(list())
        self.start_symbol = None
        self.read_from_file(file_name)

    def read_from_file(self, file_name):
        file = open(file_name, "r")
        lines = file.readlines()

        self.non_terminal_symbols = lines[0].strip().split(',')
        self.terminal_symbols = lines[1].strip().split(',')


    def print_menu(self):
        print('OPTIONS: \n'
              '\t1. show non terminals\n'
              '\t2. show terminals\n'
              '\tx. quit\n')

    def menu(self):
        isDone = False

        while not isDone:
            self.print_menu()
            option = input('Your choice is: ')
            if option == '1':
                print('The non terminals: ' + str(self.non_terminal_symbols))
            elif option == '2':
                print('The terminals: ' + str(self.terminal_symbols))
            elif option == 'x':

                isDone = True
            else:
                print('Wrong option! Please try again!')


if __name__ == '__main__':
    grammar = Grammar('g1.txt')
    grammar.menu()