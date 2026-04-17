def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(limit):
    """Return a list of all prime numbers up to the given limit."""
    return [n for n in range(2, limit + 1) if is_prime(n)]


def get_first_n_primes(count):
    """Return the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def print_primes(primes, label="Prime Numbers"):
    """Print the list of prime numbers in a formatted way."""
    print(f"\n{label}")
    print("-" * 40)
    print(primes)
    print(f"Total count: {len(primes)}")


# ── Main Program ──────────────────────────────
if __name__ == "__main__":

    # 1. Primes up to a limit
    limit = 50
    primes_up_to = get_primes_up_to(limit)
    print_primes(primes_up_to, label=f"Primes up to {limit}")

    # 2. First N primes
    n = 10
    first_n = get_first_n_primes(n)
    print_primes(first_n, label=f"First {n} Primes")

    # 3. Check if a specific number is prime
    number = 97
    result = "✅ Prime" if is_prime(number) else "❌ Not Prime"
    print(f"\nIs {number} a prime number? {result}")