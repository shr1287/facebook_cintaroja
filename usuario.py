class  Usuario:
	nombre = ""
	"""docstring for  user"""
	def __init__(self):
  		self.url = "https://graph.facebook.com/v2.8/me"
  		self.token = "EAACEdEose0cBAJ9ZBZCOi9QKOYSFiNc7r3RORKIdI30iADohJZA2ismjcCdMmI2zZCmiD2c307qXiOyxfTpXpZBgbkv0g2ii6ObKpUSL495U8iGzsWdbeAaFVC8tTden7RAE6NVTnqRgv7zrgX7cxMpxJensHXMVGiWIYdglCswZDZD"

  	def obtenInformacion(self):
  		parametros = {"acces_token": self.token}
  		resultado = request.get(self.url, params=parametros).json
  		print (resultado)
  		self.nombre = resultado["name"]
  		return resultado

  arreglar
  