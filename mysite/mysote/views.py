from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hell World")

def detail(request,num,num2):
    return HttpResponse("detail-%s-%s" %(num,num2))

from mysote.models import Grades,Students
def grades(request):
    #去模型里取数据
    gradesList=Grades.objects.all()
    #将数据传递给模板,模板将渲染好的页面返回给浏览器
    return render(request,'mysote/grades.html',{"grades":gradesList})

def students(request):
    #studentList=Students.objects.all()
    #如果使用自定义模型Manager类 则修改对象objects
    studentList = Students.stuObj2.all()
    #查询集返回列表，可以使用返回下标的方法进行分页（不能是负数），类似于sql中的limit
    #studentList = Students.stuObj2.all()[0:3]  显示前三条数据
    return render(request, 'mysote/Students.html',
                  {"students": studentList,"num":10,"code":"<h1>啦啦啦</h1>"})


def stupage(request,page):
    "分页查询"
    page=int(page)
    studensList=Students.stuObj2.all()[(page-1)*2:page*2]
    return render(request, 'mysote/Students.html', {"students": studensList})

from django.db.models import Max,F,Q
def stusearch(request):
    "条件查询"
    studentList = Students.stuObj2.filter(sname__contains='超')
    #studentList = Students.stuObj2.aggregate(Max('sage'))
    return render(request, 'mysote/Students.html', {"students": studentList})
    """
    跨关联查询：处理join 语法：模型类名__属性字段__比较运算符
    描述学生表scontent中带有‘帅’内容的数据属于哪个班级的
    """
    # grade=Grades.objects.filter(studens__scontent__contains='帅')
    # print(grade)


    """
    F对象
    1.可以比较模型A属性和B属性 g=Grades.objects.filter(ggirlnum__gt=F('gboynum')
    2.支持算术运算g=Grades.objects.filter(ggirlnum__gt=F('gboynum'+20)
    Q对象
    1.条件为and模式，or操作Students.stuObj2.filter(Q(pk__lte=3)|Q(sage__gt=50))
    2.取反Students.stuObj2.filter(~Q(pk__lte=3)
    """

def gradesStudent(request,num):
    #在班级列表中点击某个班级显示学生
    grade=Grades.objects.get(pk=num)
    studentsList=grade.students_set.all()
    return render(request, 'mysote/Students.html', {"students": studentsList})

"""
    查询集的缓存
   每个查询集都包含一个缓存，来最小化对数据库的访问
   在新建的查询集中，缓存首次为空，在第一次对查询集求值会发生数据缓存
   django会将查询出来的数据做一个缓存并返回查询结构 以后查询直接使用查询集的缓存
"""

def addstudent(request):
    grade=Grades.objects.get(pk=1)
    stu=Students.createStudent("超哥",22,True,"超哥好帅",grade,False)
    stu.save()
    return HttpResponse('学生添加成功')
def addstudent2(request):
    grade=Grades.objects.get(pk=1)
    stu=Students.stuObj2.createStudent("周杰伦",22,True,"超哥好帅",grade,False)
    stu.save()
    return HttpResponse('又添加成功')

#HttpRequest的方法
def attribles(request):
   print(request.path)
   print(request.method)
   print(request.GET)
   print(request.POST)
   print(request.COOKIES)
   print(request.session)
   print(request.FILES)
   return HttpResponse('Response')

