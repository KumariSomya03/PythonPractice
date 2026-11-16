name="Somya Kumari"
print(len(name)) #length of string
print(name.endswith("ya"))
print(name.startswith("so"))
print(name.capitalize())
print(name.replace("Somya","shiela"))
print(name.find("my"))  #returns index
print(name.upper())
print(name.lower())
print(name.title())


text="   Python    "
print(text.strip())   #removes space from both ends
print(text.lstrip())  #removes space from left end
print(text.rstrip())  #removes space from right end


city="Greater Noida"
print(city.count("a")) #counts the number occuerence of character
print(city.split())    #string->list
print(" ".join(city))  #joins elements in string