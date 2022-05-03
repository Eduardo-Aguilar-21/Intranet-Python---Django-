from django.contrib import admin


from Notas.models import TipoUsuario, Usuario, Distrito, Carrera, Curso, Estudiante
# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Distrito)
admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(Estudiante)
