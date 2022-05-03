from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Administrativo, Carrera, Estudiante, TipoUsuario, Usuario, Distrito, Curso, Profesor
from .models import Tarea1, Tarea2, Tarea3, Tarea4, Tarea5,Notas
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method =='POST':
        try:

            logeo = Usuario.objects.get(
                nomusu=request.POST['usuario'], conusu=request.POST['contrasena'], tipousu=request.POST['tipousu'])
            print("Usuario=", logeo)

            request.session['nomusu'] = logeo.nomusu
            tipo = request.POST['tipousu']
            #return render(request, 'bienvenido.html')

            if tipo == "1":
                return render(request, 'iniciopro.html')
            elif tipo == "2":
                return render(request, 'inicioest.html')
            elif tipo == "3":
                return render(request, 'bienvenido.html')
            else:
                return render(request, 'Error.html')

        except Usuario.DoesNotExist as e:
            messages.success(request, "Nombre de usuario o contraseña incorrecta")
    return render(request, 'login.html')
    


#------------------------------------------------------------------------------
#Menucrud
#------------------------------------------------------------------------------
def inicio(request):
    return render(request, 'bienvenido.html')

def inicioprof(request):
    messages.success(request, "Bienvenido al sistema")
    return render(request, 'iniciopro.html')

def inicioest(request):
    messages.success(request, "Bienvenido al sistema")
    return render(request, 'inicioest.html')

def menucrud(request):
    return render(request, 'menucrud.html')

def menuprocesos(request):
    return render(request, 'menuprocesos.html')

def menutar(request):
    return render(request, 'menutar.html')

def menuasistencia(request):
    return render(request, 'menuasistencia.html')

def menunotatarea(request):
    return render(request, 'menunotatarea.html') 

def menuasispro(request):
    return render(request, 'menuasispro.html') 

def menunotpro(request):
    return render(request, 'menunotpro.html') 

def menutarpro(request):
    return render(request, 'menutarpro.html') 
       
def menurealnot(request):
    return render(request, 'menurealnot.html') 
       
#------------------------------------------------------------------------------
#Tipo Usuario
#------------------------------------------------------------------------------

def indtip (request):
    tipo = TipoUsuario.objects.all()
    return render(request, 'CRUDS/TipoUsuario/gestiontipusu.html', {"tipo": tipo})

def registartipousuario(request, methods=['POST']):
    #id=request.POST["txtid"]
    nomtipusu=request.POST["txtnomtipusu"]
    esttipusu="1"

    tipousu = TipoUsuario.objects.create(nomtipusu=nomtipusu, esttipusu=esttipusu )
    messages.success(request, "¡Cursos registrados!")
    return redirect('/indtip/')

def ediciontipousuario(request,id):
    tipousu = TipoUsuario.objects.get(id=id)
    return render(request, "CRUDS/TipoUsuario/ediciontipusu.html", {"tipousu":tipousu})

def editartipousu(request):
    id=request.POST["txtid"]
    nomtipusu=request.POST["txtnomtipusu"]
    esttipusu=request.POST["txtesttipusu"]

    tipousu = TipoUsuario.objects.get(id=id)
    tipousu.nomtipusu = nomtipusu
    tipousu.esttipusu = esttipusu
    tipousu.save()
    return redirect('/indtip/')

def eliminartipousuario(request, id):
    tipousu = TipoUsuario.objects.get(id=id)
    tipousu.delete()
    return redirect('/indtip/')

#------------------------------------------------------------------------------
#Usuario
#------------------------------------------------------------------------------ 
def indusu (request):
    usuario = Usuario.objects.all()
    tipo = TipoUsuario.objects.all()
    return render(request, 'CRUDS/Usuario/gestionusuario.html', {"usuario": usuario, "tipo":tipo })

def registarusuario(request, methods=['POST']):
    #id=request.POST["txtid"]
    nomusu=request.POST["txtnomusu"]
    conusu=request.POST["txtconusu"]
    estusu="1"
    #tipousu=request.POST["txttipusu"]

    #tipo = TipoUsuario.objects.get(pk = request.POST['txttipusu'])
    usuario = Usuario()
    usuario = Usuario.objects.create(nomusu=nomusu,conusu=conusu,estusu=estusu)
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indusu/')

def edicionusuario(request,id):
    
    usu = Usuario.objects.get(id=id)
    tipo = TipoUsuario.objects.all()
    return render(request, "CRUDS/Usuario/edicionusuario.html", {"usu":usu,"tipo":tipo})

def editarusuario(request):
    id=request.POST["txtid"]
    nomusu=request.POST["txtnomusu"]
    conusu=request.POST["txtconusu"]
    estusu="1"
    

    usuario = Usuario.objects.get(id=id)
    usuario.nomusu = nomusu
    usuario.conusu = conusu
    usuario.estusu = estusu
    
    usuario.save()

    return redirect('/indusu/')


def eliminarusuario(request, id):
    usuario = Usuario()
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('/indusu/')

#------------------------------------------------------------------------------
#Distrito
#------------------------------------------------------------------------------
def inddis (request):
    distrito = Distrito.objects.all()
    return render(request, 'CRUDS/Distrito/gestiondistrito.html', {"distrito": distrito })

def registardistrito(request, methods=['POST']):
    #id=request.POST["txtid"]
    nomdis=request.POST["txtnomdis"]
    estdis="1"

    distrito = Distrito.objects.create(nomdis=nomdis,estdis=estdis)
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/inddis/')

