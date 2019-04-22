from django.db import models
from .students import Students


class MarkSheet(models.Model):

    student_id = models.ForeignKey(Students, on_delete=models.PROTECT, to_field='roll_number')
    marks_maths = models.IntegerField()
    marks_chemistry = models.IntegerField()
    marks_physics = models.IntegerField()
    total = models.IntegerField()

    class CONSTANTS:
        NUM_OF_SUBJECTS = 3

    @classmethod
    def add_marks(cls, student_id, maths, chemistry, physics):

        # ---- Validating student_id ------
        student = Students.get_by_user_id(student_id)
        if student is None:
            return None
        marksheet_obj = cls(student_id=student.user_id, marks_maths=maths, marks_chemistry=chemistry,
                            marks_physics=physics)
        marksheet_obj.save()
        return marksheet_obj

    @classmethod
    def update_marks(cls, student_id, maths, chemistry, physics):

        # --- Check for existing record corresponding to the student_id ----------
        try:
            marksheet_obj = cls.objects.get(student_id=student_id)
            marksheet_obj.marks_maths = maths
            marksheet_obj.marks_chemistry = chemistry
            marksheet_obj.marks_physics = physics
            marksheet_obj.save()
            return marksheet_obj
        except cls.DoesNotExist:
            return None