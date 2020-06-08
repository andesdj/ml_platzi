import news_pages_objects as news
import argparse
import logging
import re
import datetime
import csv

from requests.exceptions import HTTPError , ChunkedEncodingError, SSLError, Timeout
from urllib3.exceptions import MaxRetryError, ConnectionError

logging.basicConfig(level=logging.INFO)

#Configuración de common.py
from common import config
logger = logging.getLogger(__name__)


# Con RegEx validamos si esta bien formado el Link
is_well_formed_link= re.compile(r'^https?://.+/.+$')

# Si es un enlace relativo solo tendra la ruta interna
is_root_path=re.compile(r'^/.+$')

def _news_scraper(news_site_uid):
	host= config()['news_sites'][news_site_uid]['url']
	logging.info(' Beginning  SCRAPER  for: {}'.format(host))
	# Se instancia un Obj de Homepage del archivo news_pages_objects.py como news
	# los params son el UID y el HOST.
	# Coon el UID se obtienen los queries a navegar y con host se realiza el Request
	homepage=news.HomePage(news_site_uid, host)
 
	# Los articulos se agregaran en la lista articles
	articles=[]
	
	# Se van a iterar todos los articles guardados en article_links 
	# Despues se valiradan los enlaces correctos  y se capturará la informacion con fetch_article
	for link in homepage.article_links:
		article = _fetch_article(news_site_uid, host, link)
		if article:
			logger.info('Article fetched!!')
			articles.append(article)
			
   			
   			

	# Guardar ls articulos en un CSV con parametros como el UID y la fecha
	_save_articles(news_site_uid, articles)


def _save_articles(news_site_uid, articles):
    #Se definira una fecha de extraccion de los archivos con la fecha en formato Y_m_d
	now= datetime.datetime.now().strftime('%Y_%m_%d')
	# Ej: eluniversal_2020_06_02.csv
	out_filename= '{news_site_uid}_{datetime}_articles.csv'. format(news_site_uid=news_site_uid, datetime=now)
	# obtiene los encabezados del primer registro obtenido de un articulo
	# Con los cuales se guardara el archivo
	csv_headers = list(filter (lambda property: not property.startswith('_'), dir(articles[1])))
	with open(out_filename, mode='w+') as f:
		writer= csv.writer(f)
		writer.writerow(csv_headers)

		for article in articles:
			row = [ str(getattr(article, prop)) for prop in csv_headers]
			writer.writerow(row)


def _fetch_article (news_site_uid,host,link):
	logger.info('Start FETCHING article at {}'.format(link))
	article=None
 
	# Se usa try y excep t para tratar de capturar los links validos y que el programa no se termine si encuentra errores
 	#  Con Build link se construira el enlace completo si solo tiene un enlace relativo
	try:
		article= news.ArticlePage(news_site_uid, _build_link(host, link))
	# Capturar errores  que uno puede y sabe atrapart
	# HTTPError: Errores cuando los vínculos no existen
	# MaxRetryError: Errores cuando van al infinito y no accede al sitio web
	except (HTTPError, MaxRetryError, ConnectionError, ChunkedEncodingError, SSLError, Timeout) as e :
		logger.warning('Error! HTTP ERR  by Exception ', exc_info=False)

	
	# si pasa el try y excep.. tenemos un articulo pero no tiene el body no sirve se captura el error
	if article and not article.url:
			logger.warning('Invalid!!  Article without URL')
			return None	
	
	if article and not article.body:
			logger.warning('Invalid!!  Article without body')
			return None

		
	return article

# utiliza Expresiones regulares para saber si los links contienen todos los criterios de una URL
# de lo contrario creara su respectivo enlace
def _build_link(host,link):
	if is_well_formed_link.match(link):
		return link

	#Si solo falta la mitad deberá ponerse host link
	elif is_root_path.match(link):
		return '{}{}'.format(host,link)
	# Si no tiene ruta raiz se debe formar con el Host/link concatenandolo
	else:
		return '{host}/{uri}'. format(host=host, uri=link)

if __name__== '__main__':
    #Es un parseador de argumentos al momento de pasar args a main.py  
	parser= argparse.ArgumentParser()
	#Acceder a los parametros del archivo config.py devuelve un iterador que se volvera una lista con list
	news_sites_choices=list(config()['news_sites'].keys())
	# Argumentos son obligatorios
	parser.add_argument('news_site',
						help= 'The news site taht you want to scrape!',
						type= str,
						choices = news_sites_choices
						)
	#Parsear y crear un Obj con los argumentos para iuniciar  el codigo y los pasa en los params de la funcion
	args= parser.parse_args()
	_news_scraper(args.news_site)