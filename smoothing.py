#сглаживание методом скользящего среднего
def smt1(array,  k):
    smt = []
    for i in range(len(array)):
        j = 0
        while (i + j < len(array)) and (2 * j < k) and (i - j >= 0):
            j += 1
        smt.append(sum(array[i - j + 1: i + j])/(2 * j - 1))
    return smt

#метод скользящего среднего со скользящим окном наблюдения
def smt2(array, k):
    smt = []
    for i in range(len(array)):
        smt.append(smtFunc(array[:i + 1], k))
    return smt

def smtFunc(array, k):
    while abs(array[-1] - (sum(array) / len(array))) / array[-1] > k:
        array.pop(0)
    return sum(array) / len(array)