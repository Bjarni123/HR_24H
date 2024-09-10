def decimal_to_binary(nr):
    if nr == 0:
        return '0'
    binaryvaluereversed = ''
    while nr != 0:
        bit = nr % 2
        nr =  nr // 2
        binaryvaluereversed += str(bit)
    return binaryvaluereversed[::-1]


