import operator

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
    "%": operator.mod,
    "//": operator.floordiv,
    "**": operator.pow,
    ">>": operator.rshift,
    "<<": operator.lshift,
    "&": operator.and_,
    "|": operator.or_,
    "^|": operator.xor,
    "~": operator.invert,
}

while True:
    mark = input("what is the mark(+,-,/,* and etc.)")

    if mark == "exit":
        break
    elif mark not in operations:
        print("invalid operation, please enter valid mark")
        continue

    no_1 = float(input("enter the 1st number"))
    no_2 = float(input("enter the 2nd number"))

    output = operations[mark](no_1, no_2)
    print("answer:", round(output, 2))