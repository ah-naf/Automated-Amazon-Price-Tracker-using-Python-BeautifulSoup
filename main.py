from bs4 import BeautifulSoup
import requests
import smtplib

params = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"

}

url = "https://www.amazon.com/TCL-32-720p-ROKU-Smart/dp/B088S3V3R4/ref=sr_1_2?dchild=1&field-shipping_option-bin=3242350011&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=85a9188d-dbd5-424e-9512-339a1227d37c&pf_rd_r=T56SC61TRMDZ3T89AJ80&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1622047411&rnid=1266092011&s=electronics&sr=1-2&th=1"
response = requests.get(url, headers=params)

soup = BeautifulSoup(response.text, "html.parser")

data = soup.find_all(name='span', class_="p13n-sc-price")
price = (float(data[1].string.split("$")[1]))

title =soup.find(id="productTitle").string.strip()


BUY_PRICE = 150

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login("ahnafhasanshifat@gmail.com", "Allah.....blessme01817711262")
        
        connection.sendmail(
            from_addr="ahnafhasanshifat@gmail.com",
            to_addrs="ahnafhasanshifat@gmail.com",
            msg=f"Subject: Price Alert!!\n\n{message}\n{url}"
        )
