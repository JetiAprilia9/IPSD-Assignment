def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(count):
    """Generate a list of the first 'count' prime numbers."""
    primes = []
    num = 2  # Start checking for primes from 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def print_prime_pattern(rows):
    """Print the prime number pattern."""
    total_primes = sum(range(1, rows + 1))  # Total number of primes needed
    primes = generate_primes(total_primes)

    index = 0
    for row in range(1, rows + 1):
        for _ in range(row):
            print(primes[index], end=' ')
            index += 1
        print()  # Move to the next line


# Example usage
print_prime_pattern(5)