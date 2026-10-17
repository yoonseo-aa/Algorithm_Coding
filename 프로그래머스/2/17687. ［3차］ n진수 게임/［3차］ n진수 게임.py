def solution(n, t, m, p):
    digits = "0123456789ABCDEF"
    sequence = ""
    num = 0

    while len(sequence) < t * m:
        x = num
        converted = ""

        if x == 0:
            converted = "0"

        while x > 0:
            converted = digits[x % n] + converted
            x //= n

        sequence += converted
        num += 1

    return sequence[p - 1::m][:t]