def ediciondistrito(request,id):
    distrito = Distrito.objects.get(id=id)
    return render(request, "CRUDS/Distrito/ediciondistrito.html", {"distrito":distrito})

def editardis(request):
    id=request.POST["txtid"]
    nomdis=request.POST["txtnomdis"]
    estdis="1"


    distrito = Distrito.objects.get(id=id)
    distrito.nomdis = nomdis
    distrito.estdis = estdis
    distrito.save()
    return redirect('/inddis/')

def eliminardistrito(request, id):
    distrito = Distrito.objects.get(id=id)
    distrito.delete()
    return redirect('/inddis/')

#------------------------------------------------------------------------------
#Carrera
#------------------------------------------------------------------------------
def indcar (request):
    carrera = Carrera.objects.all()
    return render(request, 'CRUDS/Carrera/gestioncarrera.html', {"carrera": carrera })

def registarcarrera(request, methods=['POST']):
    #id=request.POST["txtid"]
    nomcar=request.POST["txtnomcar"]
    descar=request.POST["txtdescar"]
    estcar="1"

    carrera = Carrera.objects.create(nomcarrera=nomcar,descarrera=descar,estcarrera=estcar)
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indcar/')

def edicioncarrera(request,id):
    carrera = Carrera.objects.get(id=id)
    return render(request, "CRUDS/Carrera/edicioncarrera.html", {"carrera": carrera })

def editarcar(request):
    id=request.POST["txtid"]
    nomcar=request.POST["txtnomcar"]
    descar=request.POST["txtdescar"]
    estcar="1"


    carrera = Carrera.objects.get(id=id)
    carrera.nomcarrera = nomcar
    carrera.descarrera = descar
    carrera.estcarrera = estcar
    carrera.save()
    return redirect('/indcar/')

def eliminarcarrera(request, id):
    carrera = Carrera.objects.get(id=id)
    carrera.delete()
    return redirect('/indcar/')

#------------------------------------------------------------------------------
#CURSO
#------------------------------------------------------------------------------

def indcur (request):
    curso = Curso.objects.all()
    return render(request, 'CRUDS/Curso/gestioncurso.html', {"curso": curso })

def registarcurso(request, methods=['POST']):
    #id=request.POST["txtid"]
    nomcur=request.POST["txtnomcur"]
    creditos=request.POST["txtcreditos"]
    estcur="1"

    curso = Curso.objects.create(nomcur=nomcur,creditos=creditos,estcur=estcur)
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indcur/')

def edicioncurso(request,id):
    curso = Curso.objects.get(id=id)
    return render(request, "CRUDS/Curso/edicioncurso.html", {"curso": curso })

def editarcur(request):
    id=request.POST["txtid"]
    nomcur=request.POST["txtnomcur"]
    creditos=request.POST["txtcreditos"]
    estcur="1"


    curso = Curso.objects.get(id=id)
    curso.nomcur = nomcur
    curso.creditos = creditos
    curso.estcur = estcur
    curso.save()
    return redirect('/indcur/')

def eliminarcurso(request, id):
    indcur = Curso.objects.get(id=id)
    indcur.delete()
    return redirect('/indcur/')

#------------------------------------------------------------------------------
#Estudiante
#------------------------------------------------------------------------------

def indest (request):
    estudiante = Estudiante.objects.all()
    carrera = Carrera.objects.all()
    distrito = Distrito.objects.all()
    usuario = Usuario.objects.all()
    #tipo = TipoUsuario.objects.all()
    
    return render(request, 'CRUDS/Estudiante/gestionestudiante.html', {"estudiante": estudiante,
     "carrera": carrera, "distrito":distrito, "usuario":usuario})

def registarestudiante(request, methods=['POST']):
    #id=request.POST["txtid"]
    nomest=request.POST["txtnomest"]
    apeest=request.POST["txtapeest"]
    dniest=request.POST["txtdniest"]
    direccion=request.POST["txtdir"]
    emailest=request.POST["txtemailest"]
    estest="1"
    #tipousu=request.POST["txttipusu"]

    carrera = Carrera.objects.get(pk = request.POST['txtcar'])
    distrito = Distrito.objects.get(pk = request.POST['txtdis'])
    usuario = Usuario.objects.get(pk = request.POST['txtusu'])
    #tipo = TipoUsuario.objects.get(pk = 2)
    estudiante = Estudiante()
    estudiante = Estudiante.objects.create(nomest=nomest,apeest=apeest,dniest=dniest,
    direccion=direccion, emailest=emailest, estest=estest, carrera=carrera, 
    distrito=distrito, usuario=usuario)
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indest/')

def edicionestudiante(request,id):
    
    estudiante = Estudiante.objects.get(id=id)
    carrera = Carrera.objects.all()
    distrito = Distrito.objects.all()
    usuario = Usuario.objects.all()
    return render(request, "CRUDS/Estudiante/edicionestudiante.html", {"estudiante": estudiante, "usuario":usuario,
     "carrera": carrera, "distrito":distrito, "usuario":usuario })

