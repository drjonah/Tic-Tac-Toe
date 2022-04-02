from asyncio.format_helpers import _format_callback_source


def factorial(number):

    if number < 0:
        return "NA"

    if number < 1:
        return 1

    else:
        return number * factorial(number-1)

print(factorial(3))