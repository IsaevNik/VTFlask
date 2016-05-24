import urllib.request
import re
import os
import shutil

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
    lev = 11    
    result = re.findall(r'\s*<a title="(.*?)" style="display\:block;" class="mainlevel" href="/(.*?)"', page) #Ищем главные разделы каталога товаров
    #site_dir = [{'name':result[i][0],'href':result[i][1],'sublevels':[]} for i in result] #добавляем список разделов в виде словаря {имя,ссылка,список товаров}
    site_dir = [{'name':result[lev][0],'href':result[lev][1],'sublevels':[]}] #Для отладки берём только первый раздел каталога
    
    
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
        if len(result) == 0:
            level['sublevels'] = [{'name': level['name'], 'href': level['href'], 'products':[]}]
        else:
            level['sublevels'] = [{'name':i[0],'href':i[1],'products':[]} for i in result] #добавляем в каждый раздел каталога список подразделов в виде списка словарей {имя,ссылка,список товаров}
        if os.path.exists(level['href']):
            shutil.rmtree(level['href']) 
        os.mkdir(level['href'])

        for j,sublevel in enumerate(level['sublevels']):
            url_sublevel = main_url + sublevel['href']
            #sublevel_dir = sublevel['href'].split('/')[0]
            sublevel_dir = sublevel['href'].split('/')[0]+str(j)#Если есть некрасивые ссылки
            dest_dir = os.path.join(level['href'],sublevel_dir)
            os.mkdir(dest_dir)
            try:
                url_d = urllib.request.urlopen(url_sublevel)
            except:
                print_url_error(url_sublevel)
            else:
                page = url_d.read().decode('utf-8')
                print_url_sucsees(url_sublevel)

            names = re.findall(r'<a style="font-size\:16px; font-weight\:bold;" href="(?:.*?)">(.*?)</a>', page)
            prices = re.findall(r'<p>\s*<(?:.*?)>\s*(Позвоните, чтобы уточнить цену|\d*\s*\d+\.\d+)', page)           
            imgs = re.findall(r'<img src="(http\://tksiko\.ru/components/com\_virtuemart/.+?)"', page)
            #imgs = re.findall(r'<img src="(.*?)" (?:height="\d*" width="\d*" class="browseProductImage)?"', page)
            sublevel['products'] = [{'name':product[0], 'price':product[1], 'img': product[2]} for product in list(zip(names,prices,imgs))] #Добавляем в каждый подраздел список товаров, в котором товары хранятся в виде словарей {имя,цена,ссылка на изображение} 
            print(len(sublevel['products']))
            
            for i,product in enumerate(sublevel['products']):
                img_dir = sublevel_dir+str(i)+'.jpg'
                urllib.request.urlretrieve(product['img'], os.path.join(dest_dir, img_dir))
            
            
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



