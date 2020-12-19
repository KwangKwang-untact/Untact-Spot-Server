import json
import requests

result = list()

with open("./assets/전국 차박 명소.kml", "r") as f:
    data = f.readlines()
    title = None
    tmp = list()
    for i in range(len(data)):
        if "<name>" in data[i]:
            if not tmp == []:
                fail = 0
                while True:
                    try:
                        address = tmp[0]
                        response = requests.post("https://dapi.kakao.com/v2/local/search/address.json", headers={
                            "Authorization": "KakaoAK 33b6248b144cca3b1c04efcfb742d497"
                        }, data={
                            "query": address
                        }).json()
                        latitude = response["documents"][0]["address"]["x"]
                        longitude = response["documents"][0]["address"]["y"]

                        cnt = 0
                        for t in tmp[1:]:
                            if t == "사용가능":
                                cnt += 1

                        response = requests.get("https://dapi.kakao.com/v2/search/image?query={}".format(title), headers={
                            "Authorization": "KakaoAK 33b6248b144cca3b1c04efcfb742d497"
                        }).json()

                        print({
                            "title": title,
                            "detail": title,
                            "address": address,
                            "latitude": latitude,
                            "longitude": longitude,
                            "price": "정보 없음",
                            "time": "정보 없음",
                            "facilityRating": 1 + cnt,
                            "dataTier": 3,
                            "tag": ["차박"],
                            "image": [
                                response["documents"][0]["image_url"],
                                response["documents"][1]["image_url"],
                                response["documents"][2]["image_url"]
                            ]
                        })
                        result.append({
                            "title": title,
                            "detail": title,
                            "address": address,
                            "latitude": latitude,
                            "longitude": longitude,
                            "price": "정보 없음",
                            "time": "정보 없음",
                            "facilityRating": 1 + cnt,
                            "dataTier": 3,
                            "tag": ["차박"],
                            "image": [
                                response["documents"][0]["image_url"],
                                response["documents"][1]["image_url"],
                                response["documents"][2]["image_url"]
                            ]
                        })
                        break
                    except Exception as e:
                        if fail < 5:
                            break
                        fail += 1
            tmp = list()
            title = data[i].replace('<name>', '').replace(
                '</name>', '').replace('        ', '').replace('\n', '')
            for j in range(50):
                title = title.replace('  ', ' ')
        elif "<value>" in data[i]:
            a = data[i].replace(
                '<value>', '').replace('</value>', '').replace('            ', '').replace('\n', '')
            for j in range(50):
                a = a.replace('  ', ' ')
            tmp.append(a)
    f.close()

with open('result_car.json', 'w') as f:
    f.write(json.dumps(result))
    f.close()
