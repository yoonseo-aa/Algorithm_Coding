N, M = map(int, input().split())

min_package = float('inf')
min_single = float('inf')

for _ in range(M):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

case1 = ((N + 5) // 6) * min_package
case2 = N * min_single
case3 = (N // 6) * min_package + (N % 6) * min_single

print(min(case1, case2, case3))