c = int(input("Write numbet stars for diamond: "))

"""for i in range(1, c + 1):
    space = c - i
    stars = c + 1
    print(" "* space + "*"*stars)"""

for i in range(1, c + 1):
    space = c - i
    stars = 2 * i - 1
    print(" "* space + "*"*stars)
for i in range(c - 1, 0,-1):
    space = c - i
    stars = 2 * i - 1
    print(" "* space + "*"*stars)