from collections import Counter

def solution(str1, str2):
    arr1 = []
    arr2 = []

    str1 = str1.lower()
    str2 = str2.lower()

    for i in range(len(str1) - 1):
        word = str1[i:i+2]

        if word.isalpha():
            arr1.append(word)

    for i in range(len(str2) - 1):
        word = str2[i:i+2]

        if word.isalpha():
            arr2.append(word)

    counter1 = Counter(arr1)
    counter2 = Counter(arr2)

    intersection = counter1 & counter2

    union = counter1 | counter2

    intersection_count = sum(intersection.values())
    union_count = sum(union.values())

    if union_count == 0:
        return 65536

    return int(intersection_count / union_count * 65536)