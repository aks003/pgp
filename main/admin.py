from django.contrib import admin

from main.models import deliverables_db, evaluation_db, phase_db, professor_db, project_db, rubrics_db, student_db

# Register your models here.
admin.site.register(professor_db)
admin.site.register(student_db)
admin.site.register(project_db)
admin.site.register(phase_db)
admin.site.register(deliverables_db)
admin.site.register(rubrics_db)
admin.site.register(evaluation_db)