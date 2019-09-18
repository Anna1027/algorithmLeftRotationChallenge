array = [1,2,3,4,5]

dvalue = 4

def rotate(a,d):
    return a[d:]+ a[:d]

print(rotate(array, dvalue))
