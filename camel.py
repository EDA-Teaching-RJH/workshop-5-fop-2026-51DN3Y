def main():
    camel_case = input("Input Camel Case: ")
    snake = camel_to_snake(camel_case)
    print(snake)


def camel_to_snake(text):
    snake = ""
    for c in text:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    return snake


main()
