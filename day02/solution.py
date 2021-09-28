def solution_one(numbers: list[int]) -> list[int]:
    """
    timeComplexity:  BigO(n^2)
    spaceComplexity: BigO(n)
    """
    result = []

    for idx, i in enumerate(numbers):
        tmp = 1
        for idj, j in enumerate(numbers):
            if idx == idj:
                continue

            tmp *= j

        result.append(tmp)

    return result


def solution_two(numbers: list[int]) -> list[int]:
    """
    timeComplexity:  BigO(2n)
    spaceComplexity: BigO(n)
    """
    total = 1

    for n in numbers:
        total *= n

    result = []

    for n in numbers:
        result.append(total // n)

    return result


if __name__ == "__main__":
    print(solution_one([1, 2, 3, 4, 5]))
    print(solution_two([1, 2, 3, 4, 5]))
