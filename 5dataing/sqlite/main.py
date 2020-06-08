import pandas as pd
import argparse
import logging
logging.basicConfig(level=logging.INFO)

from article import Article
from base import Base, engine, Session
logger = logging.getLogger(__name__)

def main(filename):
    Base.metadata.create_all(engine)
    session=Session()
    articles=pd.read_csv(filename)
    
    print(articles.head())

    for index, row in articles.iterrows():
        logger.info('Loading article id uid  {}'.format(row['uid']))
        article = Article(row['uid'],
                        row['body'],
                        row['title'],
                        row['host'],
                        row['newspaper_uid'],
                        row['n_tokens_title'],
                        row['n_tokens_body'],
                        row['url']
                        )
        session.add(article)
    session.commit()
    session.close()

if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help=' The file you want to load into the DB',
                        type=str
                        )
    args= parser.parse_args()
    
    main(args.filename)