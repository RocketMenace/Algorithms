
def evaluate_rpn(tokens: list[str]) -> int:
    stack = list()
    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "-":
            first_num = stack.pop()
            stack.append(stack.pop() - first_num)
        elif token == "/":
            first_num = stack.pop()
            stack.append(int(stack.pop() / first_num))
        else:
            stack.append(int(token))
    return stack.pop()

if __name__ == "__main__":
    print(evaluate_rpn(tokens = ["2","1","+","3","*"]))
    print(evaluate_rpn(tokens = ["4","13","5","/","+"]))
    print(evaluate_rpn(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))