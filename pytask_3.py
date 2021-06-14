from bs4 import*
import requests as rq
import os

request1 = rq.get("https://www.pinterest.com/ehsmith2001/toms-bedroom-aesthetic/")
soup1 = BeautifulSoup(request1.text, "html.parser")

links = []

rs1 = soup1.select("img[src^='https://i.pinimg.com/236x']")

for jpg in rs1:
    links.append(jpg['src'])

os.mkdir('pin_jpg')
i = 1
for index, img_link in enumerate(links):
    if i <= 10:
        img_data = rq.get(img_link).content
        with open("pin_jpg/"+str(index+1)+'.png', 'wb+') as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
        break
