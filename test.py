array = [1,5,6,9,5,3,1,5]

def func1(arr):
    return arr[0] + arr[-1]

print(func1(array))

def func2(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(func2(array))

def func3(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                print(arr[i], arr[j])

print(func3(array))

def func4(arr):
    arr.sort()
    for element in arr:
        print(element)

func4(array)