from django.test import TestCase
from models import Subject

print(Subject.objects.get(id=1).count_comments())
# Create your tests here.
