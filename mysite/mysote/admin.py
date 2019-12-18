from django.contrib import admin

# Register your models here.
from .models import Grades,Students
from .models import Text

#添加一个班级同时添加多个学生
class StudentsInfo(admin.TabularInline):#StackedInline
	model = Students
	extra = 2

#注册
class GradesAdmin(admin.ModelAdmin):
	inlines = [StudentsInfo]
	#列表页属性
	list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
	list_filter = ['gname']
	search_fields = ['gname']
	list_per_page = 5
	#添加 修改页属性---不能同时使用
	#fields = ['ggirlnum','gboynum','isDelete','gname','gdate']
	#分组
	fieldsets = [
		("num",{"fields":['ggirlnum','gboynum']}),
		("base",{"fields":['gname','gdate']})
	]

admin.site.register(Grades,GradesAdmin)

#使用装饰器注册
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
	def gender(self):
		if self.sgender:
			return "男"
		else:
			return "女"
	#设置页面名称
	gender.short_description="性别"
	#执行动作的位置
	actions_on_top = True
	actions_on_bottom = True
	list_display = ['pk', 'sname', 'sage', gender, 'scontent','sgrade', 'isDelete']
	list_filter = ['sname']
	search_fields = ['sname']
	list_per_page = 2

#admin.site.register(Students,StudentsAdmin)

admin.site.register(Text)