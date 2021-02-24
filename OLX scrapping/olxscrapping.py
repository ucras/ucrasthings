from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.olx.pt/tecnologia-e-informatica/computadores-informatica/componentes/odivelas-lisboa/?search%5Bfilter_enum_tipo%5D%5B0%5D=placas-graficas&search%5Bdist%5D=50"

# opening up connection, grabbing the page2
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# hmtl parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class":"offer-wrapper"})

filename = "gpu.csv"
f = open(filename, "w")

headers = "title, price\n"

f.write(headers)
#print(len(containers))

for container in containers[:15]:    # only collects the last 14 gpus
    title_container = container.findAll("a", {"data-cy":"listing-ad-title"})
    title = title_container[0].text.strip()

    price_container = container.findAll("p", {"class":"price"})
    price = price_container[0].text.strip()

    f.write(title.replace(",", ".") + "," + price.replace(",", "-").replace(".", " ") + "\n")

f.close()
