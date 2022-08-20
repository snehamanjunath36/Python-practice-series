from bs4 import BeautifulSoup
# open the html file in read mode
with open("dummy.html" , "r") as f:
    #to parse the document
    doc = BeautifulSoup(f,"html.parser")


print(doc.prettify()) #to print the contents of the doc in a prettified(indented) manner

#getting element tag which appears first in the document
r = doc.find("p") # to get first ele from this tag
print(r) #prints the whole line as it is along with the tag
print(r.string) #to print only the content of the tag selected  

#getting all element tags which appears in the document
r = doc.find_all("p") #finds all p tags in stores in r in the form of list
print(r)
res = r[1] #accessing specefic ele from the above list

#accessing tags inside another tag using nested strategy
nes = res.find_all("i") # accessing i tag from the res i.e from the p tag
df = nes[1].find_all("b") #accessing b tag from the nes 
print(df)

# changing the string val in html doc
df[0].string = "sggsg"
print(doc.prettify())