def editarest(request):
    id=request.POST["txtid"]
    nomest=request.POST["txtnomest"]
    apeest=request.POST["txtapeest"]
    dniest=request.POST["txtdniest"]
    direccion=request.POST["txtdir"]
    emailest=request.POST["txtemailest"]
    estest="1"
    #tipousu=request.POST["txttipusu"]

    #tipo = TipoUsuario.objects.get(pk = 3)
    carrera = Carrera.objects.get(pk = request.POST['txtcar'])
    distrito = Distrito.objects.get(pk = request.POST['txtdis'])
    usuario = Usuario.objects.get(pk = request.POST['txtusu'])
    

    estudiante = Estudiante.objects.get(id=id)
    estudiante.nomest = nomest
    estudiante.apeest = apeest
    estudiante.dniest = dniest
    estudiante.direccion = direccion
    estudiante.emailest = emailest
    estudiante.estest = estest
    estudiante.carrera = carrera
    estudiante.distrito = distrito
    estudiante.usuario = usuario
    #estudiante.tipousu = tipo
    estudiante.save()

    return redirect('/indest/')

def eliminarestudiante(request, id):

    estudiante = Estudiante()
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('/indest/')

#------------------------------------------------------------------------------
#Profesor
#------------------------------------------------------------------------------

def indpro (request):
    profesor = Profesor.objects.all()
    distrito = Distrito.objects.all()
    usuario = Usuario.objects.all()
    
    return render(request, 'CRUDS/Profesor/gestionprofesor.html', {"profesor": profesor,
     "distrito":distrito, "usuario":usuario })

def registarprofesor(request, methods=['POST']):
    #id=request.POST["txtid"]
    nompro=request.POST["txtnompro"]
    apepro=request.POST["txtapepro"]
    dnipro=request.POST["txtdnipro"]
    direccionpro=request.POST["txtdirpro"]
    emailpro=request.POST["txtemailpro"]
    estpro=request.POST["txtestpro"]
    #tipousu="1"

    #tipo = TipoUsuario.objects.all()
    distrito = Distrito.objects.get(pk = request.POST['txtdis'])
    usuario = Usuario.objects.get(pk = request.POST['txtusu'])
    profesor = Profesor()
    profesor = Profesor.objects.create(nompro=nompro,apepro=apepro,dnipro=dnipro,
    direccionpro=direccionpro, emailpro=emailpro, estpro=estpro, distritopro=distrito, 
    usuario=usuario)
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indpro/')

def edicionprofesor(request,id):
    
    profesor = Profesor.objects.get(id=id)
 
    distrito = Distrito.objects.all()
    usuario = Usuario.objects.all()
    return render(request, "CRUDS/Profesor/edicionprofesor.html", {"profesor": profesor, "usuario":usuario,
     "distrito":distrito, "usuario":usuario })

def editarpro(request):
    id=request.POST["txtid"]
    nompro=request.POST["txtnompro"]
    apepro=request.POST["txtapepro"]
    dnipro=request.POST["txtdnipro"]
    direccionpro=request.POST["txtdirpro"]
    emailpro=request.POST["txtemailpro"]
    estpro=request.POST["txtestpro"]
    #tipousu="1"

    #tipo = TipoUsuario.objects.get(pk = 1)
    distrito = Distrito.objects.get(pk = request.POST['txtdis'])
    usuario = Usuario.objects.get(pk = request.POST['txtusu'])
    

    profesor = Profesor.objects.get(id=id)
    profesor.nompro = nompro
    profesor.apepro = apepro
    profesor.dnipro = dnipro
    profesor.direccionpro = direccionpro
    profesor.emailpro = emailpro
    profesor.estpro = estpro
    
    #profesor.tipousu = tipousu
    profesor.distrito = distrito
    profesor.usuario = usuario
    profesor.save()

    return redirect('/indpro/')

def eliminarprofesor(request, id):

    profesor = Profesor()
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    return redirect('/indpro/')

#------------------------------------------------------------------------------
#Administractivo
#------------------------------------------------------------------------------
def indadm (request):
    adm = Administrativo.objects.all()
    distrito = Distrito.objects.all()
    usuario = Usuario.objects.all()
    
    return render(request, 'CRUDS/Admin/gestionadmin.html', {"adm": adm,
     "distrito":distrito, "usuario":usuario })

def registaradmin(request, methods=['POST']):
    #id=request.POST["txtid"]
    nomadm=request.POST["txtnomadm"]
    apeadm=request.POST["txtapeadm"]
    dniadm=request.POST["txtdniadm"]
    direccionadm=request.POST["txtdiradm"]
    emailadm=request.POST["txtemailadm"]
    estadm=request.POST["txtestadm"]
    #tipousu=request.POST["txttipusu"]

    #tipo = TipoUsuario.objects.get(pk = 3)
    distritoadm = Distrito.objects.get(pk = request.POST['txtdisadm'])
    usuario = Usuario.objects.get(pk = request.POST['txtusu'])
    adm = Administrativo()
    adm = Administrativo.objects.create(nomadm=nomadm,apeadm=apeadm,dniadm=dniadm,
    direccionadm=direccionadm, emailadm=emailadm, estadm=estadm, distritoadm=distritoadm, 
    usuario=usuario)
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indpro/')

def edicionadmin(request,id):
    
    adm = Administrativo.objects.get(id=id)
 
    distrito = Distrito.objects.all()
    usuario = Usuario.objects.all()
    return render(request, "CRUDS/Admin/edicionadmin.html", {"adm": adm, "usuario":usuario,
     "distrito":distrito, "usuario":usuario })

