
from Scanner import Scanner

def main():

    scanner = Scanner()
    Scanner.scanFile(scanner, "pb1.txt")
    Scanner.print_to_files(scanner, "pb1")

main()