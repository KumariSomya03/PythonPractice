# name=input("enter name : ")
# print(f"Good Afternoon, {name}")  #formatting string


letter='''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Somya").replace("<|Date|>","16 November 2028"))