import re

text = input("text=")
word = input("word=")

x = re.findall(word,text)
print("count=",len(x))