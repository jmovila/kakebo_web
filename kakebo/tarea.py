from kakebo import app
import sqlite3
import json

@app.route('/homework/<notaMedia>')
@app.route('/homework')
def homework(notaMedia= None):
    #msj ='**para consultar nota media de alumnos, añada /media despues de homework en el navegador'
    if not notaMedia:
        tarea2= False
    else:
        tarea2 = True
    campos= ('Nombre', 'Apellidos', 'Matematicas', 'Lengua','Naturales', 'Sociales')

    notas =[('Pedro', 'Jimenez', 10, 9, 8, 9),
        ('Juana', 'Rodriguez', 9, 4, 9, 8),
        ('Andres', 'Stevensson', 6, 7, 9, 5)
        ]

    boletines =[]
    for nota in notas:
        dic={}
        for index, valor in enumerate(nota):
            dic[campos[index]]=valor
        boletines.append(dic)
    if not tarea2: 
        return json.dumps(boletines)
        
    else:
        for med in boletines:
            med['media']=(med['Matematicas']+ med['Lengua']+med['Naturales']+med['Sociales'])/4
            med['grafico'] = '*'*int(med['media'] / 0.5)
        
        return json.dumps(boletines)

@app.route('/')
def index():

    conexion = sqlite3.connect('movimientos.db')
    cur = conexion.cursor()

    cur.execute('SELECT * FROM movimientos;')

    claves = cur.description


    filas = cur.fetchall()
    lista=[]
    for fila in filas:
        d = {}
        for indice, dato in enumerate(fila):
            d[claves[indice][0]]=dato
        lista.append(d)
        '''
        for item in lista:
            if item['esGasto'] == 0:
                item['saldo'] = item['cantidad'] + item[0+1]['cantidad']
        '''
    return json.dumps(lista)

        
        
    
    conexion.close() 

    return 'consulta realizada'