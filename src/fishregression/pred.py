import requests as reqs

def pred():
    l = input("🐳 물고기의 길이를 입력해주세요 : ")

    resp = reqs.get(f"http://localhost:8001/fish?length={l}").text
    w=eval(resp)["prediction"]
    
    resp = reqs.get(f"http://localhost:8002/fish_std?length={l}&weight={w}&nneighbor=5").text
    pred=eval(resp)["prediction"]

    print(f"\n🐳 입력한 물고기의 길이는 {l}입니다.")
    if float(w)<0:
        print(f"🐳 물고기의 무게는 너무 작아 예측이 어렵습니다.")        
    else:
        print(f"🐳 물고기의 무게는 {w}로 예측됩니다.")
    print(f"🐳 물고기의 종류는 {pred}로 예측됩니다.\n")
