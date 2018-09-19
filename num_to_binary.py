def num_to_binary(num):

    binary = ""
    while num > 0:
        binary += str(num % 2)
        num = int(num / 2)

    return binary


if __name__ == '__main__':
    print(num_to_binary(1))
    print(num_to_binary(9))
    print(num_to_binary(1234))
    print(num_to_binary(15))
    print(num_to_binary(255))
