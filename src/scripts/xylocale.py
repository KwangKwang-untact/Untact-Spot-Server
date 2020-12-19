import json

result = list()
with open('DB.json', 'r') as f:
    data = json.loads(f.read())
    for tmp in data:
        print(tmp)
        if tmp["address"] == "경기 포천시 이동면 화동로 1925-47":
            tmp["latitude"] = 127.364518333317
            tmp["longitude"] = 38.0189834254687
        elif tmp["address"] == "경남 통영시 천대국치길 297-10 (인평동)":
            tmp["latitude"] = 128.39007097737
            tmp["longitude"] = 34.8385493982446
        elif tmp["address"] == "전남 함평군 신광면 덕일길 192-91":
            tmp["latitude"] = 126.509447278409
            tmp["longitude"] = 35.1363395468159
        elif tmp["address"] == "경기 고양시 덕양구 북한산로387번길 180 (지축동)":
            tmp["latitude"] = 126.949793353391
            tmp["longitude"] = 37.6671521092109
        else:
            tmp["latitude"] = float(tmp["latitude"].replace("4d", ""))
            tmp["longitude"] = float(
                tmp["longitude"].replace("3d", "").replace('!', ''))
        result.append(tmp)

with open('DB_final.json', 'w') as f:
    f.write(json.dumps(result))
