import urllib.request
import re
import os

def print_url_error(url):
    print('Ошибка при открытии ', url)

def print_url_sucsees(url):
    print('$$$$$$$$${} прочитан успешно $$$$$$$$'.format(url))

def main():
    main_url = 'http://tksiko.ru/'
    hrefs = []
    
    try:
        url_d = urllib.request.urlopen(main_url)
    except:
        print_url_error(main_url)
    else:
        page = url_d.read().decode('utf-8')
        print_url_sucsees(main_url)
        
    result = re.findall(r'\s*<a title="(.*?)" style="display\:block;" class="mainlevel" href="/(.*?)"', page) #Ищем главные разделы каталога товаров
    #site_dir = [{'name':result[i][0],'href':result[i][1],'sublevels':[]} for i in result] #добавляем список разделов в виде словаря {имя,ссылка,список товаров}
    site_dir = [{'name':result[1][0],'href':result[1][1],'sublevels':[]}] #Для отладки берём только первый раздел каталога
    
    
    for level in site_dir:
        
        url_level = main_url + level['href']
        try:
            url_d = urllib.request.urlopen(url_level)
        except:
            print_url_error(url_level)
        else:
            page = url_d.read().decode('utf-8')
            print_url_sucsees(url_level)
            
        result = re.findall(r'\s*<a title="(.*?)" style="display\:block;" class="sublevel" href="/(.*?)"', page) #Ищем названия подраздела товаровов и ссылку на него в каждом разделе каталога
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
            prices = re.findall(r'<p>\s*<(?:.*?)>\s*(Позвоните, чтобы уточнить цену|\d+\.\d+)', page)            
            imgs = re.findall(r'<img src="(.*?)" height="\d*" width="\d*" class="browseProductImage"', page)
            sublevel['products'] = [{'name':product[0], 'price':product[1], 'img': product[2]} for product in list(zip(names,prices,imgs))] #Добавляем в каждый подраздел список товаров, в котором товары хранятся в виде словарей {имя,цена,ссылка на изображение} 
            input("-----  Подраздел {} считан успешно. Перейти к следующему?".format(sublevel["name"]))
            
        input("Раздел {} считан успешно. Перейти к следующему?".format(level["name"]))
        
    for level in site_dir:
        print('{} | ссылка {}'.format(level['name'], level['href']))
        for sublevel in level['sublevels']:
            print('-----  {} | ссылка {}'.format(sublevel['name'], sublevel['href']))
            for product in sublevel['products']:
                print('++++++++++++ {name:20} {price:20} {img}'.format(**product))
    

            
if __name__== "__main__":
    main()



