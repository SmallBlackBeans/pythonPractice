# coding: utf-8

import urllib
import re
from urllib import request
from Spider.SpiderTool import SpiderTool


class BDTB:
    # 传入参数是否只看楼主的帖子
    def __init__(self, baseUrl, seeLz, floorTag):
        self.baseUrl = baseUrl
        self.seeLz = '?see_lz=' + str(seeLz)
        self.tool = SpiderTool()
        self.file = None
        self.floor = 1
        self.defaultTitle = u'百度贴吧'
        self.floorTag = floorTag

    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.seeLz + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except urllib.request.URLError as e:
            if hasattr(e, 'reason'):
                print(u'链接百度贴吧失败，原因：%s' % e.reason)
                return None

    # 获取帖子标题
    '''
    <h3 class="core_title_txt pull-left text-overflow  " title="纯原创我心中的NBA2014-2015赛季现役50大" style="width: 396px">纯原创我心中的NBA2014-2015赛季现役50大</h3>
    '''

    def getTitle(self, page):
        pattern = re.compile('<h3 class="core_title_txt.*?">(.*?(?#标题))</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            # 这里注意group()是最外层 group(1)是后面每一组都添加到后面
            return result.group(1).strip()
        else:
            return None

    # 获取帖子页数
    '''
    <li class="l_reply_num" style="margin-left:8px"><span class="red" style="margin-right:3px">141</span>回复贴，共<span class="red">5</span>页</li>
    '''

    def getPageNum(self, page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # 提取正文
    '''
    <div id="post_content_53018668923" class="d_post_content j_d_post_content ">        
        很多媒体都在每赛季之前给球员排个名，我也有这个癖好…………，我会尽量理性的分析球队地位，个人能力等因素，
        评出我心目中的下赛季50大现役球员，这个50大是指预估他本赛季在篮球场上对球队的影响力……不是过去的荣誉什么的，
        所以难免有一定的主观性……如果把你喜欢的球星排低了，欢迎理性讨论！
        <img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=557ae4d4fadcd100cd9cf829428947be/a9d6277f9e2f0708468564d9eb24b899a801f263.jpg" pic_ext="jpeg" pic_type="0" width="339" height="510">
        <br><br><br><br>
        状元维金斯镇楼<br>
        P.S 1 我每天都至少更新一个，不TJ。<br>   
        2 今年的新秀我就不考虑了，没上赛季参照
    </div>
    '''

    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTitle(self, title):
        if title is not None:
            self.file = open(title + '.txt', 'wb+')
        else:
            self.file = open(self.defaultTitle + '.txt', 'wb+')

    def writteData(self, contents):
        for item in contents:
            if self.floorTag == '1':
                floorLine = "\n" + str(
                    self.floor) + u"-------------------------------------------------------------------\n"
                self.file.write(floorLine.encode('utf-8'))
            self.file.write(item)
            self.floor += 1

    def start(self):
        # 主页
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        if pageNum == None:
            print("URL 已失效，请重试")
            return

        title = self.getTitle(indexPage)
        self.setFileTitle(title)

        try:
            print('该帖子共有 ' + str(pageNum) + '页')
            for i in range(1, int(pageNum) + 1):
                print("正在写入第" + str(i) + "页")
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writteData(contents)
        except IOError as e:
            print('写入异常 原因' + e.message)
        finally:
            print('写入任务完成')


# 3138733512
print(u"请输入帖子代号")
baseURL = 'http://tieba.baidu.com/p/' + str(input(u'http://tieba.baidu.com/p/'))
seeLz = input("是否只获取楼主的发言，是1否0\n")
floorTag = input("是否写入楼层信息，是1否0\n")
bdtb = BDTB(baseURL, seeLz, floorTag)
bdtb.start()
