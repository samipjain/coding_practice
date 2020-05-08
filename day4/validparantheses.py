def isValid(s):
    stack = []
    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char) # Push the element in the stack
        else:
            if not stack: # For use case: input - "}"
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False 
            if current_char == "[":
                if char != "]":
                    return False
     #Check if empty stack
    if stack: # For input "("
        return False
    return True

if __name__ == "__main__":
    expr = "{]"

    print(isValid(expr))


