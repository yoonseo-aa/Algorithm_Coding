rating = 0
gpa = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
sum_v = 0
credit = 0
for _ in range(20):
    subject = list(input().split())
    if subject[2] == 'P':
        continue
    credit += float(subject[1])
    sum_v += (gpa[subject[2]] * float(subject[1]))

print(f'{sum_v / credit:.6f}')