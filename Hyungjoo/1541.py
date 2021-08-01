expression = list(input())

# change plus operator appeared later than minus operator.
meet_minus = False
for i in range(len(expression)):
    if expression[i] == "-":
        meet_minus = True
    elif meet_minus and expression[i] == "+":
        expression[i] = "-"
expression = "".join(expression)

# remove zero prefix.
expression = expression.split("+")
for i in range(len(expression)):
    phrase = expression[i].split("-")
    phrase_ = []
    for token in phrase:
        phrase_.append(str(int(token)))
    expression[i] = "-".join(phrase_)
expression = "+".join(expression)

print(eval("".join(expression)))
