#Восстановление апроксимацией
def aprok(s, f, arr):
    k = 0
    if f == len(arr):
        f -= 1
    if arr[f] == None:
        k = arr[s - 1] - arr[s - 2]
        b = arr[s - 1] - k * (s - 1)
    else:
        if s == 0:
            b = arr[f]
        else:
            k = (arr[f] - arr[s - 1]) / (f - s + 1)
            b = arr[s - 1] - k * (s - 1)
    for i in range(s, f):
        if int(k * i + b) >= 0:
            arr[i] = int(k * i + b)
        else:
            arr[i] = 0
    if arr[f] == None:
        arr[f] = int(k * f + b)

def aprokRest(array):
    i = 0
    s = 0
    f = 0
    while i < len(array):
        while i < len(array) and array[i] == None:
            i += 1
            f = i
        if s != f:
            aprok(s, f, array)
        i += 1
        s = i
        f = i
    return array

#Винзорирование
def venz(array):
    for i in range(len(array)):
        while array[i] == None:
            n = array[i-1]
            array[i] = n
    return array