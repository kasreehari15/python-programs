str1=input("Enter a string")
consonants=0
vowels=0
for i in str1:
    if i in 'AEIOUaeiou':
        vowels+=1
    else:
        consonants+=1
print("number of vowels are",vowels)
print("number of consonants are",consonants)  
