class BDTB:

    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()
    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            response = urllib.request.urlopen(url)
            return response.read().decode('utf-8')


    #获取帖子标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1)  #测试输出
            return result.group(1).strip()
        else:
            return None

    #获取帖子一共有多少页
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    #获取每一层楼的内容,传入页面内容
    def getContent(self,page):
        pattern = re.compile('d_post_content j_d_post_content ">(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        new = []
        for item in items:
            new.append(self.tool.replace(item))
        return new
