from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    id=models.IntegerField(primary_key=True)
    nomtipusu=models.CharField(max_length=20)
    esttipusu=models.IntegerField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nomtipusu, str(self.esttipusu))

class Usuario(models.Model):

    id=models.IntegerField(primary_key=True)
    nomusu=models.CharField(max_length=20)
    conusu=models.CharField(max_length=30)
    estusu=models.IntegerField()
    #tipousu =models.OneToOneField(to='TipoUsuario', to_field='id', null=True, blank=True, on_delete=models.CASCADE)
    tipousu=models.ForeignKey(TipoUsuario, null=True,blank=True,on_delete=models.CASCADE)

    """def __str__(self):
        texto = "{0} {1} {1} ({3}) ({4})"
        return texto.format(self.nomusu, self.conusu, str(self.estusu) , str(self.tipusu))
"""

class Distrito(models.Model):
    id=models.IntegerField(primary_key=True)
    nomdis=models.CharField(max_length=50)
    estdis=models.IntegerField()

class Carrera(models.Model):
    id=models.IntegerField(primary_key=True)
    nomcarrera=models.CharField(max_length=50)
    descarrera=models.CharField(max_length=50)
    estcarrera=models.IntegerField()
    
class Curso(models.Model):
    id=models.IntegerField(primary_key=True)
    nomcur=models.CharField(max_length=30)
    creditos=models.IntegerField()
    estcur=models.IntegerField()

class Estudiante(models.Model):
    id=models.IntegerField(primary_key=True)
    nomest=models.CharField(max_length=50)
    apeest=models.CharField(max_length=50)
    dniest=models.CharField(max_length=8)
    direccion=models.CharField(max_length=50)
    emailest=models.EmailField()
    estest=models.IntegerField()
    usuario=models.OneToOneField(to='Usuario', to_field='id', null=True, blank=True, on_delete=models.CASCADE)
    carrera=models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)
    distrito=models.ForeignKey(Distrito, null=True, blank=True, on_delete=models.CASCADE)
    #tipousu=models.ForeignKey(TipoUsuario, null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
            texto = "{0} {1} {2} {3} {4} {5} ({6}) ({7}) ({8}) ({9})"
            return texto.format(self.nomest, self.apeest, self.dniest , self.direccion, 
            self.emailest, str(self.estest), str(self.usuario), str(self.carrera), str(self.distrito) )

class Profesor(models.Model):
    id=models.IntegerField(primary_key=True)
    nompro=models.CharField(max_length=50)
    apepro=models.CharField(max_length=50)
    dnipro=models.CharField(max_length=50)
    direccionpro=models.CharField(max_length=50)
    distritopro=models.ForeignKey(Distrito, null=True,blank=True,on_delete=models.CASCADE)
    emailpro=models.EmailField()
    estpro=models.IntegerField()
    usuario=models.OneToOneField(to='Usuario', to_field='id', null=True, blank=True, on_delete=models.CASCADE)
    #tipousu=models.ForeignKey(TipoUsuario, null=True,blank=True,on_delete=models.CASCADE)

class Administrativo(models.Model):
    id=models.IntegerField(primary_key=True)
    nomadm=models.CharField(max_length=50)
    apeadm=models.CharField(max_length=50)
    dniadm=models.CharField(max_length=50)
    direccionadm=models.CharField(max_length=50)
    distritoadm=models.ForeignKey(Distrito, null=True,blank=True,on_delete=models.CASCADE)
    emailadm=models.EmailField()
    estadm =models.IntegerField()
    usuario=models.OneToOneField(to='Usuario', to_field='id', null=True, blank=True, on_delete=models.CASCADE)
    #tipousu=models.ForeignKey(TipoUsuario, null=True,blank=True,on_delete=models.CASCADE)


class Tarea1(models.Model):
    id=models.IntegerField(primary_key=True) 
    tittar = models.CharField(max_length=1000)
    destar = models.CharField(max_length=1000)
    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
    curso =models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    carrera=models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)

class Tarea2(models.Model):
    id=models.IntegerField(primary_key=True) 
    tittar = models.CharField(max_length=1000)
    destar = models.CharField(max_length=1000)
    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
    curso =models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    carrera=models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)

class Tarea3(models.Model):
    id=models.IntegerField(primary_key=True) 
    tittar = models.CharField(max_length=1000)
    destar = models.CharField(max_length=1000)
    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
    curso =models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    carrera=models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)

class Tarea4(models.Model):
    id=models.IntegerField(primary_key=True) 
    tittar = models.CharField(max_length=1000)
    destar = models.CharField(max_length=1000)
    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
    curso =models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    carrera=models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)

class Tarea5(models.Model):
    id=models.IntegerField(primary_key=True) 
    tittar = models.CharField(max_length=1000)
    destar = models.CharField(max_length=1000)
    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
    curso =models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    carrera=models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)


class Notas(models.Model):
    id=models.IntegerField(primary_key=True)
    profesor = models.ForeignKey(Profesor, null=True,blank=True,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=True,blank=True,on_delete=models.CASCADE)
    alumno = models.OneToOneField(to='Estudiante', to_field='id', null=True, blank=True, on_delete=models.CASCADE)

    sesion1_nt = models.IntegerField()
    sesion1_asis=models.CharField(max_length=50)
    tarea1_info = models.ForeignKey(Tarea1, null=True,blank=True,on_delete=models.CASCADE)
    soltarea1 = models.CharField(max_length=1000)
    notatarea1 = models.IntegerField()

    sesion2_nt = models.IntegerField()
    sesion2_asis=models.CharField(max_length=50)
    tarea2_info = models.ForeignKey(Tarea2, null=True,blank=True,on_delete=models.CASCADE)
    soltarea2 = models.CharField(max_length=1000)
    notatarea2 = models.IntegerField()

    sesion3_nt = models.IntegerField()
    sesion3_asis=models.CharField(max_length=50)
    tarea3_info = models.ForeignKey(Tarea3, null=True,blank=True,on_delete=models.CASCADE)
    soltarea3 = models.CharField(max_length=1000)
    notatarea3 = models.IntegerField()

    sesion4_nt = models.IntegerField()
    sesion4_asis=models.CharField(max_length=50)
    tarea4_info = models.ForeignKey(Tarea4, null=True,blank=True,on_delete=models.CASCADE)
    soltarea4 = models.CharField(max_length=1000)
    notatarea4 = models.IntegerField()

    sesion5_nt = models.IntegerField()
    sesion5_asis=models.CharField(max_length=50)
    tarea5_info = models.ForeignKey(Tarea5, null=True,blank=True,on_delete=models.CASCADE)
    soltarea5 = models.CharField(max_length=1000)
    notatarea5 = models.IntegerField()




"""

python manage.py runserver --- levantar servidor

python manage.py check Notas 

python manage.py makemigrations 

python manage.py sqlmigrate Notas 0010

python manage.py migrate 

"""







