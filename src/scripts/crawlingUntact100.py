from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('window-size=1920x1080')
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

link_data = [
    "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=0138a8ef-f507-4162-accd-64a33f65f187", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=fbbb24e9-5d4b-497e-88cf-9fd5efb4f20a", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=ee0c4df9-52cf-4bce-9ba5-e305a1cedf71", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=054833a5-5989-4b6e-81ef-e983d3ad93cd", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=12e2d0aa-f9e1-4f62-966e-bbcf359bc810", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=197e6e5e-b111-4561-9edc-2579205d9151", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=6b57ccdd-4fb8-43ec-b89b-b607a41546e2", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=9aa7f780-1032-43b1-aa9d-12c26b5df4a2", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=a231057b-2633-4550-997b-1d39bf526bd3", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=6a61f74a-9c2c-4784-bc05-a9dc5f933e31", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=abbe0a2e-9e07-498a-bf59-25d71b9c121a", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=23b10bc3-da93-4fce-9335-26ba0e2e61c0", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=5625b954-6822-4098-b69a-4cb7247bb0f3", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=3d7548a8-b98f-4b50-aea8-5c2328219d67", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=9d1a5779-c0be-4476-843c-151b805653ea", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=8ff4bcb5-e404-4329-a6bd-75077bcc8cec", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=a2c8627c-a567-4779-be8d-d5b76e893e46", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=30f0a401-5c26-46c5-9fb7-7d3de7da4056", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=12f740a3-2117-4f4e-a13f-cad34501279b", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=fd224731-0e0c-40c3-937b-96112885dfa3", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=8333f1a9-244c-452c-94c2-fbe51b8e7ca2", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=13941295-50d3-4e80-ae10-31a1975c307e", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=9d73ffc7-751b-4108-82eb-2ce8517d39c9", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=81ab5e52-835e-4fec-bafd-35ea1ab8ee9a", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=ee78a56f-8fb0-421e-b714-b20472df9e00", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=de494a01-4629-4a22-83c4-6f5eab6b2720", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=c8e9f410-3fa4-461a-b205-a41252426b87", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=3732f9d0-1c50-45ef-81d6-0b25a83e86da", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=2117bd9b-c0a4-411e-802d-a71e8e8b122e", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=eb067a02-fb66-4ce3-86cb-8ddf2a8f3925", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=a353db2d-4e96-49d3-a091-7f8c359ca22c", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=52c22f66-eb3d-4a16-8455-692697868b3b", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=9ac39dd9-4dfe-4dc0-866e-b3a98fd581c7", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=098578f0-0c46-4d62-abf9-14d8b8d5149c", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=e0ed82d6-c90c-4618-8c4b-05c5afa33dfb", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=008820e2-13e8-4bc5-93e2-c4d95d0eaf8c", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=811921ac-72c0-4bd6-a239-3c3840b69fe7", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=7eb8f2eb-64f9-4428-9416-2ad85623bff9", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=c8694b54-aea9-4774-b738-f34024d611b4", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=7d4c881c-a326-46fe-9a86-307c1510dab0", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=08631717-270b-4f47-81dc-118de3e709b5", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=735bfed5-2e1c-4c23-aafa-1ba026292c37", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=85abf749-25b0-4278-bda5-7ecdc36873c4", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=247967e0-3742-45bc-af25-e02cecf6784b", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=173f639d-238f-428e-807d-56b7a722f418", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=94eece9c-a5c2-4f91-836b-38f34cc6dd84", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=61ecf913-4f07-4c1a-a8b8-372404a049d0", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=c38c7a51-5b13-480a-856f-1ba0f0947287", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=ff9079dc-2ac1-4ab4-a918-391bc16054a0", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=93eb3111-2ad1-48e4-a957-eec31a6550fb", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=68588e50-6630-49ae-85e1-835c2d594ed1", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=f8a28283-450a-4780-87ee-11cfa82ca56b", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=47f1e913-b022-417f-ba9e-34bcc8dbb54c", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=42e1ba17-6dc5-469f-99d7-e432931f2bea", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=275474f6-667c-4fab-b320-178354891e5c", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=e3f4aab6-4033-4d1d-96aa-7e9f011a2594", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=7f278c5c-3c76-4d9c-8ca5-ad066274795d", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=87e613c6-f7c3-4d3f-8d60-13c2f8166b95", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=cbc679cc-4dae-4f9a-887c-b650912a100e", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=57d81233-696d-44a8-a751-915ee2fc580d", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=fbbda33c-d44a-4dae-ac50-b91ee95d185a", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=04a696be-c97f-4d72-9fb8-59eaf77a79ab", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=49c3a878-05ab-4fdf-84ab-b1d61079ac93", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=9e74f3ec-8591-4c03-a555-c688b1750abe", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=e806f940-9f6f-4110-b5f0-db779cdbff28", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=1dc4a3e7-33f5-463b-9f31-f22838709e73", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=e2910a29-51d3-45f2-b1ae-b6794863d27b", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=3d80c9cb-79d4-461b-b223-697a621322cd", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=8cb6694a-46db-4ac0-927f-cfa5be74b5e0", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=f2cc06fa-0e24-4bde-ad8a-5f044c3b7754", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=3e82a842-f061-4f01-a20e-b06590b47b2e", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=01503d2f-b4b3-46e0-9836-c580cd17bee8", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=52561673-e059-499d-930d-a5698f31a7d0", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=44ab3132-75a4-4179-b1e7-262db516c677", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=c11f92b4-46cd-466a-9875-8b0a6cafec29", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=6c170886-e1bb-42eb-83d7-41ff92ba6132", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=24dc8003-7616-4fcf-870d-0405e1a06543", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=83ec7bcc-bb79-4a18-a094-2163f657d41c", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=369a4dd1-a50d-44f6-8367-5364237a60c1", "https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=c1ecd92e-f3c1-4497-bdef-380a367a3f28"
]
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.implicitly_wait(5)

