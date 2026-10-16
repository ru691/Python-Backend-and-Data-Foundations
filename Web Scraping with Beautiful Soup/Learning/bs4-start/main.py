from bs4 import BeautifulSoup
# import lxml (alternative way instead of html.parser)

with open("website.html") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
# print(soup.title) - GET THE WHOLE TITLE LINE
# print(soup.title.name) - GET THE NAME "TITLE"
# print(soup.title.string) - GET THE NAME INSIDE TITLE
# print(soup.prettify()) - HELP YOU INDENT THE LINES TO MAKE IT NEATER
# print(soup.a) - GIVE US THE FIRST <a it finds
# print(soup.li) - GIVE US THE FIRST <li> it finds
# print(soup.p) - GIVE US THE FIRST <p> it finds

all_anchors = soup.find_all("a") # - GIVE US ALL <a it finds

# to get the anchor text name
for anchor in all_anchors:
    print(anchor.text)
    # print(anchor.getText()) both is the same
    print(anchor.get("href")) # to get the links instead of the tags

heading = soup.find(name = "h1", id = "name") #to get a specific element
print(heading)

section_heading = soup.find(name = "h3", class_ = "heading") #use to get specific element, we do not use class but
                                                             #class_ instead
print(section_heading.getText()) #get the text of that line

company_url = soup.select_one(selector = "p a") # p = paragraph, a = anchor tag, "p a" = find the anchor tag sitting
                                                #inside the paragraph
print(company_url)

name = soup.select_one(selector = "#name") #find the name element, must use #
print(name.getText())

headings = soup.select(".heading") #select all element with headings, we must use .heading
print(headings)