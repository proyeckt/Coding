#Edwin Alejandro Turizo Prieto

def calculateNGrams(text,n):
    array=[]
    length=len(text) #Length of text

    if(n<1 or n>length): #Edge cases
        return array #Return empty array

    #Time complexity: O(N), where N=(n-length)+1, it is the ecuation for the number of iterations for loop
    for i in range(0,abs(n-length)+1):
        subtext=text[i:n]
        array.append(subtext)
        n+=1
    return array

def mostFrequentNGram(text,n):

    #Time complexity: O(N), where N=(n-length)+1, it is the ecuation for the number of iterations for loop
    nGram=calculateNGrams(text,n) #Create n-Gram with first function

    if nGram: #Validate nGram array
        #Time Complexity O(N) where N is the length of Ngram array
        maxValues=[nGram.count(value) for value in nGram] #Count the frequency of all numbers in array

        word = nGram[maxValues.index(max(maxValues))] #Calculate max in counts of Ngram values and find the index to access value
        return word
    return None

#Step 1
text="Slang"
n=3
nGram=calculateNGrams(text, n) #Basic function (Step 1)
print(nGram)

#Step 2
text2="to be or not to be"
n=2
nGram=mostFrequentNGram(text2, n) #Extended function (Step 2)
print(nGram)
