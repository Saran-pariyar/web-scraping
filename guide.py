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


#get tag with id = "navbarSupportedContent"
navbarSupportedContent = soup.find(id="navbarSupportedContent")
print(navbarSupportedContent)
#print the tag's children
print(navbarSupportedContent.children())

#print it's content (tags, text,etc)
# print(navbarSupportedContent.contents)

#print content in formatted way
for elem in navbarSupportedContent.contents:
    print(elem)

#   .content and .children are almost same thing with few differences

#print text inside the tag
for elem in navbarSupportedContent.string:
    print(elem)

#print text inside the tag in listed order
for elem in navbarSupportedContent.stripped_strings:
    print(elem)

#print(navbarSupportedContent.parent) #prints the parent

#print(navbarSupportedContent.parents) #prints the parents and we have to iterate it using loop
for items in navbarSupportedContent.parents:
    print(items.name)#prints name of body tag, html tag, all parent tag


# print(navbarSupportedContent.next_sibling) #prints next sibling 
# print(navbarSupportedContent.previous_sibling) #prints previous sibling 

#we can print it multiple times 
# print(navbarSupportedContent.previous_sibling.previous_sibling)

#Explore beautifulSoup yourself more!!!