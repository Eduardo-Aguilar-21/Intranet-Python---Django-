"""Intranet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlapatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpat terns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Notas.views import inicio,inicioprof,inicioest, menucrud, menuprocesos, menutar,menuasistencia, menunotatarea, menuasispro
from Notas.views import menunotpro, menutarpro, menurealnot
from Notas.views import indtip, login,registartipousuario, eliminartipousuario,ediciontipousuario,editartipousu
from Notas.views import indusu, registarusuario,edicionusuario,editarusuario, eliminarusuario
from Notas.views import inddis, registardistrito, ediciondistrito, editardis, eliminardistrito
from Notas.views import indcar, registarcarrera, edicioncarrera, editarcar, eliminarcarrera
from Notas.views import indcur, registarcurso, edicioncurso, editarcur, eliminarcurso
from Notas.views import indest, registarestudiante, edicionestudiante, editarest, eliminarestudiante
from Notas.views import indpro, registarprofesor, edicionprofesor, editarpro, eliminarprofesor
from Notas.views import indadm, registaradmin, edicionadmin, editaradm, eliminaradmin
from Notas.views import indtar1, registartarea1, ediciontarea1, editart1, eliminartarea1 
from Notas.views import indtar2, registartarea2, ediciontarea2, editart2, eliminartarea2
from Notas.views import indtar3, registartarea3, ediciontarea3, editart3, eliminartarea3 
from Notas.views import indtar4, registartarea4, ediciontarea4, editart4, eliminartarea4 
from Notas.views import indtar5, registartarea5, ediciontarea5, editart5, eliminartarea5 
from Notas.views import indnot, registarnotas, edicionnotas, editarnot, eliminarnotas
from Notas.views import indasis1, asistios1, faltos1, justificados1
from Notas.views import indasis2, asistios2, faltos2, justificados2
from Notas.views import indasis3, asistios3, faltos3, justificados3
from Notas.views import indasis4, asistios4, faltos4, justificados4
from Notas.views import indasis5, asistios5, faltos5, justificados5
from Notas.views import indnts, editarns1, edicionns1
from Notas.views import indntt1, editarntt1, edicionnt1
from Notas.views import indntt2, editarntt2, edicionnt2
from Notas.views import indntt3, editarntt3, edicionnt3
from Notas.views import indntt4, editarntt4, edicionnt4
from Notas.views import indntt5, editarntt5, edicionnt5
from Notas.views import indlisasisprof, indlisanotasprof, indlisgennot,indlisnotses,listasiest,listnotalum
from Notas.views import realtarea1, edirealt1, edicionrealt1
from Notas.views import realtarea2, edirealt2, edicionrealt2
from Notas.views import realtarea3, edirealt3, edicionrealt3
from Notas.views import realtarea4, edirealt4, edicionrealt4
from Notas.views import realtarea5, edirealt5, edicionrealt5

from Notas import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('index/', index),
    #path('' , index),
    path('login/', login, name='login'),
    path('inicio/',inicio),
    path('inicioprof/',inicioprof),
    path('inicioest/',inicioest),
    path('menucrud/',menucrud),
    path('menuprocesos/',menuprocesos),
    path('menutar/',menutar),
    path('menuasistencia/',menuasistencia),    
    path('menunotatarea/',menunotatarea),   
    path('menuasispro/',menuasispro), 
    path('menunotpro/',menunotpro), 
    path('menutarpro/',menutarpro), 
    path('menurealnot/',menurealnot), 
    
    #-------------------------------------------------
    #             CRUDS
    #-------------------------------------------------

    # Tipo usuario
    path('indtip/', indtip),
    path('registartipousuario/', registartipousuario, name='registartipousuario' ),
    path('ediciontipousuario/<int:id>', ediciontipousuario),
    path('editartipousu/', editartipousu),
    path('eliminartipousuario/<int:id>', eliminartipousuario),

    #Usuario
    path('indusu/', indusu),
    path('registarusuario/', registarusuario, name='registarusuario' ),
    path('edicionusuario/<int:id>', edicionusuario),
    path('editarusuario/', editarusuario),
    path('eliminarusuario/<int:id>', eliminarusuario),

    #Distrito
    path('inddis/', inddis),
    path('registardistrito/', registardistrito, name='registardistrito' ),
    path('ediciondistrito/<int:id>', ediciondistrito),
    path('editardis/', editardis),
    path('eliminardistrito/<int:id>', eliminardistrito),

    #Carrera
    path('indcar/', indcar),
    path('registarcarrera/', registarcarrera, name='registarcarrera' ),
    path('edicioncarrera/<int:id>', edicioncarrera),
    path('editarcar/', editarcar),
    path('eliminarcarrera/<int:id>', eliminarcarrera),

    #Curso
    path('indcur/', indcur),
    path('registarcurso/', registarcurso, name='registarcurso' ),
    path('edicioncurso/<int:id>', edicioncurso),
    path('editarcur/', editarcur),
    path('eliminarcurso/<int:id>', eliminarcurso),

    #Estudiante
    path('indest/', indest),
    path('registarestudiante/', registarestudiante, name='registarestudiante' ),
    path('edicionestudiante/<int:id>', edicionestudiante),
    path('editarest/', editarest),
    path('eliminarestudiante/<int:id>', eliminarestudiante),

    #Profesor
    path('indpro/', indpro),
    path('registarprofesor/', registarprofesor, name='registarprofesor' ),
    path('edicionprofesor/<int:id>', edicionprofesor),
    path('editarpro/', editarpro),
    path('eliminarprofesor/<int:id>', eliminarprofesor),


    #Administractivo
    path('indadm/', indadm),
    path('registaradmin/', registaradmin, name='registaradmin' ),
    path('edicionadmin/<int:id>', edicionadmin),
    path('editaradm/', editaradm),
    path('eliminaradmin/<int:id>', eliminaradmin),

    #Tarea1
    path('indtar1/', indtar1),
    path('registartarea1/', registartarea1),
    path('ediciontarea1/<int:id>', ediciontarea1),
    path('editart1/', editart1),
    path('eliminartarea1/<int:id>', eliminartarea1),
    
    #Tarea2
    path('indtar2/', indtar2),
    path('registartarea2/', registartarea2),
    path('ediciontarea2/<int:id>', ediciontarea2),
    path('editart2/', editart2),
    path('eliminartarea2/<int:id>', eliminartarea2),
    
    #Tarea3
    path('indtar3/', indtar3),
    path('registartarea3/', registartarea3),
    path('ediciontarea3/<int:id>', ediciontarea3),
    path('editart3/', editart3),
    path('eliminartarea3/<int:id>', eliminartarea3),

    #Tarea4
    path('indtar4/', indtar4),
    path('registartarea4/', registartarea4),
    path('ediciontarea4/<int:id>', ediciontarea4),
    path('editart4/', editart4),
    path('eliminartarea4/<int:id>', eliminartarea4),
    
    #Tarea5
    path('indtar5/', indtar5),
    path('registartarea5/', registartarea5),
    path('ediciontarea5/<int:id>', ediciontarea5),
    path('editart5/', editart5),
    path('eliminartarea5/<int:id>', eliminartarea5),
    

    #Notas
    path('indnot/', indnot),
    path('registarnotas/', registarnotas),
    path('edicionnotas/<int:id>', edicionnotas),
    path('editarnot/', editarnot),
    path('eliminarnotas/<int:id>', eliminarnotas),
 
    #Asistencia S1
    path('indasis1/', indasis1),
    path('asistios1/<int:id>', asistios1),
    path('faltos1/<int:id>', faltos1),
    path('justificados1/<int:id>', justificados1),

    #Asistencia S2
    path('indasis2/', indasis2),
    path('asistios2/<int:id>', asistios2),
    path('faltos2/<int:id>', faltos2),
    path('justificados2/<int:id>', justificados2),

    #Asistencia S3
    path('indasis3/', indasis3),
    path('asistios3/<int:id>', asistios3),
    path('faltos3/<int:id>', faltos3),
    path('justificados3/<int:id>', justificados3),

    #Asistencia S4
    path('indasis4/', indasis4),
    path('asistios4/<int:id>', asistios4),
    path('faltos4/<int:id>', faltos4),
    path('justificados4/<int:id>', justificados4),

    #Asistencia S5
    path('indasis5/', indasis5),
    path('asistios5/<int:id>', asistios5),
    path('faltos5/<int:id>', faltos5),
    path('justificados5/<int:id>', justificados5),

    #Registro de Notas de sesiones
    path('indnts/', indnts),
    path('editarns1/<int:id>', editarns1),
    path('edicionns1/', edicionns1),

    #Registro de Notas de tareas
    #Nota tarea 1
    path('indntt1/', indntt1),
    path('editarntt1/<int:id>', editarntt1),
    path('edicionnt1/', edicionnt1),

    #Nota tarea 2
    path('indntt2/', indntt2),
    path('editarntt2/<int:id>', editarntt2),
    path('edicionnt2/', edicionnt2),

    #Nota tarea 3
    path('indntt3/', indntt3),
    path('editarntt3/<int:id>', editarntt3),
    path('edicionnt3/', edicionnt3),

    #Nota tarea 4
    path('indntt4/', indntt4),
    path('editarntt4/<int:id>', editarntt4),
    path('edicionnt4/', edicionnt4),

    #Nota tarea 5
    path('indntt5/', indntt5),
    path('editarntt5/<int:id>', editarntt5),
    path('edicionnt5/', edicionnt5),

    #Listado asistencia profesor
    path('indlisasisprof/', indlisasisprof),
    path('indlisanotasprof/', indlisanotasprof),
    path('indlisgennot/', indlisgennot),
    path('indlisnotses/', indlisnotses),
    path('listnotalum/', listnotalum),
    

    #Listado asistencia estudiantes
    path('listasiest/', listasiest),

    #Realizacion de tareas
    #Realizar tarea 1
    path('realtarea1/', realtarea1),
    path('edirealt1/<int:id>', edirealt1),
    path('edicionrealt1/', edicionrealt1),

    #Realizar tarea 2
    path('realtarea2/', realtarea2),
    path('edirealt2/<int:id>', edirealt2),
    path('edicionrealt2/', edicionrealt2),

    #Realizar tarea 3
    path('realtarea3/', realtarea3),
    path('edirealt3/<int:id>', edirealt3),
    path('edicionrealt3/', edicionrealt3),

    #Realizar tarea 4
    path('realtarea4/', realtarea4),
    path('edirealt4/<int:id>', edirealt4),
    path('edicionrealt4/', edicionrealt4),

    #Realizar tarea 5
    path('realtarea5/', realtarea5),
    path('edirealt5/<int:id>', edirealt5),
    path('edicionrealt5/', edicionrealt5),

]
