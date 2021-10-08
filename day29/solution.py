def solution(string: str):
    resp = ""
    curr = None

    for char in string:
        if curr is None:
            curr = char
            continue

        if curr[0] == char:
            curr += char
            continue

        if curr[0] != char:
            resp += f"{len(curr)}{curr[0]}"
            curr = char
            continue

    resp += f"{len(curr)}{curr[0]}"

    return resp


if __name__ == "__main__":
    print(solution("AAAABBBCCDAA"))