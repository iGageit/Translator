# Turning each vowel into a G
# You can use this type of program to change any letter or word into any other word. 


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
          #keep the data uppercase if user types in uppercase letters. 
          if letter.isupper():
            translation = translation + "G"
          else: 
            translation = translation + "g"
        else: 
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))
