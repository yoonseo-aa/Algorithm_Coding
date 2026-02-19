num = input().strip()
original = num

if len(num) == 1:
    num = '0' + num

cycle = 0

while True:
    cycle += 1

    a = int(num[0])
    b = int(num[1])

    new_sum = a + b
    new_num = num[1] + str(new_sum % 10)

    if new_num == original.zfill(2):
        break

    num = new_num

print(cycle)