def editaradm(request):
    id=request.POST["txtid"]
    nomadm=request.POST["txtnomadm"]
    apeadm=request.POST["txtapeadm"]
    dniadm=request.POST["txtdniadm"]
    direccionadm=request.POST["txtdiradm"]
    emailadm=request.POST["txtemailadm"]
    estadm=request.POST["txtestadm"]
    #tipousu=request.POST["txttipusu"]

    #tipo = TipoUsuario.objects.get(pk = 3)
    distrito = Distrito.objects.get(pk = request.POST['txtdis'])
    usuario = Usuario.objects.get(pk = request.POST['txtusu'])
    

    adm = Administrativo.objects.get(id=id)
    adm.nompro = nomadm
    adm.apepro = apeadm
    adm.dnipro = dniadm
    adm.direccionadm = direccionadm
    adm.emailadm = emailadm
    adm.estadm = estadm
    
    #adm.tipousu = tipo
    adm.distrito = distrito
    adm.usuario = usuario
    adm.save()

    return redirect('/indadm/')

def eliminaradmin(request, id):

    adm = Administrativo()
    adm = Administrativo.objects.get(id=id)
    adm.delete()
    return redirect('/indadm/')



#------------------------------------------------------------------------------
#Procesos
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Tarea 1
#------------------------------------------------------------------------------

def indtar1 (request):
    tarea = Tarea1.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Tarea1/gestiontarea1.html', {"tarea": tarea, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def registartarea1(request, methods=['POST']):
    #id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]
    
    car = Carrera.objects.get(pk = request.POST['txtcar'])
    cur = Curso.objects.get(pk = request.POST['txtcur'])
    pro = Profesor.objects.get(pk = request.POST['txtpro'])

    tarea = Tarea1()
    tarea = Tarea1.objects.create(tittar=tittar,destar=destar,carrera=car,
    curso=cur, profesor=pro)
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indtar1/')

def ediciontarea1(request,id):
    tarea = Tarea1.objects.get(id=id)
 
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, "PROCESOS/Tarea1/ediciontarea1.html", {"tarea": tarea, "carrera":carrera,
     "curso":curso, "profesor":profesor})

def editart1(request):
    id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]

    profesor = Profesor.objects.get(pk = request.POST['txtpro'])
    curso = Curso.objects.get(pk = request.POST['txtcur'])
    carrera = Carrera.objects.get(pk = request.POST['txtcar'])
    

    tarea = Tarea1.objects.get(id=id)
    tarea.tittar = tittar
    tarea.destar = destar
    tarea.profesor = profesor
    tarea.curso = curso
    tarea.carrera = carrera
    tarea.save()

    return redirect('/indtar1/')


def eliminartarea1(request, id):

    tarea = Tarea1()
    tarea = Tarea1.objects.get(id=id)
    tarea.delete()
    return redirect('/indtar1/')


#------------------------------------------------------------------------------
#Tarea 2
#------------------------------------------------------------------------------

def indtar2 (request):
    tarea = Tarea2.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Tarea2/gestiontarea2.html', {"tarea": tarea, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def registartarea2(request, methods=['POST']):
    #id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]
    
    car = Carrera.objects.get(pk = request.POST['txtcar'])
    cur = Curso.objects.get(pk = request.POST['txtcur'])
    pro = Profesor.objects.get(pk = request.POST['txtpro'])

    tarea = Tarea2()
    tarea = Tarea2.objects.create(tittar=tittar,destar=destar,carrera=car,
    curso=cur, profesor=pro)
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indtar2/')

def ediciontarea2(request,id):
    tarea = Tarea2.objects.get(id=id)
 
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, "PROCESOS/Tarea2/ediciontarea2.html", {"tarea": tarea, "carrera":carrera,
     "curso":curso, "profesor":profesor})

def editart2(request):
    id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]

    profesor = Profesor.objects.get(pk = request.POST['txtpro'])
    curso = Curso.objects.get(pk = request.POST['txtcur'])
    carrera = Carrera.objects.get(pk = request.POST['txtcar'])
    

    tarea = Tarea2.objects.get(id=id)
    tarea.tittar = tittar
    tarea.destar = destar
    tarea.profesor = profesor
    tarea.curso = curso
    tarea.carrera = carrera
    tarea.save()

    return redirect('/indtar2/')


def eliminartarea2(request, id):

    tarea = Tarea2()
    tarea = Tarea2.objects.get(id=id)
    tarea.delete()
    return redirect('/indtar2/')


#------------------------------------------------------------------------------
#Tarea 3
#------------------------------------------------------------------------------

def indtar3 (request):
    tarea = Tarea3.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Tarea3/gestiontarea3.html', {"tarea": tarea, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def registartarea3(request, methods=['POST']):
    #id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]
    
    car = Carrera.objects.get(pk = request.POST['txtcar'])
    cur = Curso.objects.get(pk = request.POST['txtcur'])
    pro = Profesor.objects.get(pk = request.POST['txtpro'])

    tarea = Tarea3()
    tarea = Tarea3.objects.create(tittar=tittar,destar=destar,carrera=car,
    curso=cur, profesor=pro)
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indtar3/')

def ediciontarea3(request,id):
    tarea = Tarea3.objects.get(id=id)
 
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, "PROCESOS/Tarea3/ediciontarea3.html", {"tarea": tarea, "carrera":carrera,
     "curso":curso, "profesor":profesor})

def editart3(request):
    id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]

    profesor = Profesor.objects.get(pk = request.POST['txtpro'])
    curso = Curso.objects.get(pk = request.POST['txtcur'])
    carrera = Carrera.objects.get(pk = request.POST['txtcar'])
    

    tarea = Tarea3.objects.get(id=id)
    tarea.tittar = tittar
    tarea.destar = destar
    tarea.profesor = profesor
    tarea.curso = curso
    tarea.carrera = carrera
    tarea.save()

    return redirect('/indtar3/')


