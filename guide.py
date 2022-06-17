import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

# step 1 : get the html
r = requests.get(url)
htmlContent = r.content  # contains all the html of the page
# print(htmlContent)
# step 2 : parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify()) #prettifies the html code

# Step 3: HTML tree traversal
# html tree is like DOM, it's structure and traversal means traveling to different parts of tree/html

# commonly used types of objects:
# 1. tag
# print(type(title))

# 2. NavigableString
# print(type(title.string))

# 3. BeautifulSoup
# print(type(soup))

# 4. Comment
#

title = soup.title  # gets the title tag of the webpage

# get all the paragraph from the page
paras = soup.find_all('p')
# print(paras)

print(soup.find('p'))  # returns the first paragraph tag
print(soup.find('p')['class'])  # returns the class of the paragraph tag

# find elements with class=mt-2
print(soup.find_all("p", class_="mt-2"))

# get text from the tag/soup
print(soup.find('p').get_text())  # returns the class of the paragraph tag


# get all the anchor from the page
anchors = soup.find_all('a')
all_links = set()  # all link is a set that means there will be unique links and will not store same links
# get all the links in the page
for link in anchors:
    if(link.get('href') != '#'):  # now only those link will print which doesn't have href="#"
        linkText = "https://codewithharry.com"+link.get('href') #we need to write https://xyz at the first to get the full link
        all_links.add(link) #adding the links inside the all_links set
        print(linkText)
