# book1
包含静态爬虫，动态爬虫，和我个人网站
*静态爬虫  
*步骤：
1）	确认要爬取的网站为豆瓣读书，确认URL
2）	使用requests与beautifiulsoup库获取网页源代码
3）	使用浏览器查看源码，分析需要爬取的图片，标题等的特征
4）	使用findall函数获取数据存入列表中
5）	分析url爬取更多页数编写循环
6）	将得到的数据存入数据库
*动态爬虫：
*步骤
1）	编写seach()函数模拟浏览器登录京东输入零食点击搜索，使用wait.until函数判断是否加载出对应插件来完善函数
2）	编写getrouser()函数来获取数据，其中由于京东页面机制必须下拉页面图片和商品信息才能显示出来，所以我使用webdirver里的execute_script("window.scrollBy(0, 1000)")函数模仿用户下拉，实现页面全加载，在获取页面源码。
3）	分析页面源码提取提取的关键词，完善getrouser()函数返回数据
4）	编写main函数获得数据插入数据库
*djgango
*步骤：
1）	使用pycharm创建项目，先创建一个用户，在创建一个BOOK应用
2）	把我的静态爬虫文档导入到应用文档下，在view中应用，使用
def openbook(request):
    flag=0
    a,b,c,d=douban.getdetiles()
    ls = models.bookdetils.objects.all()
    for i in ls :
        if(i.id==1):
            flag=1
            break
    if(flag==0):
        for i in range(len(a)):
            models.bookdetils.objects.create(id=i,title=a[i],tiems=b[i],detile=d[i],imgs=c[i])
    ls = models.bookdetils.objects.all()
return render(request,'index.html',{'li':ls})
返回一个字典
其中models.bookdetils.objects.create是往数据库中插入数据
我写这个的目的是方便哪些没有mysql的用户也可以使用我的项目，不用连接mysql,
使用系统自带的SQLLIST3,方便使用。
3）	在book1的url中写两个PATH一个跳转到主页，一个详细页
4）	再详细页中使用获取的字典，显示数据
