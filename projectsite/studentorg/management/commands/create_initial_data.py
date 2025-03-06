from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember    

class Command(BaseCommand):
    help = "Create initial data for studentorg app"

    def handle(self, *args, **kwargs):
        self.fake = Faker()
        self.fake_ph = Faker('en_PH')
        self.create_organization(10)
        self.create_students(50)
        self.create_membership(10)

    def create_organization(self, count):
        for _ in range(count):
            words = [self.fake.word() for _ in range(2)]
            organization_name = " ".join(words)
            college = College.objects.order_by('?').first()
            if college:
                Organization.objects.create(
                    name=organization_name.title(),
                    college=college,
                    description=self.fake.sentence()
                )
            else:
                self.stdout.write(self.style.ERROR('No colleges found'))
        self.stdout.write(self.style.SUCCESS('Organizations created successfully'))
        
    def create_students(self, count):
        for _ in range(count):
            program = Program.objects.order_by('?').first()
            if program:
                Student.objects.create(
                    student_id=f"{self.fake_ph.random_int(2020,2024)}-{self.fake_ph.random_int(1,8)}-{self.fake_ph.random_number(digits=4)}",
                    lastname=self.fake_ph.last_name(),
                    frstname=self.fake_ph.first_name(),
                    middlename=self.fake_ph.first_name(),
                    program=program
                )
            else:
                self.stdout.write(self.style.ERROR('No programs found'))
        self.stdout.write(self.style.SUCCESS('Students created successfully'))
    
    def create_membership(self, count):
        for _ in range(count):
            student = Student.objects.order_by('?').first()
            organization = Organization.objects.order_by('?').first()
            if student and organization:
                OrgMember.objects.create(
                    student=student,
                    organization=organization
                )
            else:
                if not student:
                    self.stdout.write(self.style.ERROR('No students found'))
                if not organization:
                    self.stdout.write(self.style.ERROR('No organizations found'))
        self.stdout.write(self.style.SUCCESS('Memberships created successfully'))