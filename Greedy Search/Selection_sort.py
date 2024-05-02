
def selectionSort(array, size):
    iterations = 0  # Initialize a counter for iterations
    for ind in range(size):
        min_index = ind
        for i in range(ind + 1, size):
            iterations += 1  # Increment counter for each comparison
            if array[i] < array[min_index]:
                min_index = i

        array[ind], array[min_index] = array[min_index], array[ind]

    return iterations  # Return the number of iterations

size = int(input("Enter the size of the array: "))
arr = []
print("Enter the elements of the array")
for i in range(size):
    arr.append(int(input()))

iterations = selectionSort(arr, size)

print("The array after sorting is: ")
print(arr)
print("Number of iterations (comparisons):", iterations)
