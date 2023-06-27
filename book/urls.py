from django.urls import path
from book import views
app_name="book"

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('add/',views.add,name="add"),
    path('add1/',views.add1,name="add1"),
    path('view1/',views.view1,name="view1"),
    path('students',views.students,name="students"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('fact',views.fact,name="fact"),
    path('operation', views.operation, name="operation"),
    path('viewbook/<int:p>',views.viewbook,name='viewbook'),
    path('deletebook/<int:p>',views.deletebook,name='deletebook'),
    path('updatebook/<int:p>', views.updatebook, name='updatebook'),
    path('search/',views.search,name='search'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    ]