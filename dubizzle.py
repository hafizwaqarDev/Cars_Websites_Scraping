import requests, csv
from lxml.html import fromstring
import PySimpleGUI as sg

class dubizzle_Scraper():
    def __init__(self) -> None:
        pass

    def header(self):
        
        header = ['Product Title','Product Url','Product Image','Posted Date','Price','Posted By','Adress','Interior Color','Exterior Color','Motors Trim','Year','Regilonal Space','Kilometers','Doors','Body Type','Body Conditation','Mechanical Condition','Seller Type','Seating Capacity','Transmission Type','Engine Capacity','Horse Power','Warranty','Fuel Type','No of Cylinders','Target Market','Extras','Technical Feartures','Auto Option','Description']
        with open(file='dubizzle.csv',mode='w',newline='') as file:
            csv.writer(file).writerow(header)

    def Selectcites(self):
        cities = ['UAE',"Al Ain","Dubai","Abu Dhabi","Ras Al Khaimah","Sharjah","Fujairah","Ajman","Umm Al Quwain"]

    
    def SelectCarsBrands(self):
        car_brands = ["All in Cars", "Abarth", "Acura", "Alfa Romeo", "Ariel", "Aston Martin", "Audi", "BAC", "BAIC", "Bentley", "Bestune", "Bizzarrini", "BMW", "BMW Alpina", "Borgward", "Brilliance", "Bufori", "Bugatti", "Buick", "BYD", "Cadillac", "Can-am", "Caterham", "CEVO", "Changan", "Chery", "Chevrolet", "Chrysler", "Citroen", "CMC", "Daewoo", "Daihatsu", "Datsun", "DeLorean", "Denza", "DFSK", "Dodge", "DongFeng", "Dorcen", "Equus", "Exeed", "Faw", "Fengon", "Fenyr", "Ferrari", "Fiat", "Fisker", "Force", "Ford", "Foton", "GAC", "GAC Gonow", "Geely", "Genesis", "GMC", "Grand Tiger", "Great Wall", "Gumpert", "Haval", "HiPhi", "Honda", "Hongqi", "Hummer", "Hyundai", "Infiniti", "International", "Isuzu", "Iveco", "JAC", "Jaguar", "Jeep", "Jetour", "Jinbei", "JMC", "Kia", "King Long", "Koenigsegg", "KTM", "Lada", "Lamborghini", "Lancia", "Land Rover", "LEVC", "Lexus", "Lincoln", "Lotus", "Luxgen", "Lynk & Co", "Mahindra", "Maserati", "Maxus", "Maybach", "Mazda", "McLaren", "Mercedes-AMG", "Mercedes-Benz", "Mercedes-Maybach", "Mercury", "MG", "Milan", "MINI", "Mitsubishi", "Morgan", "Morris", "Nio", "Nissan", "Noble", "Oldsmobile", "Opel", "Oullim", "Pagani", "PAL-V", "Peugeot", "PGO", "Polestar", "Pontiac", "Porsche", "Proton", "Qiantu", "RAM", "Renault", "Rivian", "Rolls Royce", "Rover", "Saab", "Seat", "Shenlong/Sunlong", "Skoda", "Smart", "Soueast", "Speranza", "Spyker", "SsangYong", "Studebaker", "Subaru", "Suzuki", "TANK", "TATA", "Tesla", "Toyota", "Triumph", "UAZ", "Victory", "Volkswagen", "Volvo", "Voyah", "W Motors", "Westfield Sportscars", "Wiesmann", "XPeng", "Zeekr", "Zenvo", "ZNA", "Zotye", "Other Make"]

    
    def SelectCarsModels(self,brandName):
        cookies = {
            'visid_incap_2413658': 'XqLnPwKcTJ+iqYcZQOboz+vn4GQAAAAAQUIPAAAAAAALXEdqXfBwahBoZr1bhqdl',
            '_gcl_au': '1.1.738000927.1692461064',
            '_fbp': 'fb.1.1692461068087.287528610',
            '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22iAx3z7v2sN1B7X2BhOAF%22%7D',
            'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2298aae2e6-ee09-4964-8da6-fccbc0ed78c7%22%2C%22deviceAdded%22%3Atrue%7D',
            '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22922946391.1692461065%22%7D',
            '_cc_id': '2d4af62ca801f8cd234441148b811f21',
            '_pbjs_userid_consent_data': '3524755945110770',
            'ias': '0',
            '_gid': 'GA1.2.1422734624.1693199313',
            'panoramaId_expiry': '1693285718584',
            'panoramaId': 'f0481555abf46ce31af7dcfb5692a9fb927a3115d035a4bfaa0feb955c9b6381',
            'OPT_IN_SHOWN_TIME': '1693199328171',
            'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
            'nlbi_2413658': 'adAIIItIqW4E0vgIT83W0gAAAADXhsmPgZd3U5Qoroi2ZDX+',
            'moe_uuid': '98aae2e6-ee09-4964-8da6-fccbc0ed78c7',
            'incap_ses_956_2413658': '0tfCKpK/fEEjqt89ymVEDTKp7GQAAAAAD5t7oLfgwsrszcTM6M6EDw==',
            'skybar_sess_False': '1',
            'default_site': '2',
            'sid': '3k4bnnlmbelkvxa3az19fytnnpkpzo6u',
            '__gads': 'ID=e646d52605d1d993:T=1692461069:RT=1693232461:S=ALNI_MbrWiK1Kc7-6DtY8rTi7aH7bZRQNQ',
            '__gpi': 'UID=00000c8af577d599:T=1692461069:RT=1693232461:S=ALNI_Mb0t2LIY9kZZqGYa2p_zr1zsqlBgQ',
            'reese84': '3:Rl1l6Csb4yPexotzHDxWwA==:abJdeTC3du33sz3WVpyHBm28fLjAvssxlmCPe3KFXUwt3WLF4gUHTjEGMxoiFx8IMeS67Xnu3vPrZ5cfcEUYgPQmgYYZ7WCsZBvR0eRw7c5cd3wb509eoYDdqDIQIE6/4M17/okcfJzLmyw1e/9EW20mE5EDcdoSYL7cUnqnfOZcXk46wJo27fGNcQEGetfXtBYJP6+ZGBma2D6zorcIwWKNhx/LmyRKbM5kLGGr7fgl7YPSQkA8gSZ3hKwAqEP67F2dM7RK+qVT4dFxr0yTGz949foSK1KZnAGyZ4uQu8srrCcaY0E254xxuaQvuqth5wI7sHMKf0WWDl5m/UY/OvT1baS3IMO1A5aIf3sFd1eKgVxjw2gUQQPz881IcymGziMRxSNclDgR2aHbEsA4K4kKMN2DeYyXOncKmuDW1AotC/sYGYO+sm7CC3Hn+eGZMbP7r0vqkgxYWooETUdzeaQCciaA6uU13+Ugm+0+/bW6ho+2bzwlRyckhH46gOtoO4m6inJISN4SuShStnHRsHAbl3tdXAjjL+vWqKKC1Bw=:PxIZi0yh2hVNxdsySHkkifjrFyVGOis2ZVSN5WPysQE=',
            'nlbi_2413658_2147483392': 'op2sN8MoUWIUt1dnT83W0gAAAACRC3YDD2Z8vwx5G5mMHOot',
            '_gat_UA-205528691-1': '1',
            '_ga': 'GA1.1.922946391.1692461065',
            '_ga_LRML1YM9GH': 'GS1.1.1693231414.13.1.1693233281.49.0.0',
            'cto_bundle': 'Sr0pLl9jOWMlMkJ4bnBJYXpwQzFaVGFJNGMlMkJBcXBQbWNJYlBFNHNncktLQURnQmE1VyUyRnBSdDlDWjhyNTN5R1N0cVlDMW1pUkVvMVhZSkpNN2ZIcSUyQklQOHJxTGhIRWlNTkNEenB5dVNucmFwSWp6d1FYdmhmYzF4U2NMOFZBazlzWmJ3Q0VnR1FoR0E2b0Z6STIzZDZia1MlMkJQUEV3JTNEJTNE',
        }

        headers = {
            'authority': 'dubia.dubizzle.com',
            'accept': 'application/json',
            'accept-language': 'en',
            'cache-control': 'must-revalidate, max-age=0, no-cache, no-store',
            'content-type': 'application/json;charset=UTF-8',
            # 'cookie': 'visid_incap_2413658=XqLnPwKcTJ+iqYcZQOboz+vn4GQAAAAAQUIPAAAAAAALXEdqXfBwahBoZr1bhqdl; _gcl_au=1.1.738000927.1692461064; _fbp=fb.1.1692461068087.287528610; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22iAx3z7v2sN1B7X2BhOAF%22%7D; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2298aae2e6-ee09-4964-8da6-fccbc0ed78c7%22%2C%22deviceAdded%22%3Atrue%7D; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22922946391.1692461065%22%7D; _cc_id=2d4af62ca801f8cd234441148b811f21; _pbjs_userid_consent_data=3524755945110770; ias=0; _gid=GA1.2.1422734624.1693199313; panoramaId_expiry=1693285718584; panoramaId=f0481555abf46ce31af7dcfb5692a9fb927a3115d035a4bfaa0feb955c9b6381; OPT_IN_SHOWN_TIME=1693199328171; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; nlbi_2413658=adAIIItIqW4E0vgIT83W0gAAAADXhsmPgZd3U5Qoroi2ZDX+; moe_uuid=98aae2e6-ee09-4964-8da6-fccbc0ed78c7; incap_ses_956_2413658=0tfCKpK/fEEjqt89ymVEDTKp7GQAAAAAD5t7oLfgwsrszcTM6M6EDw==; skybar_sess_False=1; default_site=2; sid=3k4bnnlmbelkvxa3az19fytnnpkpzo6u; __gads=ID=e646d52605d1d993:T=1692461069:RT=1693232461:S=ALNI_MbrWiK1Kc7-6DtY8rTi7aH7bZRQNQ; __gpi=UID=00000c8af577d599:T=1692461069:RT=1693232461:S=ALNI_Mb0t2LIY9kZZqGYa2p_zr1zsqlBgQ; reese84=3:Rl1l6Csb4yPexotzHDxWwA==:abJdeTC3du33sz3WVpyHBm28fLjAvssxlmCPe3KFXUwt3WLF4gUHTjEGMxoiFx8IMeS67Xnu3vPrZ5cfcEUYgPQmgYYZ7WCsZBvR0eRw7c5cd3wb509eoYDdqDIQIE6/4M17/okcfJzLmyw1e/9EW20mE5EDcdoSYL7cUnqnfOZcXk46wJo27fGNcQEGetfXtBYJP6+ZGBma2D6zorcIwWKNhx/LmyRKbM5kLGGr7fgl7YPSQkA8gSZ3hKwAqEP67F2dM7RK+qVT4dFxr0yTGz949foSK1KZnAGyZ4uQu8srrCcaY0E254xxuaQvuqth5wI7sHMKf0WWDl5m/UY/OvT1baS3IMO1A5aIf3sFd1eKgVxjw2gUQQPz881IcymGziMRxSNclDgR2aHbEsA4K4kKMN2DeYyXOncKmuDW1AotC/sYGYO+sm7CC3Hn+eGZMbP7r0vqkgxYWooETUdzeaQCciaA6uU13+Ugm+0+/bW6ho+2bzwlRyckhH46gOtoO4m6inJISN4SuShStnHRsHAbl3tdXAjjL+vWqKKC1Bw=:PxIZi0yh2hVNxdsySHkkifjrFyVGOis2ZVSN5WPysQE=; nlbi_2413658_2147483392=op2sN8MoUWIUt1dnT83W0gAAAACRC3YDD2Z8vwx5G5mMHOot; _gat_UA-205528691-1=1; _ga=GA1.1.922946391.1692461065; _ga_LRML1YM9GH=GS1.1.1693231414.13.1.1693233281.49.0.0; cto_bundle=Sr0pLl9jOWMlMkJ4bnBJYXpwQzFaVGFJNGMlMkJBcXBQbWNJYlBFNHNncktLQURnQmE1VyUyRnBSdDlDWjhyNTN5R1N0cVlDMW1pUkVvMVhZSkpNN2ZIcSUyQklQOHJxTGhIRWlNTkNEenB5dVNucmFwSWp6d1FYdmhmYzF4U2NMOFZBazlzWmJ3Q0VnR1FoR0E2b0Z6STIzZDZia1MlMkJQUEV3JTNEJTNE',
            'referer': 'https://abudhabi.dubizzle.com/motors/used-cars/',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            # 'x-access-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjljNWQwMmY2LTQ5ZTYtNDg1ZS1iNjEwLThjZmQ4MTJiZTMxZCIsImlzcyI6ImR1Yml6emxlLmNvbSIsImF1ZCI6WyJkdWJpenpsZS5jb20iXSwic3ViIjoiOWM1ZDAyZjYtNDllNi00ODVlLWI2MTAtOGNmZDgxMmJlMzFkIiwiZXhwIjoxNjkzMzE5Njc2LCJpYXQiOjE2OTMyMzMyNzYsImp0aSI6IjcyOTE3ZjlmLWM2NTItNDExNy05Yzg2LWI2YmMzM2UxMDRkMiIsInR5cCI6IkFjY2VzcyBKV1QgVG9rZW4iLCJmbGFncyI6eyJsb2dnZWRfaW4iOmZhbHNlLCJpc19zdGFmZiI6ZmFsc2UsImlzX3N1cGVydXNlciI6ZmFsc2UsImlzX3Byb3BlcnR5X2FnZW50IjpmYWxzZSwiaXNfbGFuZGxvcmQiOmZhbHNlLCJpc19tb3RvcnNfYWdlbnQiOmZhbHNlLCJpc19qb2JzX2FnZW50IjpmYWxzZSwiaXNfbGVhZF9ibG9jayI6ZmFsc2UsImlzX2NoYXRfYmxvY2siOmZhbHNlLCJoYXNfY2FsbF90cmFja2luZyI6ZmFsc2UsImNhbl9yZXBvcnQiOnRydWUsImhpZGVfcHVibGljX3Byb2ZpbGUiOmZhbHNlfSwidXNlcl9kYXRhIjp7InVzZXJfaWQiOm51bGwsImdlbmRlciI6bnVsbCwibmF0aW9uYWxpdHkiOm51bGwsImVkdWNhdGlvbiI6bnVsbCwicm9sZSI6bnVsbCwiZG9iIjpudWxsLCJhZ2UiOm51bGwsImZpcnN0X25hbWUiOiIiLCJsYXN0X25hbWUiOiIiLCJlbWFpbCI6IiIsInBob25lIjoiIiwidmVyaWZpY2F0aW9uX3N0YXR1cyI6Im5vdF9hcHBsaWVkIiwidmVyaWZpY2F0aW9uX3N0YXJ0X2RhdGUiOm51bGx9fQ.TBACcnHT3VZW2WxsFz6OXo3DjBP-k0K6b2S-nNvp7_SlGqhV5v3N_adTWPXbpRPu8aECrVz8-pohXJBFlGXB3AhyrNK7DFqqZj6hUogD2mr5TUD6tOrRGJVmyLceMIz2MVYlRkO5OgAEWyJON-GUC6-EWYWX6FNz1N2Unjs-0qKOmZWkLbUo5HHdKOxwR9oDqEzO0FEfmS5SeqARy848bnbHfZ7uyeCWpPGet95H-xszlI8L9poZWMSQEoGvRji0o677QTVuygS5XQWD6CIoDHsdy6-jF6LYjSx-v0aGoYslDVNqOxnp4RemiLyKqaa48FHgE3ATSC-V1mguBSnHcufvewK2grqIeo7CnpsdwWgipKq3OLtBhlEOkIiXe2GPBy8Glrh2cjlPr9c2ty7-I1thPhBUC-GcmRPn5EgFaN9xOKu4vxC4o8xDXNYkopNv4DIYNdkytt47by4gSCnKB_jAeqXEMbIVDr5hyou3tcaX5FeHetLiu1TfMtcQu4747LyUUOKniDoELamvZKA-ZDZ41SQ1NOIeDjYZLM5us9Zq_giX7GTBG_Ka7nZfjfhUDyej8L3Zsg_10xChMKa1HleDkZ7UWRV7wkZEhmnUdo88aekatNkwRqJS0EZ3nZquB7TLpWesHCCVpLsFos2AnUIjevGJitGLpOptamup6Fk',
        }

        response = requests.get(
            f'https://dubia.dubizzle.com/motors/svc/buyer/api/v1/options/?category=motors/used-cars/{brandName}&city=''&filter_name=category',
            cookies=cookies,
            headers=headers,
        )
        if response.status_code == 200:
            jsonData = response.json()
            ModelData = jsonData['options']
            allModels = []
            for data in ModelData:
                models = data['label']['en']
                allModels.append(models)

        else:
            print(f"Request failed with status code: {response.status_code}")
    
    def pageResponse(self,pageUrl,cityName):
        header = {
            'authority':f'{cityName}.dubizzle.com',
            'method':'POST',
            # 'Accept':'application/json; charset=utf-8',
            'Cookie':'visid_incap_2413658=XqLnPwKcTJ+iqYcZQOboz+vn4GQAAAAAQUIPAAAAAAALXEdqXfBwahBoZr1bhqdl; _gcl_au=1.1.738000927.1692461064; _fbp=fb.1.1692461068087.287528610; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22iAx3z7v2sN1B7X2BhOAF%22%7D; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2298aae2e6-ee09-4964-8da6-fccbc0ed78c7%22%2C%22deviceAdded%22%3Atrue%7D; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22922946391.1692461065%22%7D; _cc_id=2d4af62ca801f8cd234441148b811f21; _pbjs_userid_consent_data=3524755945110770; ias=0; _gid=GA1.2.1422734624.1693199313; OPT_IN_SHOWN_TIME=1693199328171; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; default_site=2; sid=3k4bnnlmbelkvxa3az19fytnnpkpzo6u; panoramaId_expiry=1693379067055; panoramaId=f0481555abf46ce31af7dcfb5692a9fb927a3115d035a4bfaa0feb955c9b6381; nlbi_2413658=JuQRPgHH3yrU01qxT83W0gAAAAAJ2/OVWGpF0lDjJD4k3rKp; incap_ses_969_2413658=OsHNJXCyMwCGesODVJVyDfWX7mQAAAAAfuwQVLmlTBfYa2mrRgh/LA==; reese84=3:tTEcgnRw9vhL2pwFd1O9cg==:FM3NfIPIO8AA6Ao7SLn2tG/GaxejMynktAM/uSKB14QrHEcXuyRD29jfZSClMtelqW7kb8JlOlTdWncv+UfyGV51r1pzCVvX/vFzGccRW5OA4fv+vwd7tb6tNqX8uCnR+Pg1h3zZmf60aF0rqF6ztzYZif1ajRxIN1hyNrbDZEq98uBYX9979nzoamcpWV9cuUquyGF510udBm2OLTCCn9cta8n7ZuOd+TTndUaCT9xtx9kkuNsCp3Js2xKig1Xd6lLfjV66O8n8VLvW8MopFGLhspvonwjlCp+6muCoCLT8LMNRwMxW+cUDe+7q5SzmEtGDjqWj4+eW3DR86w55Kz2R2VYB+6JC4z1iBZ3rLWhpwD05CncsD7MoHvzrBEJAVZ3WTwqfsGCV66v6wwdCelA+3T4tycx+4nlw8/J5QHJK1U/BZSChTPdDxQqZ8wkwaJI/ikdQmRz+9/uRFW+qIZ+A4PJQAOl02rWt/rqpbJxExgkq4d2hjP7RIXsk+77VRoWlguEePhGfZ1XlzJEPNNYGx4KqLyxkRN5RWQSK2PI=:fOl4JZvpLZo9Jpb7BkoWi3hApH+d8ffPcdTxedOaPGM=; __gads=ID=e646d52605d1d993:T=1692461069:RT=1693358077:S=ALNI_MbrWiK1Kc7-6DtY8rTi7aH7bZRQNQ; __gpi=UID=00000c8af577d599:T=1692461069:RT=1693358077:S=ALNI_Mb0t2LIY9kZZqGYa2p_zr1zsqlBgQ; moe_uuid=98aae2e6-ee09-4964-8da6-fccbc0ed78c7; _ga=GA1.2.922946391.1692461065; cto_bundle=WEqOoV9jOWMlMkJ4bnBJYXpwQzFaVGFJNGMlMkJBZ2lzb3ZNakt2T1dnaXgxNU0yOGFtTGtHJTJGRUM3emoxUVJFYkpOclZZTUROdG5BQ0R0VGtSJTJCZFRXR0Q5VG03NHMlMkI5ZG9BSCUyQm5TcnIzZ3hla2ZpeHdNMFpjbUhndWRVaW5LcEFnUnNjanJIQzRhaEtaZTc0Ykk0QUJHJTJCYXIlMkZSZE1BJTNEJTNE; _ga_LRML1YM9GH=GS1.1.1693358075.19.1.1693358125.10.0.0; nlbi_2413658_2147483392=ttaUPszJvHp+bCS4T83W0gAAAAACTMV64QgB6NqWivD8b5L0',
            'Origin':f'https://{cityName}.dubizzle.com',
            'Sec-Ch-Ua-Platform':'Windows',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
        
        pageResponse = requests.get(pageUrl,headers=header)
        if pageResponse.status_code == 200:
            pageSouptree = fromstring(pageResponse.text)
            domain = f'https://{cityName}.dubizzle.com/'
            lastpage = pageSouptree.xpath('//a[@data-testid="page-next"]')
            prductUrlsTag = pageSouptree.xpath('//div[@id="listings-container"]/div[@type="primary"]/a')
            for url in prductUrlsTag:
                productUrls = domain + url.get('href')
                self.parseData(productUrls,header)

        else:
            print(f"Request failed with status code: {pageResponse.status_code}")

    def parseData(self,url,header):
        pageResponse = requests.get(url,headers=header)
        pageResponse.status_code
        souptree = fromstring(pageResponse.text)
        try: title = souptree.find('.//h3[@data-ui-id="listing-name"]').text.strip()
        except: title = ''
        try: postedDate = souptree.find('.//p[@class="sc-1pns9yx-0 hWbPbb"]').text_content().strip()
        except: postedDate = ''
        try: price = souptree.find('.//div[@class="sc-19dsmxk-0 qiYSA"]/p').text.strip()
        except: price = ''
        try: postedBy = souptree.find('.//div[@class="sc-1ezarox-0 hgQuiu"]/div/div/div/p[2]').text.strip()
        except: postedBy = ''
        try: image = souptree.find('.//img[@class="image-gallery-image"]').get('src')
        except: ''
        try: interiorColor = souptree.find('.//p[@data-ui-id="details-value-interior_color"]').text.strip()
        except: interiorColor = ''
        try: motors_trim = souptree.find('.//p[@data-ui-id="details-value-motors_trim"]').text.strip()
        except: motors_trim = ''
        try: year = souptree.find('.//p[@data-ui-id="details-value-year"]').text.strip()
        except: year = ''
        try: regilonalSpace  = souptree.find('.//p[@data-ui-id="details-value-regional_specs"]').text.strip()
        except: regilonalSpace = ''
        try: kilometers  = souptree.find('.//p[@data-ui-id="details-value-kilometers"]').text_content().strip()
        except: kilometers = ''
        try: door = souptree.find('.//p[@data-ui-id="details-value-doors"]').text.strip()
        except: door = ''
        try: bodyType = souptree.find('.//p[@data-ui-id="details-value-body_type"]').text.strip()
        except: bodyType = ''
        try: bodyConditation = souptree.find('.//p[@data-ui-id="details-value-body_condition"]').text.strip()
        except: bodyConditation = ''
        try: mechanical_condition = souptree.find('.//p[@data-ui-id="details-value-mechanical_condition"]').text.strip()
        except: mechanical_condition = ''
        try: seller_type = souptree.find('.//p[@data-ui-id="details-value-seller_type"]').text.strip()
        except: seller_type = ''
        try: seating_capacity = souptree.find('.//p[@data-ui-id="details-value-seating_capacity"]').text.strip()
        except: seating_capacity = ''
        try: transmission_type = souptree.find('.//p[@data-ui-id="details-value-transmission_type"]').text.strip()
        except: transmission_type = ''
        try: engine_capacity = souptree.find('.//p[@data-ui-id="details-value-engine_capacity_cc"]').text.strip()
        except: engine_capacity = ''
        try: horsepower = souptree.find('.//p[@data-ui-id="details-value-horsepower"]').text.strip()
        except: horsepower = ''
        try: warranty = souptree.find('.//p[@data-ui-id="details-value-warranty"]').text.strip()
        except: warranty = ''
        try: fuel_type = souptree.find('.//p[@data-ui-id="details-value-fuel_type"]').text.strip()
        except: fuel_type = ''
        try: no_of_cylinders = souptree.find('.//p[@data-ui-id="details-value-no_of_cylinders"]').text.strip()
        except: no_of_cylinders = ''
        try: exterior_color = souptree.find('.//p[@data-ui-id="details-value-exterior_color"]').text.strip()
        except: exterior_color = ''
        try: target_market = souptree.find('.//p[@data-ui-id="details-value-target_market"]').text.strip()
        except: target_market = ''
        try: location = souptree.find('.//div[@class="sc-19dsmxk-0 sc-1lcvnfi-0 iMFMms bXqkWN"]/div/span').text_content().strip()
        except: location = ''
        try: extras = souptree.find('.//p[@data-ui-id="details-value-auto_options_recommended"]').text_content().replace('\n','').strip()
        except: extras = ''
        try: technicalFeartures = souptree.find('.//p[@data-ui-id="details-value-technical_features"]').text_content().replace('\n','').strip()
        except: technicalFeartures = ''
        try: autoOption = souptree.find('.//p[@data-ui-id="details-value-auto_options"]').text_content().replace('\n','').strip()
        except: autoOption = ''
        try: 
            descriptionTag = souptree.xpath('//div[@class="sc-19dsmxk-0 sc-1bi45uo-0 iMFMms jtFNPR"]/div/span')
            description = [tag.text.replace('\n','').replace('-','').replace('*','').strip() for tag in descriptionTag]
        except: description = ''
        row = [title,url,image,postedDate,price,postedBy,location,interiorColor,exterior_color,motors_trim,year,regilonalSpace,kilometers,door,bodyType,bodyConditation,mechanical_condition,seller_type,seating_capacity,transmission_type,engine_capacity,horsepower,warranty,fuel_type,no_of_cylinders,target_market,extras,technicalFeartures,autoOption,description]
        print(f'[Info] Getting Car :- {title}')
        self.saveData(row)
    
    def saveData(self,row):
        with open(file='dubizzle.csv',mode='r',newline='',encoding='UTF-8') as file:
            CsvReader = csv.reader(file)
            if row not in CsvReader:
                with open(file='dubizzle.csv',mode='a',newline='',encoding='UTF-8') as file:
                    csv.writer(file).writerow(row)
    
    def ShownselectedItem(self,sample_list,SomeCatageory):
        layout = [
            [sg.Text(SomeCatageory)],
            [sg.Listbox(values=sample_list, size=(30, 6), key='-LIST-', enable_events=True)],
            [sg.Button("Select"), sg.Button("Exit")]
        ]

        window = sg.Window("Item Selector", layout)
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
            elif event == "Select":
                selected_item = values['-LIST-'][0] if values['-LIST-'] else None
                if selected_item:
                    sg.popup(f"You selected: {selected_item}")
                else:
                    sg.popup("Please select an item from the list.")
                    window.close()
                window.close()
      
        window.close()
        
    def run(self):
        cities = self.Selectcites()
        Citesquery = f'[Info] Select a city in this list:-'
        selectCity = self.ShownselectedItem(cities,Citesquery)
        brands = self.SelectCarsBrands()
        Brandsquery = f'[Info] Select a brand in this list:-'
        selectbrand = self.ShownselectedItem(brands,Brandsquery)
        carModels = self.SelectCarsModels(selectbrand)
        Modelsquery = f'[Info] Select a Car Model in this list:-'
        selectModel = self.ShownselectedItem(carModels,Modelsquery)
        page = 1
        while True:
            pageUrl = f'https://{selectCity}.dubizzle.com/motors/used-cars/{selectbrand}/{selectModel}/?page={page}'
            lastpage = self.pageResponse(pageUrl,selectCity)
            if not lastpage:
                break
            page += 1
            print(f'\n[Info] Getting data from this Url:-{pageUrl}\n')
        
open(file='dubizzle.csv',mode='a').close()
myclass = dubizzle_Scraper()
myclass.header()
myclass.run()
