'''
This is an implementation of a simple regex parser

This Regex only supports two special characters
  * - none or many
  + - one or many

Examples of input:
  a*bcd
  abcde+
  abbc*d+e
'''

ONE_OR_MANY = '+'
NONE_OR_MANY = '*'


def matches(regex, s):
    regex_len = len(regex)
    str_len = len(s)
    regex_idx = 0
    str_idx = 0

    if regex_len == 0:
        return str_len == 0

    if regex_len == 1:
        return str_len == 1 and regex[0] == s[0]

    if regex[1] == ONE_OR_MANY:
        # Change to none or many moving forward so as not to get caught
        return str_len > 0 and regex[0] == s[0] and matches(regex[0] + '*' + regex[2:], s[1:])

    elif regex[1] == NONE_OR_MANY:
        return (str_len > 0 and regex[0] == s[0] and matches(regex, s[1:])) or matches(regex[2:], s)

    else:
        return str_len > 0 and regex[0] == s[0] and matches(regex[1:], s[1:])


if __name__ == '__main__':
    print("Testing Simple Regex...")

    print("a*bcd, abcd - " + str(matches("a*bcd", "abcd")))
    print("a*bcd, aaabcd - " + str(matches("a*bcd", "aaabcd")))
    print("a*bcd, bcd - " + str(matches("a*bcd", "bcd")))
    print("a*bcd, dbcd - " + str(matches("a*bcd", "dbcd")))
    print("a+bcd, bcd - " + str(matches("a+bcd", "bcd")))
    print("a+bcd, abcd - " + str(matches("a+bcd", "abcd")))
    print("a+bcd, aaabcd - " + str(matches("a+bcd", "aaabcd")))
