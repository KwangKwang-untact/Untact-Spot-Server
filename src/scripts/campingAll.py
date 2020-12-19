import requests
import json
import csv

result = list()
with open('./assets/한국관광공사_전국 야영장 등록정보_20190712.csv', 'r') as f:
    datas = csv.reader(f)
    for data in datas:
        print(data)
        if data[2] == "위도":
            continue
        if not int(data[5]) + int(data[6]) + int(data[7]) + int(data[8]) == 0:
            fail = 0
            while True:
                try:
                    if int(data[9]) + int(data[10]) + int(data[11]) < 5:
                        rating = 1
                    elif int(data[9]) + int(data[10]) + int(data[11]) < 10:
                        rating = 2
                    elif int(data[9]) + int(data[10]) + int(data[11]) < 20:
                        rating = 3
                    elif int(data[9]) + int(data[10]) + int(data[11]) < 40:
                        rating = 4
                    else:
                        rating = 5

                    response = requests.get("https://dapi.kakao.com/v2/search/image?query={}".format(data[0]), headers={
                        "Authorization": "KakaoAK 33b6248b144cca3b1c04efcfb742d497"
                    }).json()
                    print({
                        "title": data[0],
                        "detail": data[17] + '\n' + data[18],
                        "address": data[4],
                        "latitude": data[3],
                        "longitude": data[2],
                        "price": "정보 없음",
                        "time": "정보 없음",
                        "facilityRating": rating,
                        "dataTier": 1,
                        "tag": data[1].split(','),
                        "image": [
                            response["documents"][0]["image_url"],
                            response["documents"][1]["image_url"],
                            response["documents"][2]["image_url"]
                        ]
                    })
                    result.append({
                        "title": data[0],
                        "detail": data[17] + '\n' + data[18],
                        "address": data[4],
                        "latitude": data[3],
                        "longitude": data[2],
                        "price": "정보 없음",
                        "time": "정보 없음",
                        "facilityRating": rating,
                        "dataTier": 1,
                        "tag": data[1].split(','),
                        "image": [
                            response["documents"][0]["image_url"],
                            response["documents"][1]["image_url"],
                            response["documents"][2]["image_url"]
                        ]
                    })
                    break
                except Exception as e:
                    if fail > 5:
                        break
                    fail += 1

with open('result_all.json', 'w') as f:
    f.write(json.dumps(result))
    f.close()
