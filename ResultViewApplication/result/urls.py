from django.conf.urls import url
from .views import add_student, add_student_record

urlpatterns = [

    url(r'add/student/', add_student)

]