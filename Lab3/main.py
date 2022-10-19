from SymbolTable import SymbolTable
from Symbol import Symbol

def main():
    st = SymbolTable()

    sb1 = Symbol("a", "int")
    sb2 = Symbol("b", "char")
    sb3 = Symbol("c", "int")

    st.add("a")
    st.add("c")
    st.add("b")

    #st.add(sb1)
    #st.add(sb2)
    #st.add(sb3)

    print(st.get("a"))
    print(st.get("b"))
    print(st.get("c"))


main()