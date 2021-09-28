def solution(k: int, numbers: list[int]) -> bool:
    if k == 0:
        return True

    if k < 0:
        return False

    for n in numbers:
        remainder = k - n

        if solution(remainder, numbers):
            return True

    return False


if __name__ == "__main__":
    print(solution(17, [10, 15, 3, 7]))
