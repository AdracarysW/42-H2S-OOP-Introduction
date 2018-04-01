# #!/usr/bin/env python

# # My program takes in a number in base 10 and prints out its equivalent in base 2 (binary)
# # By awaraich

number = int(input("Enter a number: "))


def operation(num):
    if num > 1:
        operation(num // 2)
    print(num % 2, end='')

def main():
    operation(number)


main()
