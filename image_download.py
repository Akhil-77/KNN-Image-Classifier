
# Code used for creating the database

import os
import requests # pip install requests 
from bs4 import BeautifulSoup # pip install bs4 


Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'


u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
} #write: 'my user agent' in browser to get your browser user agent details

Image_Folder = 'Images_1'

def main():
    if not os.path.exists(Image_Folder):
        os.mkdir(Image_Folder)
    download_images()

def download_images():
    data = input('Enter your search keyword: ')
    name_intial = ("forest")
    num_images = int(input('Enter the number of images you want: '))
    
    print('Searching Images....')
    
    search_url = Google_Image + 'q=' + data 
    
   
    response = requests.get(search_url, headers=u_agnt)
    html = response.text 

    b_soup = BeautifulSoup(html, 'html.parser') 
    results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
    
    count = 0
    imagelinks= []
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count = count + 1
            if (count >= num_images):
                break
            
        except KeyError:
            continue
    
    print(f'Found {len(imagelinks)} images')
    print('Downloading...')


    for i, imagelink in enumerate(imagelinks):
        # open each image link and save the file
        response = requests.get(imagelink)
        # print(i)
        imagename = Image_Folder + '/' + name_intial + str(i+401) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)
        i+=1

    print('Download Completed!')
    

if __name__ == '__main__':
    main()


# All the keywords used for scraping

# forest 
# jungle 
# Amazon rainforest 
# rainforest 
# taiga rainforest 
# Congo rainforest

# Desert
# Sahara Desert
# Gobi Desert
# Empty Quarter
# Thar Desert
# Namib Desert