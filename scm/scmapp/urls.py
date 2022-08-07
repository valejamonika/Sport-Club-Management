from django.urls import path

from .import views

urlpatterns = [
            path('',views.index,name='index'),
            path('user',views.user,name='user'),
            path('admin1',views.admin1,name='admin1'),
            path('user_reg',views.user_reg,name='user_reg'),
            path('for_pas',views.for_pas,name='for_pas'),
            path("user_test",views.user_test,name="user_test"),
            path('user_check',views.user_check,name='user_check'),
            path("user_logout",views.user_logout,name="user_logout"),
            path("show_event",views.show_event,name="show_event"),
            path("ground_booking",views.ground_booking,name="ground_booking"),
            path("data_ground_booking",views.data_ground_booking,name="data_ground_booking"),


]