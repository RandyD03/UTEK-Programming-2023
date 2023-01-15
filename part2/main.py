# reading the file in

# CHANGE INPUT FILE HERE
f = open("2c.in", "r")
kingdoms = int(f.readline())
homes = int(f.readline())
inputArray = f.readline().split(" ")
misplacedArray = []
f.close()

# making an array for each home where there is a home and a number to represent its index
# such as [['a1', 0], ['b3', 1], ['b1', 2], ['b2', 3], ['a3', 4], ['c2', 5], ['c1', 6], ['c3', 7], ['a2', 8]]
for i in range(kingdoms * homes):
    misplacedArray.append([inputArray[i], i])

numArray = []

# numArray = array with numbers representing each home
# house represents a pair in the misplacedArray
for home in misplacedArray:
  numArray.append((ord(home[0][0])-97)*homes + int(home[0][1]))

f = open("2c.out", "a")

# our selection sort sorting algorithm
def selectionSort(numArray, misplacedArray, size):
    
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if numArray[j] < numArray[min_index]:
                min_index = j
              
         # swapping the elements to sort the array
        (numArray[i], numArray[min_index]) =(numArray[min_index],numArray[i])
        (misplacedArray[i], misplacedArray[min_index]) = (misplacedArray[min_index],misplacedArray[i])
      
        # print(" swapped " + accArray[i][0] + " and " + accArray[min_index][0])
        if misplacedArray[i][0] != misplacedArray[min_index][0]:
          f.write("Swap " + misplacedArray[i][0] + " and " + misplacedArray[min_index][0] +"\n")

selectionSort(numArray, misplacedArray, len(numArray))
f.close()