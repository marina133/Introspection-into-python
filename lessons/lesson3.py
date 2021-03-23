
def log_function(n: float, m: float):
    """Calculates the integer part of logarithm of m (base n)"""

    x = 0
    m_copy = m

    while(m >= n):
        m = m / n
        x = x + 1

    print(f'n = {n}, m = {m_copy}, result is {x}')


