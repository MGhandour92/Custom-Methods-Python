'''
# Custom Find Fuction
    Build a Function that takes an input string and Character 
    and returns the Index of everytime that Character Appears 
    e.g. 

    Input : 'abcabcabc' , 'c' 

    Output :[2,5,8]
'''

def customFind (str1,chr1):
    lst =[]
    #loop through the string characters
    for c in range(0,len(str1)):
        # if the charcter in the loop equals to the parameter
        if str1[c] == chr1:
            #append to the list
            lst.append(c)
    return lst

#customFind('abcabcabc','c')

#================================================================

'''
# Custom Split Function

    Build a Customized Split Function with **two Options **
    ---
    > ***Option One :*** Splitting at first Occurance Only

    Input: 'Abo Khayria byslem 3lyk', 'b'

    Output :  ['A','o Khayria byslem 3lyk']
    ---
    > ***Option two :*** Splitting  Every time the Character Appears

    Input: 'Abo Khayria byslem 3lyk', 'b'

    Output :  ['A','o Khayria ','yslem 3lyk']
'''

def customSplit(s, c, opt):
    splitted = []
    tmpText = ''
    counter = 0

    #user choose the option 1 or 2

    if opt == 1:
        #loop through the string
        for x in s:            
            #use counter when the cursor equals to the string
            if x == c and counter != 1:
                counter +=1
                #append the previous characters (saved at the temp variable)
                splitted.append(tmpText)
                #empty the temp
                tmpText = ''
            else: #if still not found the character keep saving the old text in temp varaible
                tmpText += x

        if tmpText: #if temp if not empty append the rest of temp to the array 
            splitted.append(tmpText)

    elif opt == 2:
        #same idea, except you will not use the counter
        #because you need it once not multiple
        for x in s:
            if x == c:
                splitted.append(tmpText)
                tmpText = ''
            else:
                tmpText += x
        if tmpText:
            splitted.append(tmpText)

    return splitted

# print(customSplit('Abo Khayria byslem 3lyk', 'b', 1))
# print(customSplit('Abo Khayria byslem 3lyk', 'b', 2))

#=========================================================

'''
# Bulk Rename Function
    Rename all the files in a directory with specific text
'''
import os

def renameFiles(pathStr, renameTxt):
    i = 0
    #list all the files in the directory
    for f in os.listdir(pathStr):
        #build file name
        name = renameTxt + str(i)+".txt"
        #rename files
        os.rename(pathStr + f, pathStr + name)
        i += 1


#renameFiles("E:\\GIT\\AI-Course-Python\\Published\\Custom-Methods-Python\\03- Bulk Rename Function\\testOSlib", "test")
