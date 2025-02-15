def generate_primes(n: int) -> list[int]:
    """
    Generates a list of prime numbers up to a given number.

    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.

    Parameters:
    n (int): The upper limit (inclusive) for generating prime numbers. Must be a positive integer.

    Returns:
    list[int]: A list containing all prime numbers up to 'n'.

    Example Usage:
    >>> generate_primes(10)
    [2, 3, 5, 7]

    >>> generate_primes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if n < 2:
        return []

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes

# Example
upper_limit = int(input("Enter a number: "))
prime_numbers = generate_primes(upper_limit)

print(f"Prime numbers up to {upper_limit}: {prime_numbers}")
