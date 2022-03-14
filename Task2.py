import numpy as np

def generation(line):
    arr = np.fromiter([True if i == '1' else False for i in line], dtype=np.bool)
    arr2 = np.fromiter([True if i == '1' else False for i in line], dtype=np.bool)
    for i in range(10):
        for j in range(-1, arr.size - 1):
            if i % 2 == 0:
                a = arr[j - 1]
                b = arr[j]
                c = arr[j + 1]
                if not a and not b and not c or a and not b and c or a and b and not c or a and b and c:
                    arr2[j] = False
                else:
                    arr2[j] = True
            else:
                a = arr2[j - 1]
                b = arr2[j]
                c = arr2[j + 1]
                if not a and not b and not c or a and not b and c or a and b and not c or a and b and c:
                    arr[j] = False
                else:
                    arr[j] = True
    return ''.join(['1' if x else '0' for x in arr])

print(generation("00000000000000100000000000000"))