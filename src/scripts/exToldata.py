import requests
import json

result = list()

for i in range(1, 6):
    response = requests.get(
        "http://data.ex.co.kr/openapi/basicinfo/unitList?key=4625471897&type=json&numOfRows=100&pageNo={}".format(i)).json()["unitLists"]

    for data in response:
        tmp = requests.get(
            "http://data.ex.co.kr/openapi/locationinfo/locationinfoUnit?key=4625471897&type=json&unitCode={}&numOfRows=10&pageNo=1".format(
                data["unitCode"])
        ).json()["list"][0]
        result.append({
            "name": data["unitName"],
            "code": data["unitCode"],
            "latitude": tmp["xValue"],
            "longitude": tmp["yValue"]
        })
        print({
            "name": data["unitName"],
            "code": data["unitCode"],
            "latitude": tmp["xValue"],
            "longitude": tmp["yValue"]
        })

with open("result_tol.json", 'w') as f:
    f.write(json.dumps(result))
