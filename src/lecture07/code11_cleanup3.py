def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)  # try -> else -> finally


divide(2, 0)  # except ZeroDivisionError -> finally


divide("2", "1")  # unhandled exception
