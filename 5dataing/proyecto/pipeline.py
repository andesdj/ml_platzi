import logging
loggin.basicConfig(level=logging.INFO)
import subprocess 

logger= logging.getLogger(__name__)
news_sites_uids=['eluniversal', 'elpais']

def main():
    logger.info('Starting  ETL process')
    _extract()
    _tranform()
    _load()
    
def _extract():
    logger.info('Starting  EXTRACT  process')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python', 'main.py', news_site_uid, cwd='./extract'])
        subprocess.riun(['find', '.', '-name',   '{}*'.format(news_site_uid),
                         '-exec', 'mv' , '{}'  '../trasnform/{}_.csv'.format(news_site_uid),
                         ';', cwd='./extract'])       

def _transform():
    logger.info('Starting  TRANSFORM  process')
    for news_site_uid in news-sites_uids:
        dirty_data_filename = '{}_.csv'.format(news_site_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform')
        subprocess.run(['rm', dirty_data_filename], cwd='./transform')
        subprocess.run(['mv', clean_data_filename, '../load/{}.csv'.format(news_site_uid)],
                       cwd='./transform')

def _load():
    logger.info('Starting  LOAD  process')   
    for news_sites_uids in news_sites_uids:
        clean_data_filename = '{}.csv'.format(news_site_uid)
        subprocess.run(['python', 'main.py', clean_data_filename], cwd='./load')
        subprocess.run(['rm', clean_data_filename, cwd='./load'])
    
if __name__ == '__main__':
    main()

