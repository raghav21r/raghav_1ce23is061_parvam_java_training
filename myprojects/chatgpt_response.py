def is_prime(num):
    """Check if a number is prime"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_primes(n):
    """Print all prime numbers up to n"""
    for i in range(2, n + 1):
        if is_prime(i):
            print(i)


# Example usage
limit = int(input("Enter the limit: "))
print_primes(limit)