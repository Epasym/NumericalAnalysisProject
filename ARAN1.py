import matplotlib.pyplot as plt
import numpy as np
import random
import math


def f(x):
    f = np.exp(np.sin(x) ** 3) + x ** 6 - 2 * (x ** 4) - x ** 3 - 1
    return f


def fder1(x):
    f = 3 * np.exp(np.sin(x) ** 3) * np.cos(x) * np.sin(x) ** 2 + 6 * x ** 5 - 8 * x ** 3 - 3 * x ** 2
    return f


def fder2(x):
    f = -6 * (np.sin(x) * (np.sin(x) * (3 * (
            np.sin(x) * (4 * (25 * np.cos(x) - 24) * np.sin(x) + 47) - 84 * np.cos(x)) + 334) - 94) + 20 * np.cos(
        x) - 59)
    return f


def bisection_method(a, b, tolerance):

    print(f"\nSearching in range[{a},{b}]")

    if f(a) == 0:
        print(f"Root is {a}, initial lower boundary!\n")
        return a
    elif f(b) == 0:
        print(f"Root is {b}, initial upper boundary!\n")
        return b
    elif f(a) * f(b) >= 0:
        print(f"No or multiple roots in [{a},{b}], bisection does not work!\n")
        return "no roots"

    error = abs(b - a)

    N = math.ceil((math.log(abs(b - a)) - math.log((1 / 2) * (1 / pow(10, tolerance)))) / math.log(2))

    for i in range(N):

        xi = (b + a) / 2

        try:
            if f(a) * f(xi) < 0:
                b = xi
                error = abs(b - a)
            elif f(b) * f(xi) < 0:
                a = xi
                error = abs(b - a)
            else:
                print(f"Lower boundary a is: {a} and upper b is: {b}, approximate root: {xi}, rounded to: "
                      f"{round(xi, tolerance)}"
                      f" after {i + 1} iterations.\n")
                return [round(xi, tolerance), i + 1]
        except Exception as e:
            print(type(e))
            print("Something went wrong\n")
            return [round(xi, tolerance), i + 1]

    print(f"Error is: {error}")
    print(f"Lower boundary a is: {a} and upper b is: {b}, approximate root: {xi}, rounded to: {round(xi, tolerance)}"
          f" after {i + 1} iterations.\n")
    return [round(xi, tolerance), i + 1]


def newton_raphson_method(a, b, tolerance):
    print(f"\nSearching in range[{a},{b}]")

    if f(a) == 0:
        print(f"Root is {a}, initial lower boundary!\n")
        return a
    elif f(b) == 0:
        print(f"Root is {b}, initial upper boundary!\n")
        return b

    x = random.uniform(a, b)
    counter = 0
    while f(x) * fder2(x) <= 0 or fder1(x) == 0 or f(x) == 0:
        if f(x) == 0:
            print(f"Nice guess! Root is {x}\n")
            return [round(x, tolerance), 0]
        x = random.uniform(a, b)
        counter += 1
        if counter > 50:
            return "Couldn't find appropriate guess"

    print(f"Guess is: {x}")

    try:
        for i in range(100):

            xi = x - (f(x) / fder1(x))

            error = abs(xi - x)
            if error < (1 / 2) * (1 / pow(10, tolerance)):
                print(
                    f"Error is: {error}\nApproximate root: {xi}, rounded to: {round(xi, tolerance)} after {i} iterations\n")
                return [round(xi, tolerance), error, i + 1]
            x = xi
    except Exception as e:
        print(type(e))
        print(f"Something went wrong after {i} iterations.\n")

    print(f"Maximum iterations reached, failed to find root in [{a},{b}]")

    return [round(xi, tolerance), error, i + 1]


def secant_method(x0, x1, tolerance):
    print(f"\nSearching in range[{x0},{x1}]")

    if f(x0) == f(x1):
        return "Line is parallel to x axis! Secant doesn't work!"

    if f(x0) == 0:
        print(f"Root at lower boundary. Root is {x0}\n")
        return x0
    if f(x1) == 0:
        print(f"Root at upper boundary. Root is {x1}\n")
        return x1

    for i in range(1, 100):
        y0 = f(x0)
        y1 = f(x1)
        try:
            xi = x0 - (y0 / ((y0 - y1) / (x0 - x1)))
        except Exception as e:
            print(type(e))
            print(f"Oh no, division by zero after {i + 1} iterations!")
            print(f"x={xi}, rounded to: {round(xi, tolerance)}\nf(x)={f(xi)}\n")
            return [round(xi, tolerance), error, i + 1]
        x0 = x1
        x1 = xi
        error = abs(x1 - x0)
        if error < (1 / 2) * (1 / pow(10, tolerance)):
            print(f"Error is: {error}\nApproximate root: {xi}, rounded to: {round(xi, tolerance)} "
                  f"after {i + 1} iterations")
            return [round(xi, tolerance), error, i + 1]
        if f(x0) == f(x1):
            print("Line is parallel to x axis!")
            print(f"Error is: {error}\nApproximate root: {xi}, rounded to: {round(xi, tolerance)} "
                  f"after {i + 1} iterations\n")
            return [round(xi, tolerance), error, i + 1]

    print(f"Maximum iterations reached, approximate root: {xi}, rounded to: {round(xi, tolerance)} "
          f"after {i + 1} iterations\n")
    return [round(xi, tolerance), error, i + 1]

def main():
    tolerance = 5
    print("BISECTION:")
    print(bisection_method(-2, 2, tolerance))
    for i in range(4):
        print(bisection_method(i - 2, i - 1, tolerance))

    print("NEWTON-RAPHSON")
    print(newton_raphson_method(-2, 2, tolerance))
    for i in range(4):
        print(newton_raphson_method(i - 2, i - 1, tolerance))

    print("SECANT")
    print(secant_method(-2, 2, tolerance))
    for i in range(4):
        print(secant_method(i - 2, i - 1, tolerance))

    x = np.linspace(-2, 2, 100)
    fig = plt.figure(figsize=(10, tolerance))
    plt.plot(x, f(x))
    plt.grid()
    plt.axis()
    plt.title("Ex 1")
    plt.show()

    return 0

main()
