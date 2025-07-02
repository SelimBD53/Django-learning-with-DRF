from django.apps import AppConfig
from watson import search

class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
    def ready(self):
        import app1.signals
        Student = self.get_model('Student')
        search.register(Student, fields=('user__username','user__first_name','user__last_name','user__email','roll_no','dept','phone'))
