def hex_to_int(hex):
    
    result = 0 
    for i in range (len(hex) - 1, -1, -1):
        value = None
        if hex[i].capitalize() == 'A':
            value = 10
        elif hex[i].capitalize() == 'B':
            value = 11
        elif hex[i].capitalize() == 'C':
            value = 12
        elif hex[i].capitalize() == 'D':
            value = 13
        elif hex[i].capitalize() == 'E':
            value = 14
        elif hex[i].capitalize() == 'F':
            value = 15
        else:
            value = int(hex[i])

        result += value * (16 ** (len(hex) - 1 - i))

    return result

if __name__ == '__main__':
    print("FFF - " +  str(hex_to_int("FFF")))
    print("90 - " +  str(hex_to_int("90")))
    print("AF8 - " +  str(hex_to_int("AF8")))
    print("F - " +  str(hex_to_int("F")))
    print("10 - " +  str(hex_to_int("10")))
