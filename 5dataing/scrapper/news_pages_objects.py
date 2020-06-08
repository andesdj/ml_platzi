from common import config
import requests
import bs4

# El codigo auxiliar queda en Newspage
class Newspage:
	def __init__(self, news_site_uid, url):
		self._config = config()['news_sites'][news_site_uid]
		self._queries = self._config['queries']
		self._html = None
  		
		self._visit(url)

 #Metodo general para acceder a sitios web
	def _visit(self, url):
		response = requests.get(url)
		#Codificar en UTF8
		#Metodo que avienta un error si no se concluye la peticion, de lo contrario captura HTML con BS4
		response.raise_for_status()
		self._html = bs4.BeautifulSoup(response.text, 'html.parser')
	
	#Obtener información del documento que se va a parsear, se emplea pasando como parametro el query de BS4
	def _select(self, query_string):
		return self._html.select(query_string)


# Homepage es una subclase de  Newspages Homepage Exiende newspage
# Con super se tiene acceso a los metodos de inicializacion de newspage en Homepge
# La diferencia de Homepage con las demas es la propiedad de  article_links 
class HomePage(Newspage):

	def __init__(self,news_site_uid,url):
		self._url = url
		super().__init__(news_site_uid, url)


	# Se definiran las primeras propiedades del sitio 
	@property
	def article_links(self):
		link_list=[]
		# se recorreran todos los links de la pagina con un For y si el link tiene attr Href es valido
		# Si es valido se agrega con append.
		for link in self._select(self._queries['homepage_article_links']):
			if  link and link.has_attr('href'):
				link_list.append(link)
		# Se regresa una lista con los enlaces
  		# Con  set se borrarán los enlaces repetidos se ejecuta con un set comprehension
		return set(link['href'] for link in link_list)

# ArticlePage extiende a Newspage tambien
# con super inicializa la superclase
class ArticlePage(Newspage):
    
	def __init__(self,news_site_uid,url):
		self._url = url
		super().__init__(news_site_uid, url)
		#Abstracciones para visitar cada una de las paginas y obtener los datos de cada una de ellas
		# a traves de los property

	@property
	def body(self):
		result = self._select(self._queries['article_body'])
		return result[0].text if len(result) else ''

	@property
	def title(self):
		result = self._select(self._queries['article_title'])
		return result[0].text if len(result) else ''

	@property
	def url(self):
		if self._url:
			return self._url
		else:
			return ''
		