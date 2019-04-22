from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.students import Students
from .models.marksheet import MarkSheet
from .templates import *
from datetime import datetime
import logging


# @api_view(['GET'])
# def index(request):
#     return render(request, template_name='admin.html')

# @api_view(['POST'])
# def admin_signup(request):
#
#     data = request.data
#     email_id = data.get('email_id', None)
#     name = data.get('name', None)
#     password = data.get('password', None)
#     dob = data.get('dob', None)
#
#     if email_id is None or password is None or name is None:
#         logging.info("Incomplete Form.")
#         return Response(data={"Incomplete/missing form values"}, status=400)
#
#     email_regex = r"[^@]+@[^@]+\.[^@]+"
#     # TODO :: validation for dob ----
#     if not re.match(email_regex, email_id) or len(password) not in range(8,31):
#         logging.info("Invalid format of input data")
#         return Response(data={"Invalid details"}, status=400)
#
#     admin = Admin.admin_signup(email_id, name, password, dob)
#     if admin is None:
#         logging.info("Error signing up admin. Admin with email {} already exists".format(email_id))
#         return Response(data={'User Already Exists'}, status=400)
#     return Response(data={"Admin signed up successfully"}, status=200)

# @api_view(['POST'])
# def admin_login(request):
#
#     data = request.data
#     email_id = data.get('email_id', None)
#     password = data.get('password', None)
#     admin = Admin.admin_login(email_id, password)
#     if admin is None:
#         logging.info("Invalid Credentials")
#         return Response(data={"Invalid Credentials"}, status=400)
#
#     request.session['is_logged_in'] = True
#     # return render(request, template_name='templates/login.html', )
#     return Response(data={"Logged in"}, status=200)
#
#
# @api_view(['POST'])
# def admin_logoff(request):
#
#     data = request.data
#     email_id = data.get('email_id', None)
#     is_admin = Admin.is_admin(email_id)
#     if not is_admin:
#         logging.info("Invalid email id")
#         return Response(data={"Error logging off"}, status=400)
#     if request.session.get('is_logged_in'):
#         request.session['is_logged_in'] = False
#     return Response(data={"Logged out"}, status=200)
#

@api_view(['POST'])
def add_student(request):

    if not request.user.is_authenticated:
        logging.info("Can't add student. Unauthenticated")
        return Response(data={"Authentication Failed"}, status=403)

    data = request.data
    roll_number = data.get('roll_number')
    name = data.get('name')
    dob = data.get('dob')

    if roll_number is None or name is None or dob is None:
        logging.info("Insufficient information to save student details")
        return Response(data={"Invalid data"}, status=400)

    try:
        datetime.strptime(dob, '%d-%m-%Y')
    except ValueError:
        logging.info("Incorrect data format, should be DD-MM-YYYY")
        return Response(data={"Incorrect data format"}, status=400)

    student = Students.add_student(roll_number, name, dob)
    if student is None:
        logging.info("Error saving Student info")
        return Response(data={"Error"}, status=500)

    return Response(data={"Student info added"}, status=2000)

@api_view(['POST'])
def add_student_record(request, roll_number):

    if not request.session.get('is_logged_in'):
        logging.info("Can't add student record, user not logged in")
        return Response(data={"User not logged in"}, status=400)
    data = request.data
    maths_marks = data.get('maths')
    chem_marks = data.get('chem')
    phy_marks = data.get('phy')
    student = Students.get_by_roll_number(roll_number)
    if student is None:
        logging.info("Invalid Roll Number. Try again")
        return Response(data={"Invalid Roll Number"}, status=400)

    marks_added = MarkSheet.add_marks(roll_number, maths_marks, chem_marks, phy_marks)
    if marks_added is None:
        logging.info("Error adding marks")
    return Response(data={"Record Saved"}, status=200)