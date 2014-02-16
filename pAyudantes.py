import urllib, urllib2, cookielib

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


	return sql
