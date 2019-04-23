__author__ = "Tavleen Kaur"
__email__ = "tavleen.k13@gmail.com"


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.students import Students
from .models.marksheet import MarkSheet
from datetime import datetime
import logging


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
        datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        logging.info("Incorrect data format, should be YYYY-MM-DD")
        return Response(data={"Incorrect data format"}, status=400)

    student = Students.add_student(roll_number, name, dob)
    if student is None:
        logging.info("Error saving Student info")
        return Response(data={"Error"}, status=500)
    return Response(data={"Student info added"}, status=200)


@api_view(['POST'])
def add_student_record(request, roll_number):

    if not request.user.is_authenticated:
        logging.info("Can't add student. Unauthenticated")
        return Response(data={"Authentication Failed"}, status=403)
    data = request.data
    maths_marks = data.get('maths')
    chem_marks = data.get('chemistry')
    phy_marks = data.get('physics')
    student = Students.get_by_roll_number(roll_number)
    if student is None:
        logging.info("Invalid Roll Number. Try again")
        return Response(data={"Invalid Roll Number"}, status=400)

    marks_added = MarkSheet.add_marks(roll_number, maths_marks, chem_marks, phy_marks)
    if marks_added is None:
        logging.info("Error adding marks")
    return Response(data={"Record Saved"}, status=200)


@api_view(['POST'])
def view_result(request):

    data = request.data
    roll_number = data.get('roll_number')
    dob = data.get('dob')
    student = Students.get_by_roll_number(roll_number)
    if student is None or (datetime.strptime(dob, '%Y-%m-%d').date() != student.dob):
        logging.info("Invalid roll number {} or DOB {}".format(roll_number, dob))
        return Response(data={"Invalid data"}, status=400)

    marksheet = MarkSheet.get_marks(roll_number)
    marks_in_maths = marksheet.marks_maths
    marks_in_chem = marksheet.marks_chemistry
    marks_in_phys = marksheet.marks_physics
    total = marksheet.total

    try:
        percentage = total / (100 * MarkSheet.Constants.NUM_OF_SUBJECTS)
        percentage = percentage * 100
    except ZeroDivisionError:
        logging.info("Error: Num of subjects can not be 0")
        return Response(data={"Error fetching marks"}, status=400)

    return Response(data={"maths": marks_in_maths, "chemistry": marks_in_chem, "physics": marks_in_phys,
                          "percentage": percentage}, status=200)