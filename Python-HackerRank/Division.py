# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division, a // b.
# The second line should contain the result of float division, a / b.
# No rounding or formatting is necessary.

if __name__ == '__main__':
    def division_integer(a, b):
        return a//b
    
    def division_float(a, b):
        return a/b
    
    a = int(input())
    b = int(input())

    
    print(division_integer(a, b))
    print(division_float(a, b))