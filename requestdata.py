import requests

#def自訂函數+函數名稱(變數)
def requestdata():
    # 使用 GET 方式下載普通網頁
    response = requests.get('https://tw.portal-pokemon.com/cardmap/api/poi?uuid=e24f6ca8-d2cc-4f9b-8ec0-34b4765f94c3&bounds=23.966175871265033,120.14648437500001,24.44714958973082,121.37695312499999&zoom=11&_=1658799601894')
    obj=response.json() #檔案轉換
    dric=(obj[3])
    results = (dric["name"]) #結果
    
    return results
