__author__ = "Tavleen Kaur"
__email__ = "tavleen.k13@gmail.com"

from django.db import models
from .students import Students

class MarkSheet(models.Model):

    roll_number = models.ForeignKey(Students, on_delete=models.PROTECT, to_field='roll_number')
    marks_maths = models.IntegerField()
    marks_chemistry = models.IntegerField()
    marks_physics = models.IntegerField()
    total = models.IntegerField()

    class Constants:
        NUM_OF_SUBJECTS = 3

    @classmethod
    def add_marks(cls, roll_number, maths, chemistry, physics):

        # ---- Validating roll_number ------
        student = Students.get_by_roll_number(roll_number)
        if student is None:
            return None
        total = maths + chemistry + physics
        roll_number = student.roll_number
        marksheet_obj = cls(roll_number_id=roll_number, marks_maths=maths, marks_chemistry=chemistry,
                            marks_physics=physics, total=total)
        marksheet_obj.save()
        return marksheet_obj


    @classmethod
    def get_marks(cls, roll_number):
        try:
            marks = cls.objects.get(roll_number_id=roll_number)
            return marks
        except cls.DoesNotExist:
            return None


    @classmethod
    def update_marks(cls, roll_number, maths, chemistry, physics):

        # --- Check for existing record corresponding to the student_id ----------
        try:
            marksheet_obj = cls.objects.get(roll_number_id=roll_number)
            marksheet_obj.marks_maths = maths
            marksheet_obj.marks_chemistry = chemistry
            marksheet_obj.marks_physics = physics
            marksheet_obj.save()
            return marksheet_obj
        except cls.DoesNotExist:
            return None