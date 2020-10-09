import dload
from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import base64, re
from io import BytesIO
import time

# data:image ~~~/base64 포맷의 이미지 url로부터 이미지를 다운 받는다.
def getI420FromBase64(codec, i):
    base64_data = re.sub('^data:image/.+;base64,', '', codec)
    print('func: ' + base64_data)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    img.save(f'./imgs_homework/{i}.jpg')

#selenium의 webdriver를 쓰려면 브라우저에 맞는 드라이버를 이 코드의 파일과 같은 위치에 설치해야 한다.
#크롬의 경우, 크롬드라이버 설치
driver = webdriver.Chrome('chromedriver')
driver.get("https://www.google.com/search?q=%EC%83%81%EA%B7%BC%EC%9D%B4&hl=en&sxsrf=ALeKk02oPYTjuVXMoR1Mp82WXhWw7V2XWw:1601537412851&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiFm9nk75LsAhVGCqYKHV4MBnEQ_AUoAXoECBEQAw&biw=958&bih=927")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

i = 1
#스크랩핑할 정보 우클릭 후, copy->copy selector를 통해 경로를 복사해서 select에 붙여 넣으면 해당 태그를 뽑아낸다.
#select_one은 하나의 태그, select는 여러개의 태그
images = soup.select('#islrg > div.islrc > div > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir > img')
for image in images:
    if image.has_attr('src'):
        url = image["src"]
    else:
        url = image["data-src"]

    if url[0:4] == "data":
#        print('data: ' + url)
        getI420FromBase64(url, i)
    else:
#        print('http: ' + url)
        dload.save(url, f'./imgs_homework/{i}.jpg')
    i += 1
driver.quit() # 끝나면 닫아주기

