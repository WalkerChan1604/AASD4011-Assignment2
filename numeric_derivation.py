
def derive(f, x, h=0.0001):
    # Calculate the derivative using the definition: (f(x + h) - f(x)) / h
    derivative = (f(x + h) - f(x)) / h
    return derivative