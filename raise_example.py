"""
*********
*       *
*       *
*********

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a single character!')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater than 1!')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)

    print(symbol * width)

#boxPrint('**', 15, 5)
