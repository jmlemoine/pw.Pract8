from zeep import Client

cliente = Client('http://localhost:7777/ws/AcademicoWebService?wsdl')

listaEstudiantes = cliente.service.getAllEstudiante()
print '\n\nLista de Estudiantes: \n' + str(listaEstudiantes)

asignaturaConsultada = cliente.service.getAsignatura(1)
print '\n\nAsignatura Consultada: \n' + str(asignaturaConsultada)

profesorConsultado = cliente.service.getProfesor("031-0001-01")
print '\n\nProfesor Consultado: \n' + str(profesorConsultado)