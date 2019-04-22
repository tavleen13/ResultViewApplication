from django.db import models
import logging


class Students(models.Model):
    roll_number = models.IntegerField(unique=True, blank=False, null=False)
    name = models.CharField(max_length=200)
    dob = models.DateField()

    class Meta:
        db_table = 'students'

    @classmethod
    def get_by_roll_number(cls, roll_number):
        try:
            return cls.objects.get(roll_number=roll_number)
        except cls.DoesNotExist:
            return None

    @classmethod
    def add_student(cls, roll_number, name, dob):
        try:
            cls.objects.get(roll_number=roll_number)
            logging.info("Student Already Exists with roll_number {}. Can't add again".format(roll_number))
            return None
        except cls.DoesNotExist:
            obj = cls(roll_number=roll_number, dob=dob, name=name)
            obj.save()
            return obj

    @classmethod
    def update_student_info(cls, roll_number, name, dob):
        try:
            student = cls.objects.get(roll_number=roll_number)
            student.name = name
            student.dob = dob
            student.save()
            return student
        except cls.DoesNotExist:
            logging.info("Can't update Student as roll_number {} is invalid".format(roll_number))
            return None

    @classmethod
    def remove_student(cls, roll_number):
        try:
            obj = cls.objects.get(roll_number=roll_number)
            obj.delete()
        except cls.DoesNotExist:
            logging.info("Can't remove student record as roll_number {} invalid".format(roll_number))