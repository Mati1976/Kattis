# Creating a dictionary for the conversion

AlphaDict = {
    'a' : '@' ,
    'b' : '8' ,
    'c' : '(' ,
    'd': '|)' ,
    'e' : '3' ,
    'f' : '#' ,
    'g' : '6' ,
    'h' : '[-]' ,
    'i' : '|',
    'j' : '_|' ,
    'k' : '|<' ,
    'l' : '1' ,
    'm' : '[]\/[]' ,
    'n' : '[]\[]' ,
    'o' : '0' ,
    'p' : '|D' ,
    'q' : '(,)' ,
    'r' : '|Z' ,
    's' : '$' ,
    't' : "']['" ,
    'u' : '|_|' ,
    'v' : '\/' ,
    'w' : '\/\/' ,
    'x' : '}{' ,
    'y' : '`/' ,
    'z' : '2',
    }
# Setting up a variable for the converted string
conv = ''
# Reading the string and lowercasing it 
sen = input().lower()

# Iterating over all the characters in teh string 
for i in range(0, len(sen)):
    # checking if our Char is in the dictionary, if true we will use the dictionary to add the converted value to the conv string
    if sen[i] in AlphaDict.keys() :
        conv = conv + AlphaDict[sen[i]]
    # If the value is not in the dictionary we add the original value to the converted string  
    else :
        conv = conv + sen[i]
# printing the converted Value 
print(conv)




    
    
                 
