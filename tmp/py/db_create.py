import urllib.request
import re
import os
import sqlite3
import sys

def print_url_error(url):
    print('Ошибка при открытии ', url)

def print_url_sucsees(url):
    print('$$$$$$$$${} прочитан успешно $$$$$$$$'.format(url))

def main():
    main_url = 'http://tksiko.ru/'
    hrefs = []
    db_name = 'shop.db'    

    try:
        url_d = urllib.request.urlopen(main_url)
    except:
        print_url_error(main_url)
    else:
        page = url_d.read().decode('utf-8')
        print_url_sucsees(main_url)
    lev = int(sys.argv[1])   
    result = re.findall(r'\s*<a title="(.*?)" style="display\:block;" class="mainlevel" href="/(.*?)"', page) #Ищем главные разделы каталога товаров
    #site_dir = [{'name':result[i][0],'href':result[i][1],'sublevels':[]} for i in range(len(result))] #добавляем список разделов в виде словаря {имя,ссылка,список товаров}
    site_dir = [{'name':result[lev][0],'href':result[lev][1],'sublevels':[]}] #Для отладки берём только первый раздел каталога
    
    
    for level in site_dir:
        pk = 1
        table_name = ''.join(map(lambda name: name.capitalize(),level['href'].split("-")))
        with sqlite3.connect(db_name) as con:
            cur = con.cursor()
            cur.execute('CREATE TABLE {} (id INTEGER PRIMARY KEY, name VARCHAR(255), price REAL, img VARCHAR(125), type VARCHAR(31))'.format(table_name))
        url_level = main_url + level['href']
        try:
            url_d = urllib.request.urlopen(url_level)
        except:
            print_url_error(url_level)
        else:
            page = url_d.read().decode('utf-8')
            print_url_sucsees(url_level)
            
        result = re.findall(r'\s*<a title="(.*?)" style="display\:block;" class="sublevel" href="/(.*?)"', page) #Ищем названия подраздела товаровов и ссылку на него в каждом разделе каталога
        if len(result) == 0:
            level['sublevels'] = [{'name': level['name'], 'href': level['href'], 'products':[]}]
        else:
            level['sublevels'] = [{'name':i[0],'href':i[1],'products':[]} for i in result] #добавляем в каждый раздел каталога список подразделов в виде списка словарей {имя,ссылка,список товаров}

        for sublevel in level['sublevels']:
            url_sublevel = main_url + sublevel['href']
            try:
                url_d = urllib.request.urlopen(url_sublevel)
            except:
                print_url_error(url_sublevel)
            else:
                page = url_d.read().decode('utf-8')
                print_url_sucsees(url_sublevel)

            names = re.findall(r'<a style="font-size\:16px; font-weight\:bold;" href="(?:.*?)">(.*?)</a>', page)
            prices = re.findall(r'<p>\s*<(?:.*?)>\s*(Позвоните, чтобы уточнить цену|\d*\s*\d+\.\d+)', page)           
            #imgs = re.findall(r'<img src="(http\://tksiko\.ru/components/com\_virtuemart/.+?)"', page)
            #imgs = re.findall(r'<img src="(.*?)" (?:height="\d*" width="\d*" class="browseProductImage)?"', page)
            sublevel['products'] = [{'name':product[0], 'price':product[1], 'img': "" ,'type':""} for product in list(zip(names,prices))] #Добавляем в каждый подраздел список товаров, в котором товары хранятся в виде словарей {имя,цена,ссылка на изображение} 
            if len(sublevel['href'].split('/')) < 3: #определяем битая ли ссылка если да, то вводим имя подраздела вручную
                sublevel_name = sublevel['href'].split('/')[0]
            else:
                sublevel_name = input("Введите название подраздела({}): ".format(sublevel['name']))             
            
            for i,product in enumerate(sublevel['products']): 
                img_dir = 'shop/'+level["href"]+"/"+sublevel_name +"/"+sublevel_name+str(i)+'.jpg'
                product['img'] = img_dir
                product['type'] = sublevel['name']
                if product["price"] == 'Позвоните, чтобы уточнить цену' or product["price"] == '0.00':
                    product["price"] = 0.0
                else:
                    product["price"] = float(product["price"].replace(' ',''))
                #for_insert = [product['name'], product['price'],product['img'], product['type']]
                #print(for_insert)
                with sqlite3.connect(db_name) as con:
                    cur = con.cursor()
                    cur.execute('INSERT INTO {} VALUES (?,?,?,?,?)'.format(table_name),(pk, product['name'], product['price'],product['img'], product['type']))
                pk += 1
            #input("-----  Подраздел {} считан успешно. Перейти к следующему?".format(sublevel["name"]))
        
            
        #input("Раздел {} считан успешно. Перейти к следующему?".format(level["name"]))
        
        
    '''for level in site_dir:
        print('{} | ссылка {}'.format(level['name'], level['href']))
        for sublevel in level['sublevels']:
            print('-----  {} | ссылка {}'.format(sublevel['name'], sublevel['href']))
            for product in sublevel['products']:
                print('++++++++++++ {name:20} {price:20} {img}'.format(**product))'''
    

            
if __name__== "__main__":
    main()



