from bs4 import BeautifulSoup
import requests

#request the website for its html page n it is fected into the program using the get method
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
content = requests.get(url) #this is just a class n it gives u response of connection (its like this: <class 'requests.models.Response'>)
#content.text --> (here well get the whole html doc) wt v did here is to ask the class(response) to give us text out of it 
doc = BeautifulSoup(content.text,"html.parser")
# print(doc.prettify())

prices = doc.find_all(text='$') #price will be written with the symbol $ so we took that as refence 
first = prices[0].parent #we get just the list of $ symbols from above line, soo we fetch the whole line using
jk= first.find_all("strong")
print(jk[0].string)