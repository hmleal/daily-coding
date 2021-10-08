def solution(string: str) -> bool:
    stack = []

    for char in string:
        if char in ["(", "[", "{"]:
            stack.append(char)
            continue

        if char == ")":
            if stack.pop() != "(":
                return False
            continue

        if char == "]":
            if stack.pop() != "[":
                return False
            continue

        if char == "}":
            if stack.pop() != "{":
                return False
            continue

    if stack:
        return False

    return True


if __name__ == "__main__":
    print(solution("([])[]({})"))  # True
    print(solution("([)]"))  # False
    print(solution("((()"))  # False