with open('result.json', 'w') as f:
    json_data = list()
    for tmp_link in link_data:
        failure = 0
        while True:
            try:
                driver.get(tmp_link)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.select('#topTitle')[0].text
                detail = soup.select('.ms_detail > div > div > p')[0].text
                data = soup.select('.inr_wrap > div > ul > li')

                address = ""
                time = ""
                price = ""
                for tmp in data:
                    if tmp.select('strong')[0].text.replace(" ", "") == "주소":
                        address = tmp.select('span')[0].text
                    elif tmp.select('strong')[0].text.replace(" ", "") == "이용시간":
                        time = tmp.select('span')[0].text
                    elif tmp.select('strong')[0].text.replace(" ", "") == "입장료":
                        price = tmp.select('span')[0].text
                print(address)
                if address == "대전 동구 마산동 51-4":
                    break

                response = requests.post("https://dapi.kakao.com/v2/local/search/address.json", headers={
                    "Authorization": "KakaoAK 33b6248b144cca3b1c04efcfb742d497"
                }, data={
                    "query": address
                }).json()
                print(response)
                latitude = response["documents"][0]["address"]["x"]
                longitude = response["documents"][0]["address"]["y"]
                response = requests.get("https://dapi.kakao.com/v2/search/image?query={}".format(title), headers={
                    "Authorization": "KakaoAK 33b6248b144cca3b1c04efcfb742d497"
                }).json()
                image = response["documents"][0]["image_url"]

                json_data.append({
                    "title": title,
                    "detail": detail,
                    "address": address,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": price,
                    "time": time,
                    "image": [
                        response["documents"][0]["image_url"],
                        response["documents"][1]["image_url"],
                        response["documents"][2]["image_url"]
                    ]
                })

                break
            except Exception as e:
                if failure > 5:
                    break
                failure += 1
    f.write(json.dumps(json_data))
    f.close()
