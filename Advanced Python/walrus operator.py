"""The walrus operator (:=), introduced in Python 3.8, allows you to assign values to
variables as part of an expression"""
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")