#获取get传递的数据
def get1(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    return HttpResponse(a+b)

def get2(request):
    a=request.GET.getlist('a')
    a1=a[0]
    a2=a[1]
    c=request.GET.get('c')
    return HttpResponse(a1+" "+a2+" "+c)

def showregister(request):
    return render(request,'mysote/register.html')

def regist(request):
    "post表单数据"
    name=request.POST.get("name")
    gender=request.POST.get("gender")
    age=request.POST.get("age")
    hobby=request.POST.getlist("hobby")
    print(name)
    print(hobby)
    return  HttpResponse('注册成功！')

def cookietest(request):
    "设置cookie值并访问"
    res=HttpResponse()
    #cookie=res.set_cookie('username','22')
    cookie=request.COOKIES #表示已存有cookie
    res.write("<h1>"+"cookie值是："+cookie['username']+"</h1>")
    return res

#HttpResponse子类—HttpResponseRedirect:服务器页面跳转 url重定向
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect

def  redirect1(request):
    "重定向"
    return redirect('/redirect2')
    #return HttpResponseRedirect('/redirect2')

def redirect2(request):
    # if request.is_ajax():
    #     a=JsonResponse({'json'})#子类JsonResponse,返回json数据 用于异步请求
    return HttpResponse("我是重定向后的页面")

"""
    http协议是无状态的 每次请求都是一个新的请求
    客户端和服务端的一次通信就是一次会话
    实现状态保持，在客户端或者服务端存储有关会话的数据
    cookie: 数据存储在客户端，有过期时间
    session:数据存储在服务端，在客户端用cookie存储session_id 
    Session状态保持的目的：
    在一段时间内跟踪1请求者的状态，可以跨页面访问当前请求者的数据 
    
    settings.py启用session后，每个HttpRequest对象都有一个session属性，是类似字典的对象
    key-value根据键获取session值
"""
def main(request):
    #登录成功后取session中用户名
    username=request.session.get('name',"游客")
    print(username)
    return render(request,'mysote/main.html',{"username":username})

def login(request):
    return render(request, 'mysote/login.html')

def showmain(request):
    print('测试session')
    username=request.POST.get('username')
    #将用户名存到session中
    request.session['name']=username
    return redirect('/main')

from django.contrib.auth import logout
def quit(request):
    "清除session"
    logout(request)
    #request.session.clear()
    #request.session.flush()
    return redirect('/main')


#url反向解析
def good(request,id):
    return render(request, 'mysote/Students.html', {"num": id})


def indexmain(request):
      return render(request, 'mysote/index.html')

def verifycode(request):
    "生成验证码"
    #y引入绘图模块
    from PIL import Image,ImageDraw,ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背影色，宽，高
    bgcolor=(random.randrange(20,100),random.randrange(20,100),random.randrange(20,100))
    width=100
    height=50
    #创建画面对象
    im=Image.new('RGB',(width,height),bgcolor)
    #创建画笔对象
    draw=ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy=(random.randrange(0,width),random.randrange(0,height))
        fill=(random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)
    #定义验证码的备选值
    str='1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
    #随机选取4个值作为验证码
    rand_str=''
    for i in range(0,4):
        rand_str += str[random.randrange(0,len(str))]
    #构造字体对象
    font=ImageFont.truetype(r'C:\Users\WDX\Desktop\ADOBEARABIC-REGULAR.OTF',40)
    #构造字体颜色
    fontcolor1=(255,random.randrange(0,255),random.randrange(0,255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5,2) ,   rand_str[0], font=font , fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50,2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    #释放画笔
    del draw
    #存入session,用于做进一步验证
    request.session['verifycode']=rand_str
    #内存文件操作
    import  io
    buf=io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf,'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(),'image/png')


def codefile(request):
    flag = request.session.get('flag', True)
    str = ""
    if flag == False:
        str = "请重新输入"
    request.session.clear()
    return render(request, 'mysote/verifycodefile.html',{"flag":str})

def codecheck(request):

    code1=request.POST.get('verifycode').upper()
    code2=request.session.get('verifycode').upper()
    if code1==code2:
        return render(request,'mysote/codesuccess.html')
    else:
        request.session['flag']=False
        return  redirect('/verifycodefile/')

#上传文件
def upfile(request):
    return render(request,'mysote/upfile.html')

import os
from django.conf import settings
def savefile(request):
    if request.method == "POST":
        f=request.FILES['file']#上传的文件描述
        #将文件存到本地服务器的目录
        filepath=os.path.join(settings.MDETA_ROOT,f.name)
        with open(filepath,'wb') as fp:
            for info in f.chunks():#以文件流的形式一段一段接收
                fp.write(info)
        return HttpResponse("上传文件成功")

    else:
        return HttpResponse("上传失败")

#分页 Paginator对象
def studentpage(request,pageid):
    allList=Students.stuObj2.all()

    paginator = Paginator(allList,3)
    page = paginator.page(pageid)

    return render(request,'mysote/Students.html',{"students":page})

#Ajax显示学生列表
def ajaxshowstu(request):
    stus=Students.stuObj2.all()

    list=[]
    for stu in stus:
        list.append([stu.sname,stu.scontent])
    return JsonResponse({"data":list})

'''celery的使用
1.任务：本质是一个python函数
2.队列：将要执行的任务放到队列里
3.工人：负责执行队列中的任务
4.代理：负责调度，在部署环境中使用redis
'''

def getdate(request,year,month,day):
    return  HttpResponse("Data is %s - %s - %s  " %(year,month,day))