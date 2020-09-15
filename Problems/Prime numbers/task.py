prime_numbers = [n for n in range(2, 1001)
                 if all([n % m for m in range(2, n - 1)])]
