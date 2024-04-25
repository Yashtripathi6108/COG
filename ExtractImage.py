import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

class Extract_Image():

    def __init__(self, url = ""):
        self.url = url 

    def set_url(self, url):
        self.url = url

    def get_image(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        image_tags = soup.find_all('img')
        image_tags = [img.get('src') for img in image_tags]
        for img_url in image_tags: 
            try:
                if img_url.find('rukminim2.flixcart.com') == -1:
                    continue
                else :
                    start_index = img_url.find("/image/") + len("/image/")
                    mid_index = img_url.find("/", start_index) 
                    end_index = img_url.find("/", mid_index+1)

                    img_url = img_url[:start_index] + "500/500" + img_url[end_index:]
                    response = requests.get(img_url)
                    im = Image.open(BytesIO(response.content))
                    image_height = 200
                    im.resize((int(im.width * (image_height / im.height)), image_height))
                    return im
            except:
                pass
        return None