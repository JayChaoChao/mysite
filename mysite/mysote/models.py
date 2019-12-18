from django.db import models

# Create your models here.

class Grades(models.Model):
	"班级类对象模型"
	gname=models.CharField(max_length=20)
	gdate=models.TimeField()
	ggirlnum=models.IntegerField()
	gboynum=models.IntegerField()
	isDelete=models.BooleanField(default=False)
	def __str__(self):
		return "%s" %(self.gname)
	# class Meta:
	# 	#用于设置元信息
	# 	db_table="grades"#数据库表名

class StudentsManager(models.Manager):
	"""
	自定义模型管理器Manager类
	模型管理器是Django的模型与数据库进行交互的接口，一个模型可以有多个模型管理器
	作用：	1.向管理器中添加额外的方法
			2.修改管理器返回的原始查询集（重写get_queryset()方法）
	"""
	def get_queryset(self):
		"""
		查询集表示丛数据库获取的对象的集合
		查询集可以有多个过滤器
		过滤器就是一个函数，基于所给的参数限制查询集的结果
		查询集就像sql语句，过滤器就像where条件

		默认原始查询集返回所有对象数据，可以添加多个过滤
		创建查询集不会带来任何数据的访问，只有查询数据时才访问数据库
		"""
		return super(StudentsManager,self).get_queryset().filter(isDelete=False)



	def createStudent(self, name, age, gender, content, grade, isD=False):
		"在自定义管理器中添加一个创建对象的方法"
		stu=self.model()
		#print(type(grade))
		stu.sname=name
		stu.sage=age
		stu.sgender=gender
		stu.scontent=content
		stu.sgrade=grade
		stu.isDelete=isD
		return stu


class Students(models.Model):
	"学生类对象模型"
	#stuObj=models.Manager()#自定义模型管理器
	stuObj2=StudentsManager()
	sname=models.CharField(max_length=20)
	sgender=models.BooleanField(default=True)
	sage=models.IntegerField()
	scontent=models.CharField(max_length=20)
	isDelete=models.BooleanField(default=False)
	#关联外键
	sgrade=models.ForeignKey("Grades",on_delete=models.CASCADE)
	def __str__(self):
		return self.sname
	# class Meta:
	# 	#用于设置元信息
	# 	db_table="students"
	# 	ordering=['id']#排序字段，获取对象列表时使用，负号降序

	#在模型中添加一个类方法创建对象
	@classmethod
	def createStudent(cls,name,age,gender,content,grade,isD=False):
		stu=cls(sname=name,sage=age,sgender=gender,scontent=content,sgrade=grade,isDelete=isD)
		return stu

#富文本
from tinymce.models import HTMLField
class Text(models.Model):
	str=HTMLField()


