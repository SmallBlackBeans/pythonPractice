import requests
from urllib.parse import urlencode


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    data = json.get('data')
    if data != None:
        for item in data:
            title = item.get('title')
            images = item.get('image_detail')
            for image in images:
                yield {
                    'image': image.get('url'),
                    'title': title
                }


import os
from hashlib import md5

def save_image(item):
    itemPath = item.get('title')
    if (not os.path.exists(itemPath)) == False:
        os.mkdir(itemPath)
    try:
        response:requests.Response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(itemPath,md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
             print('%s已下载',file_path)
    except requests.ConnectionError as e:
        print('下载失败')


from multiprocessing.pool import Pool
def main(offset):
    json  = get_page(offset)
    for item in get_images(json):
        save_image(item)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()