import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    data = sys.stdin.read().strip()
    if not data:
        sys.exit(0)
    n = int(data)

divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(str(i))

print(" ".join(divisors))