def eliminartarea3(request, id):

    tarea = Tarea3()
    tarea = Tarea3.objects.get(id=id)
    tarea.delete()
    return redirect('/indtar3/')


#------------------------------------------------------------------------------
#Tarea 4
#------------------------------------------------------------------------------

def indtar4 (request):
    tarea = Tarea4.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Tarea4/gestiontarea4.html', {"tarea": tarea, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def registartarea4(request, methods=['POST']):
    #id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]
    
    car = Carrera.objects.get(pk = request.POST['txtcar'])
    cur = Curso.objects.get(pk = request.POST['txtcur'])
    pro = Profesor.objects.get(pk = request.POST['txtpro'])

    tarea = Tarea4()
    tarea = Tarea4.objects.create(tittar=tittar,destar=destar,carrera=car,
    curso=cur, profesor=pro)
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indtar4/')

def ediciontarea4(request,id):
    tarea = Tarea4.objects.get(id=id)
 
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, "PROCESOS/Tarea4/ediciontarea4.html", {"tarea": tarea, "carrera":carrera,
     "curso":curso, "profesor":profesor})

def editart4(request):
    id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]

    profesor = Profesor.objects.get(pk = request.POST['txtpro'])
    curso = Curso.objects.get(pk = request.POST['txtcur'])
    carrera = Carrera.objects.get(pk = request.POST['txtcar'])
    

    tarea = Tarea4.objects.get(id=id)
    tarea.tittar = tittar
    tarea.destar = destar
    tarea.profesor = profesor
    tarea.curso = curso
    tarea.carrera = carrera
    tarea.save()

    return redirect('/indtar4/')


def eliminartarea4(request, id):

    tarea = Tarea4()
    tarea = Tarea4.objects.get(id=id)
    tarea.delete()
    return redirect('/indtar4/')


#------------------------------------------------------------------------------
#Tarea 5
#------------------------------------------------------------------------------

def indtar5 (request):
    tarea = Tarea5.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Tarea5/gestiontarea5.html', {"tarea": tarea, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def registartarea5(request, methods=['POST']):
    #id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]
    
    car = Carrera.objects.get(pk = request.POST['txtcar'])
    cur = Curso.objects.get(pk = request.POST['txtcur'])
    pro = Profesor.objects.get(pk = request.POST['txtpro'])

    tarea = Tarea5()
    tarea = Tarea5.objects.create(tittar=tittar,destar=destar,carrera=car,
    curso=cur, profesor=pro)
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indtar5/')

def ediciontarea5(request,id):
    tarea = Tarea5.objects.get(id=id)
 
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, "PROCESOS/Tarea5/ediciontarea5.html", {"tarea": tarea, "carrera":carrera,
     "curso":curso, "profesor":profesor})

def editart5(request):
    id=request.POST["txtid"]
    tittar=request.POST["txttittar"]
    destar=request.POST["txtdestar"]

    profesor = Profesor.objects.get(pk = request.POST['txtpro'])
    curso = Curso.objects.get(pk = request.POST['txtcur'])
    carrera = Carrera.objects.get(pk = request.POST['txtcar'])
    

    tarea = Tarea5.objects.get(id=id)
    tarea.tittar = tittar
    tarea.destar = destar
    tarea.profesor = profesor
    tarea.curso = curso
    tarea.carrera = carrera
    tarea.save()

    return redirect('/indtar5/')


def eliminartarea5(request, id):

    tarea = Tarea5()
    tarea = Tarea5.objects.get(id=id)
    tarea.delete()
    return redirect('/indtar5/')

#------------------------------------------------------------------------------
#Notas General
#------------------------------------------------------------------------------


def indnot (request):
    notas = Notas.objects.all()
    profesor = Profesor.objects.all()
    curso = Curso.objects.all()
    alumno = Estudiante.objects.all()
    tarea1 = Tarea1.objects.all()
    tarea2 = Tarea2.objects.all()
    tarea3 = Tarea3.objects.all()
    tarea4 = Tarea4.objects.all()
    tarea5 = Tarea5.objects.all()
    #tarea = Tarea1.objects.all()
    
    return render(request, 'PROCESOS/gestionnotas.html', {"notas":notas,
     "profesor":profesor, "curso":curso, "alumno": alumno, "tarea1":tarea1,
      "tarea2":tarea2, "tarea3":tarea3, "tarea4":tarea4,"tarea5":tarea5
     
     })



