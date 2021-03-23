
def sum_of_range (a: int, b: int) -> int:
    """Counting sum of numbers [a, b)"""

    a, b = min(a, b), max(a, b)

    s = 0

    for number in range(a, b):
        s = s + number
    
    print(f'first number {a}, second number {b}, sum is {s}')

 
