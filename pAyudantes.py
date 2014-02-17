import urllib, urllib2, cookielib, os, time, sys
from os import listdir
from os.path import isfile, join


def datos(ru, clave):
	#Cookies
	cookie = cookielib.CookieJar()
	cookie_h = urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(cookie_h)
	urllib2.install_opener(opener)
	
	#Login
	link = "http://190.129.32.203/bestudiantes/login.php"
	data = urllib.urlencode({"user":ru, "pass":clave})
	page = urllib2.urlopen(link, data)

	#cadena
	sql = "insert into ayudantia values('', '"

	if len(page.read())<6:
		#IP - Ver que ip almacena y que numero de session es 
		page = urllib2.urlopen("http://190.129.32.203/bestudiantes/rtl.php")
		ip = page.read()
		ip = ip.split('\n')
		sql = sql + ip[80][120:len(ip[80])-15] +"', '"
		
		#Datos Personales
		page = urllib2.urlopen("http://190.129.32.203/bestudiantes/data/bauxiliar.php")
		datos = page.read()
		datos = datos.split('\n')
		sql = sql + datos[139][76:len(datos[139])-10] + "', '" + datos[143][76:len(datos[143])-10] + "', '" + datos[147][76:len(datos[147])-10] + "', '" + datos[151][76:len(datos[151])-6] + "', '" + datos[156][73:len(datos[156])-5] + "', '" + datos[165][73:len(datos[165])-5] + "', '" + datos[174][73:len(datos[174])-5] + "', '"
	
		#Lista de Materias
		page = urllib2.urlopen("http://190.129.32.203/bestudiantes/data/jcm_listar.php")
		mat = page.read()
		mat = mat.split('\n')

		if len(mat)==40:
			sql = sql + mat[14][12:len(mat[14])-6] + "', '" + mat[15][12:len(mat[15])-6] + "', '" + mat[16][12:len(mat[16])-6] + "', '" + mat[18][55:len(mat[18])-26] + "', '"
			sql = sql + mat[22][12:len(mat[22])-6] + "', '" + mat[23][12:len(mat[23])-6] + "', '" + mat[24][12:len(mat[24])-6] + "', '" + mat[26][55:len(mat[26])-26] + "', '"
			sql = sql + mat[30][12:len(mat[30])-6] + "', '" + mat[31][12:len(mat[31])-6] + "', '" + mat[32][12:len(mat[32])-6] + "', '" + mat[34][55:len(mat[34])-26] + "');"
		elif len(mat)==32:
			sql = sql + mat[14][12:len(mat[14])-6] + "', '" + mat[15][12:len(mat[15])-6] + "', '" + mat[16][12:len(mat[16])-6] + "', '" + mat[18][55:len(mat[18])-26] + "', '"
			sql = sql + mat[22][12:len(mat[22])-6] + "', '" + mat[23][12:len(mat[23])-6] + "', '" + mat[24][12:len(mat[24])-6] + "', '" + mat[26][55:len(mat[26])-26] + "', '"
			sql = sql +  "', '', '', '');"
		elif len(mat)==24:
			sql = sql + mat[14][12:len(mat[14])-6] + "', '" + mat[15][12:len(mat[15])-6] + "', '" + mat[16][12:len(mat[16])-6] + "', '" + mat[18][55:len(mat[18])-26] + "', '"
			sql = sql +  "', '', '', '', '"
			sql = sql +  "', '', '', '');"
		else:
			sql = sql +  "', '', '', '', '"
			sql = sql +  "', '', '', '', '"
			sql = sql +  "', '', '', '');"
	else:
		sql = "/* No da */"

	return sql


def carreraList(carrera):
	try:
		fil = open(carrera)
		for est in fil:
			est = est.split(' ')
			r = str(est[0])
			c = str(est[1].strip('\n'))
			try:
				print datos(r, c)
			except:
				print "/* Descanzando un rato en 3 minutos*/"
				time.sleep(120)
				print datos(r, c)
		fil.close()
	except IOError as er:
		print "Error : Lectura de archivo (%s)" % (er)



ruta = os.path.abspath("")

carreras = []
carreras = [f for f in listdir(ruta) if isfile(join(ruta,f)) and f.endswith(".lst") ]
print "Elige la carrera ;P\n==================="
print 

for nombres in (carreras):
	print "\t %s %s " % (nombres[0:3].upper(), nombres[3:len(nombres)-4].lower())

op = raw_input("Elige la opcion ")
op = (op.lower()).strip(' ')

resp = 0
for f in carreras:
	if f[0:3]==op:
		carreraList(f)
		resp = 1

if resp==1:
	print
	print "Espero te sirva la lista"
	print
else:
	print
	print "mmm aver elegi bien \m/"
	print

