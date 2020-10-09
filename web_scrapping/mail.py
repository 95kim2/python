from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def mailYouFile(me, my_password, emails, fileName=None, title='제목 없음', content=''):
    # 로그인하기
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login(me, my_password)

    for you in emails:
        # 메일 기본 정보 설정
        msg = MIMEMultipart('alternative')
        msg['Subject'] = title
        msg['From'] = me
        msg['To'] = you

        # 메일 내용 쓰기
        part2 = MIMEText(content, 'plain')
        msg.attach(part2)

        if fileName != None:
            part = MIMEBase('application', "octet-stream")
            with open(fileName, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=fileName)
            msg.attach(part)

        # 메일 보내고 서버 끄기
        s.sendmail(me, you, msg.as_string())
    s.quit()


def articlesToFile(URL, fileName):
    driver = webdriver.Chrome('./chromedriver')

    from openpyxl import Workbook

    wb = Workbook()
    ws1 = wb.active
    ws1.title = "articles"
    ws1.append(["제목", "링크", "신문사", "썸네일"])

    driver.get(URL)
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')

    articles = soup.select('#rso > div > g-card > div > div > div.dbsr > a')
    for article in articles:
        title = article.find(role='heading').text
        url = article['href']
        comp = article.select_one('div.XTjFC.WF4CUc').text
        thumbnail = article.select_one('div > g-img > img')['src']
        ws1.append([title, url, comp, thumbnail])

    wb.save(filename=fileName)
    driver.quit()

URL = "https://www.google.com/search?biw=810&bih=694&tbm=nws&sxsrf=ALeKk03PU-Rlx3tUQDRR_plq8rCdKO7QNg%3A1602074857477&ei=6bh9X97bHMT_wAPOmKTwCg&q=%EC%9E%90%EC%9C%A8%EC%A3%BC%ED%96%89&oq=%EC%9E%90%EC%9C%A8%EC%A3%BC%ED%96%89&gs_l=psy-ab.3..0l10.2769.2769.0.4152.1.1.0.0.0.0.112.112.0j1.1.0....0...1c.1.64.psy-ab..0.1.112....0.oMXuV05Wp7M"
fileName = 'articles.xlsx'
articlesToFile(URL, fileName)
me = '보내는 사람'
pw = '보내는 사람 비밀번호'
emails = ['받는 사람1', '받는 사람2']
title = 'articles'
content = 'articles'
mailYouFile(me, pw, emails, fileName, title, content)