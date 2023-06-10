import math
import matplotlib.pyplot as plt
import numpy as np
import random


def f(x):
    f = 94 * (np.cos(x) ** 3) - 24 * np.cos(x) + 177 * (np.sin(x) ** 2) - 108 * (np.sin(x) ** 4) - 72 * (
            np.cos(x) ** 3) * (np.sin(x) ** 2) - 65
    return f


def fder1(x):
    f = -6 * ((2*np.cos(x) - 1) ** 2) * (15*np.cos(x)**2 - 3*np.cos(x) - 4) * np.sin(x)
    return f


def fder2(x):
    f = (1728 - 1800*np.cos(x))*np.sin(x)**4 + (2358*np.cos(x) - 2004)*np.sin(x)**2 - 402*np.cos(x) + 354
    return f


def bisection_method(a, b, tolerance):
    print(f"\nChecking in [{a}, {b}]")
    if f(a) == 0:
        print(f"Root is {a}, initial lower boundary!\n")
        return a
    elif f(b) == 0:
        print(f"Root is {b}, initial upper boundary!\n")
        return b
    elif f(a) * f(b) >= 0:
        print(f"No or multiple roots in [{a},{b}], bisection does not work!\n")
        return "0"
    error = abs(b - a)
    N = math.ceil((math.log(abs(b - a)) - math.log((1 / 2) * (1 / pow(10, tolerance)))) / math.log(2))
    for i in range(N):

        xi = random.uniform(a, b)

        try:
            if f(a) * f(xi) < 0:
                b = xi
                error = abs(b - a)
            elif f(b) * f(xi) < 0:
                a = xi
                error = abs(b - a)
            else:
                print("Good guess.")
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
    print(f"\nChecking in [{a}, {b}]")
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
            return [round(x, tolerance), 0.0, 0]
        x = random.uniform(a, b)
        counter += 1
        if counter > 50:
            return "Couldn't find appropriate guess"

    print(f"Guess is: {x}")

    try:
        for i in range(100):

            xi = x - (1 / ((fder1(x) / f(x)) - (1 / 2) * (fder2(x) / fder1(x))))

            error = abs(xi - x)
            if error < (1 / 2) * (1 / pow(10, tolerance)):
                print(
                    f"Error is: {error}\nApproximate root: {xi}, rounded to: {round(xi, tolerance)} after {i+1} iterations\n")
                return [round(xi, tolerance), error, i + 1]
            x = xi
    except Exception as e:
        print(type(e))
        print(f"Something went wrong after {i} iterations.\n")

    print(f"Maximum iterations reached, failed to find root in [{a},{b}]")

    return [round(xi, tolerance), error, i + 1]


def secant_method(x0, x1, tolerance):

    print(f"\nChecking in [{x0}, {x1}]")

    if f(x0) == f(x1):
        return "Line is parallel to x axis! Secant doesn't work!"

    if f(x0) == 0:
        print(f"Root at lower boundary. Root is {x0}\n")
        return x0
    if f(x1) == 0:
        print(f"Root at upper boundary. Root is {x1}\n")
        return x1

    def q():
        return f(x0) / f(x1)

    def r():
        return f(x2) / f(x1)

    def s():
        return f(x2) / f(x0)

    x2 = (x0 + x1) / 2
    error = abs(x2 - x1)
    counter = 0
    while s() == 1 or r() == 1 or q() == 1:
        x2 = random.uniform(x0, x1)
        if f(x2) == 0:
            print(f"Nice guess! Root is {round(x2, tolerance)}\n")
            return [round(x2, tolerance), 0.0, 0]
        counter += 1
        if counter > 50:
            return "Couldn't find appropriate x2"

    for i in range(1, 100):

        try:
            xi = x2 - ((r() * (r() - q()) * (x2 - x1) + (1 - r()) * s() * (x2 - x0)) /
                       ((q() - 1) * (r() - 1) * (s() - 1)))
        except Exception as e:
            print(type(e))
            print(f"Oh no, division by zero after {i + 1} iterations!")
            print(f"x={x2}, rounded to: {round(x2, tolerance)}\nf(x)={f(x2)}\nf'(x)={fder1(x2)}\n")
            return [round(xi, tolerance), error, i + 1]
        x0 = x1
        x1 = x2
        x2 = xi
        error = abs(x2 - x1)
        if error < (1/2)*(1/pow(10, tolerance)):
            print(f"Error is: {error}\nApproximate root: {xi}, rounded to: {round(xi, tolerance)} "
                  f"after {i + 1} iterations\n")
            return [round(xi, tolerance), error, i + 1]
        if f(x0) == f(x1):
            print("Line is parallel to x axis!")
            print(f"Error is: {error}\nApproximate root: {xi}, rounded to: {round(xi, tolerance)} "
                  f"after {i + 1} iterations\n")
            return [round(xi, tolerance), error, i + 1]

    print(f"Maximum iterations reached. Approximation: {xi}, rounded to: {round(xi, tolerance)} "
          f"after {i + 1} iterations\n")
    return [round(xi, tolerance), error, i + 1]


def main():
    # 1
    tolerance = 5
    print("\n\nA \n\n")

    print("Bisection")
    for j in range(3):
        print(bisection_method(j, j + 1, tolerance))

    print("\nNewton-Raphson")
    for j in range(3):
        print(newton_raphson_method(j, j + 1, tolerance))

    print("\nSecant")
    for j in range(3):
        print(secant_method(j, j + 1, tolerance))

    # 2

    print("\n\nB\n\n")

    for i in range(10):
        for j in range(3):
            print(bisection_method(j, j + 1, tolerance))

    x = np.linspace(0, 3, 100)
    fig = plt.figure(figsize=(10, 5))
    plt.plot(x, f(x))
    plt.grid()
    plt.axis()
    plt.title("Ex 2")
    plt.show()


    print(f(0), fder1(0), fder2(0))
    return 0


main()
