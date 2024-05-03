from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('admin',views.admin,name='admin'),
    path('log',views.login,name='login'),
    path('teach',views.teacherpage,name='teacherhome'),
    path('reg',views.register,name='register'),
    path('logfn',views.loginfunction,name='loginfunction'),
    path('addcourse',views.addcourse,name='acc'),
    path('tech',views.teacherregister,name='treg'),
    path('edit/<int:tid>',views.editteacher,name='editthr'),
    path('editt/<int:tid>',views.editteacher_fn,name='editteacherf'),
    path('dltpg',views.dltpg,name='dltpg'),
    path('dltfn',views.dltfn,name='dltfn'),
    

]