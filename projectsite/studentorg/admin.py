from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember  

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Organization)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'lastname', 'middlename', 'program')
    list_filter = ('program', )
    search_fields = ('lastname', 'firstname', 'middlename', 'student_id')
    ordering = ('lastname', 'student_id')

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ('student', 'organization', 'date_joined')
    list_filter = ('organization', )
    search_fields = ('student', 'organization')
    ordering = ('student', 'organization')

    def get_member_program(self, obj):
        try:
            member = Student.objects.get(pk=obj.student_id)
            return member.program
        except Student.DoesNotExist:
            return None



