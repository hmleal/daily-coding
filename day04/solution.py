def solution(numbers: list[int]) -> int:
    """
    timeComplexity:  WorstCase: BigO(2n) // BestCase: BigO(n)
    spaceComplexity: BigO(n)
    """
    array_size = len(numbers)

    found = [True] + [False] * (array_size - 1)

    for n in numbers:
        if 0 < n < array_size:
            found[n] = True

    for idx, n in enumerate(found):
        if not n:
            return idx

    return array_size + 1


if __name__ == "__main__":
    print(solution([3, 4, -1, 1]))
