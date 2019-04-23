__author__ = "Tavleen Kaur"
__email__ = "tavleen.k13@gmail.com"

from django.conf.urls import url
from .views import add_student, add_student_record, view_result

urlpatterns = [

    url(r'add/student/', add_student),
    url(r'add/marks/(\d+)', add_student_record),
    url(r'check/result/', view_result)
]