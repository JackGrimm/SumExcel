import re

def subset_sum(numbers, target, answer, leeway, partial=[]):
    #where the magic happens, recursively splitting the combination list down and seeing if it adds up to the target
    s = sum(partial) #check if the partial sum is equals to target
    if (s >= target -leeway and s <= target +leeway):
        answer.append(partial)
    if s >= target:
        return answer #if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, answer, leeway, partial + [n])#recursively call down the sections

def Calculations(inlist, goalnum, roundnum=0.0): #string of numbers to make up goal, goal, rounding. All in str format.
    #Example Input: Calculations("1.0,2,3.1,4,5,6,","10","0.5")
    #Output: [[1.0, 2.0, 3.1, 4.0], [1.0, 3.1, 6.0], [1.0, 4.0, 5.0], [2.0, 3.1, 5.0], [4.0, 6.0]]
    try:
        inputarray = re.sub(r'\s', '', inlist).split(',')#get rid of all white space characters, specifically for copying from excel.
    except Exception as e:
        return (["Invalid list data. Ensure that the numbers are in General or Accounting Format, seperated by a comma.","Error: %s" %(e)])
    inputarray.sort() #lowest to highest. This helps cut time when adding them together to find the goal
    try:
        inputgoal = float(re.sub(r'\s', '', goalnum)) #cleaning the goal, incase numbers contain spaces. Again weird excel format happen.
    except Exception as e:
        return (["Invalid goal data. Ensure that the number is in General or Accounting Format.","Error: %s." %(e)])

    numbers = [] #setup for the final return arrays
    answer = []
    if (roundnum == ""): #if no leeway is given, use 0.0
        leeway=0.0
    else:
        try: leeway = abs(float(roundnum)) #try make it a float. Keeping it positive doesn't make a difference, but it's nice for consitency
        except Exception as e:
            return (["Invalid accuracy data. Ensure that the number is in General or Accounting Format.","Error: %s" %(e)])

    reversed = False
    #a bit of extra work, but keeping the goal positive saves time in the recursive calculations.
    if inputgoal < 0:
        inputgoal = -inputgoal
        reversed = True

    for row in inputarray:
        if row != "":
            try:
                if float(row) != 0.0:
                    if reversed == True:
                        numbers.append(-(float(row))) #reverse the numbers that add up to the goal.
                        numbers.sort()
                    else:
                        numbers.append(float(row))
            except Exception as e:
                return (["Invalid list data. Ensure that the numbers are in General or Accounting Format, seperated by a comma.","Error: %s" %(e)])
    subset_sum(numbers, inputgoal, answer, leeway)
    if reversed == True: #If the numbers were reversed, we need to switch everything back.
        inputgoal = -inputgoal
        tempnum = []
        tempans = []
        temprow = []
        for row in numbers:
            tempnum.append(-row)
        try:
            for row in answer:
                temprow = []
                for ind in row:
                    temprow.append(-ind)
                tempans.append(temprow)
        except Exception as e:
            return ["There are no numbers that add up to the total. Try increasing the accuracy by 1 or more in case of rounding errors."]
        answer = tempans
        numbers = tempnum
    returnlist = []

    if len(answer) == 0:
        returnlist = ["There are no numbers that add up to the total. Try increasing the accuracy by 1 or more in case of rounding errors."]
    else:
        for i in range(len(answer)):
            returnlist.append(answer[i])
    return (returnlist)

