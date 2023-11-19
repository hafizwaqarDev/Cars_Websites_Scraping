import requests, csv
from lxml.html import fromstring
import PySimpleGUI as sg

class RRRScraper():
    def __init__(self) -> None:
        pass
    
    def header(self):
        Header = ['Product Title','Product Link','Product Image','Product Code','Delivered Country','Shiping Description','Price','Currency','Value Added Tax','Quality','Position Or Note','Manufacturer Code','Manufacturer','Series','Model','Year','Model year','Body Type','Steering Wheel Position','Driving Wheels','Fuel Type','Engine Capacity','Engine Power','Gearbox Type','Color','Mileage','Company Name','Company Url','Company PhoneNumber','Company Gmail','Bread Crumbs','Social Medias','More Description']
        with open(file='RRR.csv',mode='r') as file:
            CsvReader = csv.reader(file)
            if Header not in CsvReader:
                with open(file='RRR.csv',mode='a',newline='',encoding='UTF-8') as file:
                    csv.writer(file).writerow(Header)
# send a single request that get acess filter and return json Data
    def pageResponse(self):
        cookies = {
            'disable_ovoko_modal': '64e0e8c0de3e50.28490525',
            'G_ENABLED_IDPS': 'google',
            '_fbp': 'fb.1.1692461251383.385138084',
            'page-views': '2',
            '_ga_09YZB474KL': 'GS1.1.1692851354.7.1.1692851377.0.0.0',
        }

        headers = {
            'authority': 'rrr.lt',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'disable_ovoko_modal=64e0e8c0de3e50.28490525; G_ENABLED_IDPS=google; _fbp=fb.1.1692461251383.385138084; CookieConsent={stamp:%27/L3KebzMO08cYVj51ZLP3khmZWikRKwE3YVx+XVp9iSoMQiZjv1p2A==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1692461285064%2Cregion:%27pk%27}; _gcl_au=1.1.1484494099.1692461287; _ga=GA1.1.816668259.1692461247; ci_session=f766b6704ad3edb37fc9af2da73143abc5a920c5; soundestID=20230824042916-xW2gcFFVpd11aLdWXiSbg5VzOOfpvcDDdZ5Jdx8dXtkvGrfw6; omnisendSessionID=GMI5kPKJ0AD3OK-20230824042916; page-views=2; _ga_09YZB474KL=GS1.1.1692851354.7.1.1692851377.0.0.0',
   
        }

        params = {
            'man_id': '',
            '_': '',
        }

        response = requests.get('https://rrr.lt/en/search', params=params, cookies=cookies, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
# send secound request  that choose the car brand and return json Data
    def pageResponseFirstTime(self,CarsBrands):
        cookies = {
            'disable_ovoko_modal': '64e0e8c0de3e50.28490525',
            'G_ENABLED_IDPS': 'google',
            '_fbp': 'fb.1.1692461251383.385138084',
            'CookieConsent': '{stamp:%27/L3KebzMO08cYVj51ZLP3khmZWikRKwE3YVx+XVp9iSoMQiZjv1p2A==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1692461285064%2Cregion:%27pk%27}',

            'page-views': '2',
            '_ga_09YZB474KL': 'GS1.1.1692851354.7.1.1692851377.0.0.0',
        }
        headers = {
            'authority': 'rrr.lt',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'disable_ovoko_modal=64e0e8c0de3e50.28490525; G_ENABLED_IDPS=google; _fbp=fb.1.1692461251383.385138084; CookieConsent={stamp:%27/L3KebzMO08cYVj51ZLP3khmZWikRKwE3YVx+XVp9iSoMQiZjv1p2A==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1692461285064%2Cregion:%27pk%27}; _gcl_au=1.1.1484494099.1692461287; _ga=GA1.1.816668259.1692461247; ci_session=f766b6704ad3edb37fc9af2da73143abc5a920c5; soundestID=20230824042916-xW2gcFFVpd11aLdWXiSbg5VzOOfpvcDDdZ5Jdx8dXtkvGrfw6; omnisendSessionID=GMI5kPKJ0AD3OK-20230824042916; page-views=2; _ga_09YZB474KL=GS1.1.1692851354.7.1.1692851377.0.0.0',
            'referer': 'https://rrr.lt/en/search?man_id=125&cmc=1347&cm=2412&mfi=125,1347,2412;&prs=1&page=1',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',

        }
        params = {
            'man_id': CarsBrands,
            'cmc': '',
            'cm': '',
            'mfi': f"{CarsBrands}",
            'prs': '1',
            'page': '1',
            '_': '',
        }

        response = requests.get('https://rrr.lt/en/search', params=params, cookies=cookies, headers=headers)
        if response.status_code == 200:
            jsonData2 = response.json()
            return jsonData2
        else:
            print(f"Request failed with status code: {response.status_code}")
# send third request  that choose the car brand,car model and return json Data  
    def pageResponseSecondTime(self,CarsBrands,carModel):
        cookies = {
            'disable_ovoko_modal': '64e0e8c0de3e50.28490525',
            'G_ENABLED_IDPS': 'google',
            '_fbp': 'fb.1.1692461251383.385138084',
            'CookieConsent': '{stamp:%27/L3KebzMO08cYVj51ZLP3khmZWikRKwE3YVx+XVp9iSoMQiZjv1p2A==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1692461285064%2Cregion:%27pk%27}',
            '_gcl_au': '1.1.1484494099.1692461287',
            '_ga': 'GA1.1.816668259.1692461247',
            'ci_session': 'f766b6704ad3edb37fc9af2da73143abc5a920c5',
            'soundestID': '20230824042916-xW2gcFFVpd11aLdWXiSbg5VzOOfpvcDDdZ5Jdx8dXtkvGrfw6',
            'omnisendSessionID': 'GMI5kPKJ0AD3OK-20230824042916',
            'page-views': '2',
            '_ga_09YZB474KL': 'GS1.1.1692851354.7.1.1692851377.0.0.0',
        }
        headers = {
            'authority': 'rrr.lt',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'disable_ovoko_modal=64e0e8c0de3e50.28490525; G_ENABLED_IDPS=google; _fbp=fb.1.1692461251383.385138084; CookieConsent={stamp:%27/L3KebzMO08cYVj51ZLP3khmZWikRKwE3YVx+XVp9iSoMQiZjv1p2A==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1692461285064%2Cregion:%27pk%27}; _gcl_au=1.1.1484494099.1692461287; _ga=GA1.1.816668259.1692461247; ci_session=f766b6704ad3edb37fc9af2da73143abc5a920c5; soundestID=20230824042916-xW2gcFFVpd11aLdWXiSbg5VzOOfpvcDDdZ5Jdx8dXtkvGrfw6; omnisendSessionID=GMI5kPKJ0AD3OK-20230824042916; page-views=2; _ga_09YZB474KL=GS1.1.1692851354.7.1.1692851377.0.0.0',
            'referer': 'https://rrr.lt/en/search?man_id=125&cmc=1347&cm=2412&mfi=125,1347,2412;&prs=1&page=1',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {
            'man_id': CarsBrands,
            'cmc': carModel,
            'cm': '',
            'mfi': f'{CarsBrands}{carModel};',
            'prs': '1',
            'page': '1',
            '_': '',
        }

        response = requests.get('https://rrr.lt/en/search', params=params, cookies=cookies, headers=headers)
        if response.status_code == 200:
            jsonData2 = response.json()
            return jsonData2
        else:
            print(f"Request failed with status code: {response.status_code}")
# send third request  that choose the car brand,car model,car Modification and return json Data
    def pageResponseLastTime(self,CarsBrands,carModel,carModification):
        cookies = {
            'disable_ovoko_modal': '64e0e8c0de3e50.28490525',
            'G_ENABLED_IDPS': 'google',
            '_fbp': 'fb.1.1692461251383.385138084',
            'CookieConsent': '{stamp:%27/L3KebzMO08cYVj51ZLP3khmZWikRKwE3YVx+XVp9iSoMQiZjv1p2A==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1692461285064%2Cregion:%27pk%27}',
            '_gcl_au': '1.1.1484494099.1692461287',
            '_ga': 'GA1.1.816668259.1692461247',
            'ci_session': 'f766b6704ad3edb37fc9af2da73143abc5a920c5',
            'soundestID': '20230824042916-xW2gcFFVpd11aLdWXiSbg5VzOOfpvcDDdZ5Jdx8dXtkvGrfw6',
            'omnisendSessionID': 'GMI5kPKJ0AD3OK-20230824042916',
            'page-views': '2',
            '_ga_09YZB474KL': 'GS1.1.1692851354.7.1.1692851377.0.0.0',
        }
        headers = {
            'authority': 'rrr.lt',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'disable_ovoko_modal=64e0e8c0de3e50.28490525; G_ENABLED_IDPS=google; _fbp=fb.1.1692461251383.385138084; CookieConsent={stamp:%27/L3KebzMO08cYVj51ZLP3khmZWikRKwE3YVx+XVp9iSoMQiZjv1p2A==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1692461285064%2Cregion:%27pk%27}; _gcl_au=1.1.1484494099.1692461287; _ga=GA1.1.816668259.1692461247; ci_session=f766b6704ad3edb37fc9af2da73143abc5a920c5; soundestID=20230824042916-xW2gcFFVpd11aLdWXiSbg5VzOOfpvcDDdZ5Jdx8dXtkvGrfw6; omnisendSessionID=GMI5kPKJ0AD3OK-20230824042916; page-views=2; _ga_09YZB474KL=GS1.1.1692851354.7.1.1692851377.0.0.0',
            'referer': 'https://rrr.lt/en/search?man_id=125&cmc=1347&cm=2412&mfi=125,1347,2412;&prs=1&page=1',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        page = 1
        while True:
            params = {
                'man_id': CarsBrands,
                'cmc': carModel,
                'cm': carModification,
                'mfi': f'{CarsBrands},{carModel},{carModification};',
                'prs': '1',
                'page': page,
                '_': '',
            }
            response = requests.get('https://rrr.lt/en/search', params=params, cookies=cookies, headers=headers)
            response.status_code
            if response.status_code == 200:
                jsonData3 = response.json()
                if jsonData3['pages_total'] == page:
                    break
                page += 1
                for data in jsonData3['parts']:
                    self.parseData(data["slug"])
                    print(f'[Info] Getting Product Urls:- {data["slug"]}')
            else:
                print(f"Request failed with status code: {response.status_code}")
                break
# show and select the filter
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
                return selected_item
        window.close()      
# select the items by index number
    def selectedItem(self,selectedBrand,jsonData):
        print(f'\n[Info] your are Selected this Catageory:- {selectedBrand}\n')
        if selectedBrand == "":
            selectedBrand = 1  # Default selection
        else:
            try:
                CarBrandTag = jsonData['filters']['manufacturers']
                carName = selectedBrand
                for tag_id, tag_info in CarBrandTag.items():
                    if carName == tag_info['name']:
                        return tag_info['id']

            except KeyError: pass
            try: 
                CarModel = jsonData['filters']['model_categories']
                carModelsTag = selectedBrand
                for manufacturer_id, models in CarModel.items():
                    for model_id, model_info in models.items():
                        if carModelsTag == (model_info['name']):
            

            except KeyError: pass
            try:
                CarModification = jsonData['filters']['modifications']
                carmodifactionTag = selectedBrand
                for key, value in CarModification.items():
                    for sub_key, sub_value in value.items():
                        if carmodifactionTag == sub_value['name']:
                            return sub_value['id']
            except KeyError: pass
# get carBrandTags
    def carBrandTags(self,jsonData):
        CarBrandTag = jsonData['filters']['manufacturers']
        carBrands = []
        for tag_id, tag_info in CarBrandTag.items():
            carname = tag_info['name']
            carBrands.append(carname)

# get CarModel
    def CarModel(self,jsonData):
        CarModel = jsonData['filters']['model_categories']
        carModelsList = []
        for manufacturer_id, models in CarModel.items():
            for model_id, model_info in models.items():
                carModelsList.append(model_info['name'])

# get carModification
    def carModification(self,jsonData):
        CarModification = jsonData['filters']['modifications']
        carmodifactionList = []
        desired_id = None
        for key, value in CarModification.items():
            for sub_key, sub_value in value.items():
                carmodifactionList.append(sub_value['name'])
  
# now the parse data
    def parseData(self,link):
        pageSource = requests.get(link)     
        html = pageSource.text
        Souptree = fromstring(html)
        try: title = Souptree.find('.//h1[@data-testid="part-title"]').text.strip()
        except: title = ''
        try: productCode = Souptree.find('.//li[@class="product_info__items"]/a[@data-testid]').text.strip()
        except: productCode = ''
        try: 
            price = Souptree.find('.//div[@class="product_price_block"]/span[@data-testid="part-price"]').text.strip()
            currency = price[-1]
        except: price,currency = ''
        try: Vat = Souptree.find('.//div[@class="product_price_block"]/span[@class="product_price_block_text"]').text.strip()
        except: ''
        try: quality = Souptree.find('.//div[@id="product-desc-2"]/dl/dd[1]').text.strip()
        except: quality = ''
        try: positionOrNote = Souptree.find('.//div[@id="product-desc-2"]/dl/dd[2]').text.replace('\n','').strip()
        except: positionOrNote = ''
        try: 
            manufactureCodeTag = Souptree.xpath('//dt[contains(text(),"Manufacturer code:")]/parent::dl/dd/a')
            manufactureCode = ','.join([tag.text.strip() for tag in manufactureCodeTag]).strip()
        except: manufactureCode = ''
        try: image = Souptree.find('.//img[@data-testid="part-photo"]').get('src')
        except: image = ''
        try: 
            Modeltags = Souptree.xpath('//div[@id="product-desc-1"]/dl')
            model = ''.join([tag.text_content().strip() for tag in Modeltags])
            tagList = model.split('\n')
            newText = [data.strip() for data in tagList]
            keys,values = newText[0::2],newText[1::2]
            carDescription = {}
            for x,y in zip(keys,values):
                allKey = {x:y}
                carDescription.update(allKey)
        except: model = ''
        try:
            manufacturer = carDescription.get('Manufacturer', '')
            Series = carDescription.get('Series', '')
            Model = carDescription.get('Model', '')
            year = carDescription.get('Year', '')
            modelyear = carDescription.get('Model year', '')
            bodyType = carDescription.get('Body type', '')
            Steeringwheelposition = carDescription.get('Steering wheel position', '')
            drivingWheels = carDescription.get('Driving wheels', '')
            fuelType = carDescription.get('Fuel type', '')
            engineCapacity = carDescription.get('Engine capacity, cm3', '')
            enginePower = carDescription.get('Engine power, kW', '')
            gearboxType = carDescription.get('Gearbox type', '')
            color = carDescription.get('Color', '')
            mileage = carDescription.get('Mileage, km', '')
        except Exception as e:
            print("An error occurred:", e)
            manufacturer = Series = Model = year = modelyear = bodyType = Steeringwheelposition = drivingWheels = fuelType = engineCapacity = enginePower = gearboxType = color = mileage = ''

        try: 
            shipingDescription = Souptree.find('.//div[@id="product-help-1"]/p/b').text.strip()
            country = shipingDescription.split(' ')[-1]
        except: shipingDescription,country = ''
        try: CompanyName = Souptree.find('.//a[@data-testid="seller-info-link"]').get('title').strip()
        except: CompanyName = ''
        try: companyUrl = Souptree.find('.//div[@id="product-help-4"]/div/a').get('href')
        except: companyUrl = ''
        try: 
            information = Souptree.xpath('//strong[contains(text(),"Seller description")]/parent::div')
            CompanyGmail = ''
            CompanyPhoneNumber = ''
            if information is not None:
                inforTags = ''.join([tag.text_content().strip() for tag in information])
                informationSplit = ''.join((inforTags.split('\n'))).split()
                for data in informationSplit:
                    if '@' in data:
                        CompanyGmail = data
                    elif '+' in data:
                        CompanyPhoneNumber = data
            else: 
                CompanyPhoneNumber,CompanyGmail = ''
        except Exception as e:
            print("An error occurred:", e)
        try:
            descriptionTag = Souptree.find('.//div[@class="page-description"]')
            if descriptionTag is not None:
                descTags = descriptionTag.text_content().strip()
            descriptiontag2 = descTags.replace('\xa0','').replace('\r\n','').replace('\n','').replace('/en.','').strip()
            description = ' '.join(descriptiontag2.split())
        except: description = ''
        try: 
            socialMediasTags = Souptree.xpath('//div[@class="page-description"]//a')
            socialMedias = [url.get('href') for url in socialMediasTags]
        except: socialMedias = ''
        try: 
            breadCrumbsTags = Souptree.xpath('.//div[@class="main breadcrumb__wrapper"]/ul[1]/li')
            breadCrumbs = '>'.join([url.text_content().strip() for url in breadCrumbsTags])
        except: breadCrumbs = ''
        row = [title,link,image,productCode,country,shipingDescription,price,currency,Vat,quality,positionOrNote,manufactureCode,manufacturer,Series,Model,year,modelyear,bodyType,Steeringwheelposition,drivingWheels,fuelType,engineCapacity,enginePower,gearboxType,color,mileage,CompanyName,companyUrl,CompanyPhoneNumber,CompanyGmail,breadCrumbs,socialMedias,description]
        print(f'Getting Product:- {title}')
        self.saveData(row)

# save the parse data
    def saveData(self,row):
        with open(file='RRR.csv',mode='r',newline='',encoding='UTF-8') as file:
            CsvReader = csv.reader(file)
            if row not in CsvReader:
                with open(file='RRR.csv',mode='a',newline='',encoding='UTF-8') as file:
                    csv.writer(file).writerow(row)
# run all functions
    def run(self):
        jsonData1 = self.pageResponse()
        carBrand = self.carBrandTags(jsonData1)
        checkBrand = self.ShownselectedItem(carBrand,'Select a Car Brand:- ')
        carbrandID = self.selectedItem(checkBrand,jsonData1)
        jsonData2 = self.pageResponseFirstTime(carbrandID)
        carModels = self.CarModel(jsonData2)
        checkModel = self.ShownselectedItem(carModels,'Select a Car Model:- ')
        modelId = self.selectedItem(checkModel,jsonData2)
        jsonData3 = self.pageResponseSecondTime(carbrandID,modelId)
        carModification = self.carModification(jsonData3)
        checkModification = self.ShownselectedItem(carModification,'Select a Car Modification:- ')
        carModifiId = self.selectedItem(checkModification,jsonData3)
        self.pageResponseLastTime(carbrandID,modelId,carModifiId)

open(file='RRR.csv',mode='a').close()
myClass = RRRScraper()
myClass.header()
myClass.run()
