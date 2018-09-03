# -*- coding: utf-8 -*-

"""
    @Time    : 2018/8/21 上午10:57
    @Author  : hanxiaocu
    @File    : spider.py
    
    爬取搜狗词库
"""

import os
import sys
import time

import requests
from bs4 import BeautifulSoup, Tag, element

# 设置项目路径 方便导入包
PROJECT_PATH = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
))
sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(PROJECT_PATH, '搜狗词库抓取&解析'))

import configs
from store.store import DBToMysql
from utils.tools import UtilLogger


def get_html_text(url):
    try:
        r = requests.get(url, timeout=15, stream=True)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return -1


class Sougou_spider():

    def __init__(self):
        self.store = DBToMysql(configs.LOCAL_MYSQL_SOUGOU)
        self.logger = UtilLogger('SougouSpider',
                                 os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log_sougou_spider.log'))

    def cate_ext(self, html, type1):

        res = []
        soup = BeautifulSoup(html, 'lxml')
        cate_list = soup.find('div', {'id': 'dict_cate_show'})
        list = cate_list.find_all('a')
        for a in list:
            type2 = a.text.replace('"', '')
            url = 'http://pinyin.sougou.com' + a['href'] + '/default/{}'
            res.append({
                'url': url,
                'type1': type1,
                'type2': type2
            })
        return res

    def list_ext(self, html, type1, type2):

        res = []
        try:
            soup = BeautifulSoup(html, 'lxml')

            def detail_div(tag):
                return tag.get('class') == 'dict_detail_block' or tag.get('class') == 'dict_detail_block odd'

            detail_divs = soup.find_all(detail_div(html))

            for data in detail_divs:
                div: element.Tag = data
                name = div.find('div', class_='detail_title').a.text
                url = div.find('div', class_='dict_dl_btn').a['href']
                res.append({'filename': type1 + '_' + type2 + '_' + name,
                            'type1': type1,
                            'type2': type2,
                            'url': url,
                            })
        except Exception as e:
            print('解析失败')
            return -1

    def start(self):
        cate_list = self.store.find_all('sougou_cate')
        for cate in cate_list:
            type1 = cate['type1']
            type2 = cate['type2']
            for i in range(1, int(cate['page']) + 1):
                print('正在解析{}的第{}页'.format(type1 + type2, i))
                url = cate['url'].format(i)
                html = get_html_text(url)
                if html != -1:
                    res = self.list_ext(html, type1, type2)
                    self.log.info('正在解析页面 {}'.format(url))
                    for data in res:
                        self.store.save_one_data('sougou_detail', data)
                        self.log.info('正在存储数据{}'.format(data['filename']))
                time.sleep(3)


class Download_scel():
    '''下载词库'''

    def __init__(self):
        self.store = DBToMysql(configs.LOCAL_MYSQL_SOUGOU)
        self.logger = UtilLogger('SougouDownloader',
                                 os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log_sougou_downloader.log'))

    def get_html_content(self, url):
        try:
            r = requests.api.get(url, timeout=30, stream=True)
            r.raise_for_status()
            return r.content
        except Exception as e:
            return -1

    def download_file(self, content, filename):
        path = os.path.join(configs.SECL_DIR + '/' + filename)
        with open(path + '.scel', 'wb') as f:
            f.write(content)
            print('{}词库文件保存完毕'.format(filename))

    def strip_wd(self, s):
        '''
        去除字符串中的非法字符
        :param s:
        :return:
        '''
        kwd = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
               '(', ')', '.', '/', '|', '>', '<', '\\', '*', '"', '“', ]
        ans = ''
        for i in s:
            if i not in kwd:
                ans += i
        return ans


    def start(self):
        # 从数据库检索记录
        res = self.store.find_all('sougou_detail')
        self.log.warn('一共有{}条词库等待下载'.format(len(res)))
        for data in res:
            content = self.get_html_content(data['url'])
            filename = self.strip_wd(data['filename'])
            # 如果下载失败，我们等三秒再重试
            if content == -1:
                time.sleep(3)
                self.log.info('{}下载失败 正在重试'.format(filename))
                content = self.get_html_content(data[1])
            self.download_file(content, filename)
            self.log.info('正在下载文件{}'.format(filename))
            time.sleep(1)


if __name__ == '__main__':
    Sougou_spider().cate_ext(get_html_text('https://pinyin.sogou.com/dict/cate/index/167'),'城市信息')
    #Download_scel().start()