def registarnotas(request, methods=['POST']):
   
    profesor = Profesor.objects.get(pk = request.POST['txtpro'])
    curso = Curso.objects.get(pk = request.POST['txtcur'])
    estudiante = Estudiante.objects.get(pk = request.POST['txtest'])

    ns1=request.POST["txtns1"]
    asis1=request.POST["txtasis1"]
    t1=Tarea1.objects.get(pk = request.POST['txtt1'])
    solt1=request.POST["txtsolt1"]
    nt1=request.POST["txtnt1"]
    
    ns2=request.POST["txtns2"]
    asis2=request.POST["txtasis2"]
    t2=Tarea2.objects.get(pk = request.POST['txtt2'])
    solt2=request.POST["txtsolt2"]
    nt2=request.POST["txtnt2"]

    ns3=request.POST["txtns3"]
    asis3=request.POST["txtasis3"]
    t3=Tarea3.objects.get(pk = request.POST['txtt3'])
    solt3=request.POST["txtsolt3"]
    nt3=request.POST["txtnt3"]
    
    ns4=request.POST["txtns4"]
    asis4=request.POST["txtasis4"]
    t4=Tarea4.objects.get(pk = request.POST['txtt4'])
    solt4=request.POST["txtsolt4"]
    nt4=request.POST["txtnt4"]

    ns5=request.POST["txtns5"]
    asis5=request.POST["txtasis5"]
    t5=Tarea5.objects.get(pk = request.POST['txtt5'])
    solt5=request.POST["txtsolt5"]
    nt5=request.POST["txtnt5"]

    notas = Notas()
    notas = Notas.objects.create(profesor=profesor,curso=curso,alumno=estudiante,
                                sesion1_nt=ns1, sesion1_asis=asis1, tarea1_info=t1, soltarea1=solt1, notatarea1=nt1,
                                sesion2_nt=ns2, sesion2_asis=asis2, tarea2_info=t2, soltarea2=solt2, notatarea2=nt2,
                                sesion3_nt=ns3, sesion3_asis=asis3, tarea3_info=t3, soltarea3=solt3, notatarea3=nt3,
                                sesion4_nt=ns4, sesion4_asis=asis4, tarea4_info=t4, soltarea4=solt4, notatarea4=nt4,
                                sesion5_nt=ns5, sesion5_asis=asis5, tarea5_info=t5, soltarea5=solt5, notatarea5=nt5
                                )
    
    #messages.success(request, '¡Cursos registrados!')
    return redirect('/indnot/')

def edicionnotas(request,id):

 
    notas = Notas.objects.get(id=id)
    profesor = Profesor.objects.all()
    curso = Curso.objects.all()
    alumno = Estudiante.objects.all()
    tarea1 = Tarea1.objects.all()
    tarea2 = Tarea2.objects.all()
    tarea3 = Tarea3.objects.all()
    tarea4 = Tarea4.objects.all()
    tarea5 = Tarea5.objects.all()
    return render(request, "PROCESOS/edicionnotas.html", {"notas":notas,
     "profesor":profesor, "curso":curso, "alumno": alumno, "tarea1":tarea1,
      "tarea2":tarea2, "tarea3":tarea3, "tarea4":tarea4,"tarea5":tarea5 })


def editarnot(request):
    id=request.POST["txtid"]

    profesor = Profesor.objects.get(pk = request.POST['txtpro'])
    curso = Curso.objects.get(pk = request.POST['txtcur'])
    estudiante = Estudiante.objects.get(pk = request.POST['txtest'])

    ns1=request.POST["txtns1"]
    asis1=request.POST["txtasis1"]
    t1=Tarea1.objects.get(pk = request.POST['txtt1'])
    solt1=request.POST["txtsolt1"]
    nt1=request.POST["txtnt1"]
    
    ns2=request.POST["txtns2"]
    asis2=request.POST["txtasis2"]
    t2=Tarea2.objects.get(pk = request.POST['txtt2'])
    solt2=request.POST["txtsolt2"]
    nt2=request.POST["txtnt2"]

    ns3=request.POST["txtns3"]
    asis3=request.POST["txtasis3"]
    t3=Tarea3.objects.get(pk = request.POST['txtt3'])
    solt3=request.POST["txtsolt3"]
    nt3=request.POST["txtnt3"]
    
    ns4=request.POST["txtns4"]
    asis4=request.POST["txtasis4"]
    t4=Tarea4.objects.get(pk = request.POST['txtt4'])
    solt4=request.POST["txtsolt4"]
    nt4=request.POST["txtnt4"]

    ns5=request.POST["txtns5"]
    asis5=request.POST["txtasis5"]
    t5=Tarea5.objects.get(pk = request.POST['txtt5'])
    solt5=request.POST["txtsolt5"]
    nt5=request.POST["txtnt5"]

    notas = Notas.objects.get(id=id)
    notas.profesor = profesor
    notas.curso = curso
    notas.estudiante = estudiante

    notas.sesion1_nt = ns1
    notas.sesion1_asis = asis1
    notas.tarea1_info = t1
    notas.soltarea1 = solt1
    notas.notatarea1 = nt1

    notas.sesion2_nt = ns2
    notas.sesion2_asis = asis2
    notas.tarea2_info = t2
    notas.soltarea2 = solt2
    notas.notatarea2 = nt2
  
    notas.sesion3_nt = ns3
    notas.sesion3_asis = asis3
    notas.tarea3_info = t3
    notas.soltarea3 = solt3
    notas.notatarea3 = nt3

    notas.sesion4_nt = ns4
    notas.sesion4_asis = asis4
    notas.tarea4_info = t4
    notas.soltarea4 = solt4
    notas.notatarea4 = nt4

    notas.sesion5_nt = ns5
    notas.sesion5_asis = asis5
    notas.tarea5_info = t5
    notas.soltarea5 = solt5
    notas.notatarea5 = nt5

    notas.save()

    return redirect('/indnot/')


def eliminarnotas(request, id):

    nota = Notas()
    nota = Notas.objects.get(id=id)
    nota.delete()
    return redirect('/indnot/')


#------------------------------------------------------------------------------
#Asistencia
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#Asistencia Sesion 1
#------------------------------------------------------------------------------

def indasis1 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Asistencia/gestionasistencias1.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def asistios1(request,id):
    notas = Notas.objects.all()
    a="Asistio"
    notas = Notas.objects.get(id=id)
    notas.sesion1_asis = a
    notas.save()

    return redirect('/indasis1/')

