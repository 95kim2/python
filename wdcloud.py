import matplotlib.font_manager as fm
import numpy as np
from wordcloud import WordCloud
from PIL import Image
# 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

#https://s3.ap-northeast-2.amazonaws.com/materials.spartacodingclub.kr/free/cloud.png

text = ''
text2 = ''
text3 = ''
with open("kakaoTalkChats.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        idx = line.find(',')
        if idx == -1:
            continue
        elif line[idx-3] != ':':
            continue
        idx = line.find(' : ')
        text += line[idx+3:]
        if line[idx+3:] != "이모티콘\n" and line[idx+3:] != "사진\n":
            text2 += line[idx+3:]
        text3 += line[idx+3:].replace('삭제된 메지입니다.\n','').replace('이모티콘\n', '').replace('ㅇㅋ','').replace('ㅇㅇ','').replace('ㅠ','').replace('ㅋ','').replace('사진\n','')
print(text2)

font_path = 'c:/System/Library/Fonts/AppleSDGothicNeo.ttc'

mask = np.array(Image.open('./cloud.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)#width=600, height=400)
wc.generate(text)
wc.to_file("result.png")
wc.generate(text2)
wc.to_file("result2.png")
wc.generate(text3)
wc.to_file("result3.png")
