#1. we run part 2 but only if swap perfectly puts both ppl home
#2. next, run part 1
#3. sort each subkingdom with part 2

# CHANGE INPUT FILE HERE
f = open("3c.in", "r")

kingdoms = int(f.readline())
homes = int(f.readline())
inputArray = f.readline().split(" ")
pairArray = []
# print(kingdoms)
# print(homes)
# print(inputArray)
f.close()

for i in range(kingdoms * homes):
    pairArray.append([inputArray[i], i])

# print(pairArray)

numArray = []


#stores the cost of the total moves
cost = 0

# numArray = array with numbers representing each home
for house in pairArray:
  # print(ord(house[0][0])) 
  numArray.append((ord(house[0][0])-97)*homes + int(house[0][1]))
# print(numArray)

f = open("3c.out", "a")

#sorting algorithm
def perfectSelectionSort(numArray, accArray, size, cost):
    
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if numArray[j] < numArray[min_index]:
                min_index = j
         # swapping the elements to sort the array
        if numArray[min_index] == i + 1: #if the things we swap result in perfect placement for both
          (numArray[i], numArray[min_index]) = (numArray[min_index],numArray[i])
          (accArray[i], accArray[min_index]) = (accArray[min_index],accArray[i])
        # print(" swapped " + accArray[i][0] + " and " + accArray[min_index][0])
          if accArray[i][0] != accArray[min_index][0]:
            f.write("Swap " + accArray[i][0] + " and " + accArray[min_index][0] +"\n")
            cost += 5
            
    retList = [cost, accArray]
    return retList

def part1wcost(kingdoms, homes, inputArray,  runningCost):
  returnArray = inputArray
  misplacedArray = []
  currentCost = runningCost;
  
  for i in range(kingdoms * homes):
      currentNum = int((ord(inputArray[i][0][0]) - ord('a'))) + 1
     
      if not (i < (currentNum * homes) and i >= ((currentNum - 1) * homes)):
          misplacedArray.append([inputArray[i][0], i]) 
  
  booleanArray = [False] * len(misplacedArray) # array to keep track of misplaced homes that get swapped into their right kingdom
  
  whileCondition = False
  while whileCondition == False: # while a misplaced home still exists, run
    for i in range(len(misplacedArray)):
      # Bottom three lines calculate a range for which the first index is valid (ex, 0 - a - 2)
      regionNumI = int((ord(misplacedArray[i][0][0]) - ord('a'))) 
      num1higher = (regionNumI + 1) * homes 
      num1lower = regionNumI * homes
      for j in range(len(misplacedArray)):
        # Similar code as before, but for the second pair index, also making sure j > i to not double up
        regionNumJ = int((ord(misplacedArray[j][0][0]) - ord('a')))
        if(j > i):
          if(booleanArray[i] == False and booleanArray[j] == False):
            num2higher = (regionNumJ + 1) * homes
            num2lower = regionNumJ * homes
        
            checknum1 = False
            checknum2 = False
            if(int(misplacedArray[i][1]) >= num2lower and misplacedArray[i][1] < num2higher):
              checknum1 = True
            if(int(misplacedArray[j][1]) >= num1lower and misplacedArray[j][1] < num1higher):
              checknum2 = True
            if(checknum1 and checknum2): #check to see if the swap results in both homes being placed in the right kingdom
              f.write("Swap " + misplacedArray[i][0] + " and " + misplacedArray[j][0] + "\n")
              booleanArray[i] = True
              booleanArray[j] = True
              temp = misplacedArray[i][1]
              misplacedArray[i][1] = misplacedArray[j][1]
              misplacedArray[j][1] = temp
              #Code to swap items in array for  return and add cost for return
              currentCost += 5
              temp = returnArray[i]
              returnArray[j]  = returnArray[j]
              returnArray[i] = temp
  
    # one swap only allows one swap that benefits just one pair, and then goes back to checking for mutually beneficial pairs above. Rest of loop is similar until the end
    oneSwap = False
    for i in range(len(misplacedArray)):
      if(oneSwap == False):
        regionNumI = int((ord(misplacedArray[i][0][0]) - ord('a')))
        num1higher = (regionNumI + 1) * homes
        num1lower = regionNumI * homes
        for j in range(i+1, len(misplacedArray)):
          regionNumJ = int((ord(misplacedArray[j][0][0]) - ord('a')))
          if(booleanArray[i] == False and booleanArray[j] == False):
            num2higher = (regionNumJ + 1) * homes
            num2lower = regionNumJ * homes
    
            checknum1 = False
            checknum2 = False
            
            if(int(misplacedArray[i][1]) >= num2lower and int(misplacedArray[i][1]) < num2higher):
              checknum1 = True 
            if(int(misplacedArray[j][1]) >= num1lower and int(misplacedArray[j][1]) < num1higher):
              checknum2 = True
  
            # Checks if either one is a valid switch, then makes it
            # Swaps and sets only one of them to true, indicating only one pair benefitted from swap
            if (checknum1):
              f.write("Swap " + misplacedArray[i][0] + " and " + misplacedArray[j][0] + "\n")
              booleanArray[j] = True
              oneSwap = True
              temp = misplacedArray[i][1]
              misplacedArray[i][1] = misplacedArray[j][1]
              misplacedArray[j][1] = temp

              #Code to swap items in array for  return and add cost for return
              currentCost += 10
              temp = returnArray[i]
              returnArray[j]  = returnArray[j]
              returnArray[i] = temp

              
              break
            elif (checknum2):
              f.write("Swap " + misplacedArray[i][0] + " and " + misplacedArray[j][0] + "\n")
              booleanArray[i] = True
              oneSwap = True
              temp = misplacedArray[i][1]
              misplacedArray[i][1] = misplacedArray[j][1]
              misplacedArray[j][1] = temp
              
              #Code to swap items in array for  return and add cost for return
              currentCost += 10
              temp = returnArray[i]
              returnArray[j]  = returnArray[j]
              returnArray[i] = temp
              
              break
    # condition check,  sees if the array is done sorting completely, otherwise redo process      
    whileCondition = True
    for i in range(len(booleanArray)):
      if(booleanArray[i] == False):
        whileCondition = False

  #Package cost and new array for use later
  retList = [currentCost, returnArray]
  return retList

def selectionSort(numArray, misplacedArray, size, cost):
    
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if numArray[j] < numArray[min_index]:
                min_index = j
              
         # swapping the elements to sort the array
        (numArray[i], numArray[min_index]) = (numArray[min_index],numArray[i])
        (misplacedArray[i], misplacedArray[min_index]) = (misplacedArray[min_index],misplacedArray[i])
      
        # print(" swapped " + accArray[i][0] + " and " + accArray[min_index][0])
        if misplacedArray[i][0] != misplacedArray[min_index][0]:
          f.write("Swap " + misplacedArray[i][0] + " and " + misplacedArray[min_index][0] +"\n")
          cost += 5
    retList = [cost, misplacedArray]
    return retList

#run 1.
tempList = perfectSelectionSort(numArray, pairArray, len(numArray), cost)
cost = tempList[0]
pairArray = tempList[1]

#run 2,
tempList = part1wcost(kingdoms, homes, pairArray, cost)
cost = tempList[0]
pairArray= tempList[1]

#run 3
tempList = selectionSort(numArray, pairArray, len(numArray), cost)
cost = tempList[0]
pairArray = tempList[1]

f.write(str(cost))
f.close()