def faltos1(request,id):
    notas = Notas.objects.all()
    a="Falto"
    notas = Notas.objects.get(id=id)
    notas.sesion1_asis = a
    notas.save()

    return redirect('/indasis1/')

def justificados1(request,id):
    notas = Notas.objects.all()
    a="Justificado"
    notas = Notas.objects.get(id=id)
    notas.sesion1_asis = a
    notas.save()

    return redirect('/indasis1/')

#------------------------------------------------------------------------------
#Asistencia Sesion 2
#------------------------------------------------------------------------------

def indasis2 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Asistencia/gestionasistencias2.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def asistios2(request,id):
    notas = Notas.objects.all()
    a="Asistio"
    notas = Notas.objects.get(id=id)
    notas.sesion2_asis = a
    notas.save()

    return redirect('/indasis2/')

def faltos2(request,id):
    notas = Notas.objects.all()
    a="Falto"
    notas = Notas.objects.get(id=id)
    notas.sesion2_asis = a
    notas.save()

    return redirect('/indasis2/')

def justificados2(request,id):
    notas = Notas.objects.all()
    a="Justificado"
    notas = Notas.objects.get(id=id)
    notas.sesion2_asis = a
    notas.save()

    return redirect('/indasis2/')

#------------------------------------------------------------------------------
#Asistencia Sesion 3
#------------------------------------------------------------------------------

def indasis3 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Asistencia/gestionasistencias3.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def asistios3(request,id):
    notas = Notas.objects.all()
    a="Asistio"
    notas = Notas.objects.get(id=id)
    notas.sesion3_asis = a
    notas.save()

    return redirect('/indasis3/')

def faltos3(request,id):
    notas = Notas.objects.all()
    a="Falto"
    notas = Notas.objects.get(id=id)
    notas.sesion3_asis = a
    notas.save()

    return redirect('/indasis3/')

def justificados3(request,id):
    notas = Notas.objects.all()
    a="Justificado"
    notas = Notas.objects.get(id=id)
    notas.sesion3_asis = a
    notas.save()

    return redirect('/indasis3/')

#------------------------------------------------------------------------------
#Asistencia Sesion 4
#------------------------------------------------------------------------------

def indasis4 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Asistencia/gestionasistencias4.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def asistios4(request,id):
    notas = Notas.objects.all()
    a="Asistio"
    notas = Notas.objects.get(id=id)
    notas.sesion4_asis = a
    notas.save()

    return redirect('/indasis4/')

def faltos4(request,id):
    notas = Notas.objects.all()
    a="Falto"
    notas = Notas.objects.get(id=id)
    notas.sesion4_asis = a
    notas.save()

    return redirect('/indasis4/')

def justificados4(request,id):
    notas = Notas.objects.all()
    a="Justificado"
    notas = Notas.objects.get(id=id)
    notas.sesion4_asis = a
    notas.save()

    return redirect('/indasis4/')


#------------------------------------------------------------------------------
#Asistencia Sesion 5
#------------------------------------------------------------------------------

def indasis5 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Asistencia/gestionasistencias5.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})



def asistios5(request,id):
    notas = Notas.objects.all()
    a="Asistio"
    notas = Notas.objects.get(id=id)
    notas.sesion5_asis = a
    notas.save()

    return redirect('/indasis5/')

def faltos5(request,id):
    notas = Notas.objects.all()
    a="Falto"
    notas = Notas.objects.get(id=id)
    notas.sesion5_asis = a
    notas.save()

    return redirect('/indasis5/')

def justificados5(request,id):
    notas = Notas.objects.all()
    a="Justificado"
    notas = Notas.objects.get(id=id)
    notas.sesion5_asis = a
    notas.save()

    return redirect('/indasis5/')



#------------------------------------------------------------------------------
#Nota Sesiones
#------------------------------------------------------------------------------

