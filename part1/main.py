# CHANGE INPUT FILE HERE
f = open("1c.in", "r")

kingdoms = int(f.readline())
homes = int(f.readline())
inputArray = f.readline().split(" ")
misplacedArray = [] # array to store all misplaced homes
f.close()

for i in range(kingdoms * homes):
    currentNum = int((ord(inputArray[i][0]) - ord('a'))) + 1
   
    if not (i < (currentNum * homes) and i >= ((currentNum - 1) * homes)):
        misplacedArray.append([inputArray[i], i]) 

f = open("1c.out", "a")

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
            break
          elif (checknum2):
            f.write("Swap " + misplacedArray[i][0] + " and " + misplacedArray[j][0] + "\n")
            booleanArray[i] = True
            oneSwap = True
            temp = misplacedArray[i][1]
            misplacedArray[i][1] = misplacedArray[j][1]
            misplacedArray[j][1] = temp
            break
  # condition check,  sees if the array is done sorting completely, otherwise redo process      
  whileCondition = True
  for i in range(len(booleanArray)):
    if(booleanArray[i] == False):
      whileCondition = False

f.close()
      