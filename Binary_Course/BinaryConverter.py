def DecimalToBinary(decimalNum, bits):
    """
    Input:
    decimalNum(int) - an integer which represent a decimal number.
    bits(int) - an integer which represent the amount of bits.

    Output: the function return a the given number as binary number in str using the two's complement.
    """
    decimalNum = 2 ** bits - decimalNum 
    binaryNumberLst = ['0'] * bits
    
    for i in range(bits-1, -1, -1):
        if decimalNum >= 2**i:
            binaryNumberLst[(bits - 1) - i] = '1'
            decimalNum -= 2**i

    return ''.join(binaryNumberLst)

decimalNum = int(input("Enter a positive decimal number: "))
while decimalNum < 0:
    print("The number need to be positive!")
    decimalNum = int(input("Try again: "))

bits = int(input("Enter the amount of bits: "))
while 2**bits <= decimalNum:
    print("This amount of bits isn't enough to represent the given decimal number!")
    bits = int(input("Try again: "))

print(f"The given number: {decimalNum}")
print(f"The binary representation: {DecimalToBinary(decimalNum, bits)}")