def indnts (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasSesiones/gestionregnts.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def editarns1 (request,id):
    notas = Notas.objects.get(id=id)
    return render(request, "PROCESOS/RegNotasSesiones/ednt1.html", {"notas": notas })

def edicionns1(request):
    id=request.POST["txtid"]
    nt1 =request.POST["txtnt1"]
    nt2 =request.POST["txtnt2"]
    nt3 =request.POST["txtnt3"]
    nt4 =request.POST["txtnt4"]
    nt5 =request.POST["txtnt5"]

    notas = Notas.objects.get(id=id)
    notas.sesion1_nt = nt1
    notas.sesion2_nt = nt2
    notas.sesion3_nt = nt3
    notas.sesion4_nt = nt4
    notas.sesion5_nt = nt5
    notas.save()
    messages.success(request, "Las notas fueron actualizadas")
    return redirect('/indnts/')

#------------------------------------------------------------------------------
#Nota Tareas
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Nota Tareas 1
#------------------------------------------------------------------------------

def indntt1 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/gestionregntt1.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def editarntt1 (request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/edntt1.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionnt1(request):
    id=request.POST["txtid"]
    nt1 =request.POST["txtntt"]


    notas = Notas.objects.get(id=id)
    notas.notatarea1 = nt1

    notas.save()
    messages.success(request, "Nota de la tarea 1 actualizada correctamente")
    return redirect('/indntt1/')

#------------------------------------------------------------------------------
#Nota Tareas 2
#------------------------------------------------------------------------------

def indntt2 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/gestionregntt2.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def editarntt2 (request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/edntt2.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionnt2(request):
    id=request.POST["txtid"]
    nt1 =request.POST["txtntt"]


    notas = Notas.objects.get(id=id)
    notas.notatarea2 = nt1

    notas.save()
    messages.success(request, "Nota de la tarea 2 actualizada correctamente")
    return redirect('/indntt2/')

#------------------------------------------------------------------------------
#Nota Tareas 3
#------------------------------------------------------------------------------

def indntt3 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/gestionregntt3.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def editarntt3 (request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/edntt3.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionnt3(request):
    id=request.POST["txtid"]
    nt1 =request.POST["txtntt"]


    notas = Notas.objects.get(id=id)
    notas.notatarea3 = nt1

    notas.save()
    messages.success(request, "Nota de la tarea 3 actualizada correctamente")
    return redirect('/indntt3/')

#------------------------------------------------------------------------------
#Nota Tareas 4
#------------------------------------------------------------------------------

def indntt4 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/gestionregntt4.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def editarntt4 (request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/edntt4.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionnt4(request):
    id=request.POST["txtid"]
    nt1 =request.POST["txtntt"]


    notas = Notas.objects.get(id=id)
    notas.notatarea4 = nt1

    notas.save()
    messages.success(request, "Nota de la tarea 4 actualizada correctamente")
    return redirect('/indntt4/')


#------------------------------------------------------------------------------
#Nota Tareas 5
#------------------------------------------------------------------------------

def indntt5 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/gestionregntt5.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def editarntt5 (request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RegNotasTareas/edntt5.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionnt5(request):
    id=request.POST["txtid"]
    nt1 =request.POST["txtntt"]


    notas = Notas.objects.get(id=id)
    notas.notatarea5 = nt1

    notas.save()
    messages.success(request, "Nota de la tarea 5 actualizada correctamente")
    return redirect('/indntt5/')

#------------------------------------------------------------------------------
#Listados
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Listado de asistencia profesor
#------------------------------------------------------------------------------
def indlisasisprof (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Listados/listasiprof.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

#------------------------------------------------------------------------------
#Listado de asistencia estado
#------------------------------------------------------------------------------
def listasiest (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Listados/listasiest.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

#------------------------------------------------------------------------------
#Listado de notas de tareas
#------------------------------------------------------------------------------
def indlisanotasprof (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Listados/lisanotasprof.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

#------------------------------------------------------------------------------
#Listado general de notas    
#------------------------------------------------------------------------------
def indlisgennot (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Listados/lisgennot.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

#------------------------------------------------------------------------------
#Listado de notas de sesiones     
#------------------------------------------------------------------------------
def indlisnotses (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Listados/lisnotses.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

#------------------------------------------------------------------------------
#Listado de notas de estudiantes     
#------------------------------------------------------------------------------
def listnotalum (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/Listados/listnotalum.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

#------------------------------------------------------------------------------
#Realizar Tareas 
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Realizar Tarea 1
#------------------------------------------------------------------------------

def realtarea1 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/realtarea1.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edirealt1(request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/edirealt1.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionrealt1(request):
    id=request.POST["txtid"]
    t1 =request.POST["txtsolt"]
    notas = Notas.objects.get(id=id)
    notas.soltarea1 = t1

    notas.save()
    messages.success(request, "Tarea 1 realizada")
    return redirect('/realtarea1/')

#------------------------------------------------------------------------------
#Realizar Tarea 2
#------------------------------------------------------------------------------

def realtarea2 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/realtarea2.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edirealt2(request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/edirealt2.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionrealt2(request):
    id=request.POST["txtid"]
    t1 =request.POST["txtsolt"]
    notas = Notas.objects.get(id=id)
    notas.soltarea2 = t1

    notas.save()
    messages.success(request, "Tarea 2 realizada")
    return redirect('/realtarea2/')

#------------------------------------------------------------------------------
#Realizar Tarea 3
#------------------------------------------------------------------------------

def realtarea3 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/realtarea3.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edirealt3(request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/edirealt3.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionrealt3(request):
    id=request.POST["txtid"]
    t1 =request.POST["txtsolt"]
    notas = Notas.objects.get(id=id)
    notas.soltarea3 = t1

    notas.save()
    messages.success(request, "Tarea 3 realizada")
    return redirect('/realtarea3/')


#------------------------------------------------------------------------------
#Realizar Tarea 4
#------------------------------------------------------------------------------

def realtarea4 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/realtarea4.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edirealt4(request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/edirealt4.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionrealt4(request):
    id=request.POST["txtid"]
    t1 =request.POST["txtsolt"]
    notas = Notas.objects.get(id=id)
    notas.soltarea4 = t1

    notas.save()
    messages.success(request, "Tarea 4 realizada")
    return redirect('/realtarea4/')

#------------------------------------------------------------------------------
#Realizar Tarea 5
#------------------------------------------------------------------------------

def realtarea5 (request):
    notas = Notas.objects.all()
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/realtarea5.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edirealt5(request,id):
    notas = Notas.objects.get(id=id)
    carrera = Carrera.objects.all()
    curso = Curso.objects.all()
    profesor = Profesor.objects.all()
    return render(request, 'PROCESOS/RealTareas/edirealt5.html', {"notas": notas, "carrera":carrera,
    "curso":curso, "profesor":profesor})

def edicionrealt5(request):
    id=request.POST["txtid"]
    t1 =request.POST["txtsolt"]
    notas = Notas.objects.get(id=id)
    notas.soltarea5 = t1

    notas.save()
    messages.success(request, "Tarea 5 realizada")
    return redirect('/realtarea5/')