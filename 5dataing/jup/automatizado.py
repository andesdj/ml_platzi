import argparse
import logging
import hashlib
import pandas as pd
import nltk
from nltk.corpus import stopwords
stop_words= set(stopwords.words('spanish'))
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse
ll='____________________________________________________________________________________________________________'
logger= logging.getLogger(__name__)

def main(filename):
	logger.info('Start cleaning process')
	df = _read_data(filename)
	newspaper_uid=_extract_newspaper_uid(filename)
	df = _add_newspaper_uid_column(df, newspaper_uid)
	df = _extract_host(df)
	df = _fill_missing_titles(df)
	df = _add_hash(df)
	df = _remove_jumplines(df)
	df =_enrich_token(df)
	df = _remove_duplicates(df)

# Ultima Funcion Agregar INDEX
	df = _setindex(df)
	_save_data(df,filename)
	return df

def _read_data(filename):
	logger.info('Reading file {}'. format (filename))
	return pd.read_csv(filename, encoding='utf-8', delimiter=',')

def _extract_newspaper_uid(filename):
	logger.info('Extracting newspaper UID')
	newspaper_uid= filename.split('_')[0]
	logger.info('Newspaper UID Detected: {}'.format(newspaper_uid))
	return newspaper_uid

def _add_newspaper_uid_column(df,newspaper_uid):
	logger.info('Filling News Papper Column with {}'. format(newspaper_uid))
	df['newspaper_uid']=newspaper_uid
	return df

def _extract_host(df):
	logger.info('Extracting host from urls')
	df['host'] = df['url'].apply( lambda url: urlparse(url).netloc)
	return df

def _fill_missing_titles(df):
	logger.info('Missing TITLES is Filling ')
	mtm=df['title'].isna()
	mt=(df[mtm]['url']
		.str.extract(r'(?P<missing_titles>[^/]+)$')
		.applymap(lambda title: title.split('-'))
		.applymap(lambda title_word_list: ' '.join(title_word_list))
	)
	df.loc[mtm , 'title']= mt.loc[:, 'missing_titles']
	return df

def _add_hash(df):
	logger.info('Generating HASH UID')
	uids= (df
         .apply(lambda row: hashlib.md5(bytes(row['url'].encode())) , axis=1 )
         .apply(lambda hash_object: hash_object.hexdigest())
      )
	df['uid']=uids
	
	return df

def _remove_jumplines(df):
	logger.info('Cleaning Body and Title Jumplines')
	stripb= (df
         .apply(lambda row: row['body'], axis=1)
         .apply(lambda body: list(body))
         .apply(lambda letters: list(map(lambda letter: letter.replace('\n', ''), letters)))
         .apply(lambda letters: list(map(lambda letter: letter.replace('“', ''), letters)))
         .apply(lambda letters: list(map(lambda letter: letter.replace('”', ''), letters)))
         .apply(lambda letters: list(map(lambda letter: letter.replace("'", ''), letters)))
         .apply(lambda letters: list(map(lambda letter: letter.replace('"', ''), letters)))
         .apply(lambda letters: ''.join(letters))
         )

	stript= (df
         .apply(lambda row: row['title'], axis=1)
         .apply(lambda body: list(body))
         .apply(lambda letters: list(map(lambda letter: letter.replace('\n', ''), letters)))
         .apply(lambda letters: list(map(lambda letter: letter.replace('“', ''), letters)))
         .apply(lambda letters: list(map(lambda letter: letter.replace('”', ''), letters)))
         .apply(lambda letters: list(map(lambda letter: letter.replace("'", ''), letters)))
         .apply(lambda letters: list(map(lambda letter: letter.replace('"', ''), letters)))
         .apply(lambda letters: ''.join(letters))
         )
	df['body']=stripb
	df['title']=stript
	return df



def _enrich_token(df):
	logger.info('Creating  Tokens for Title  & Body')
	df['n_tokens_title']=tokenize_column(df,'title')
	df['n_tokens_body']=tokenize_column(df,'body')
	return df

def tokenize_column(df, col_name):
    return (df
            .dropna()
            .apply(lambda row: nltk.word_tokenize(row[col_name]), axis=1)
            .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)) )
            .apply(lambda tokens: list( map(lambda token: token.lower(), tokens ) ))
            .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
            .apply(lambda valid_word_list: len(valid_word_list))
           )

def _remove_duplicates(df):
	logger.info('Removing Duplicates')
	df.drop_duplicates(subset=['title'], keep='first', inplace=True)
	return df

def _setindex(df):
	logger.info('Set INDEX UID')
	df.set_index('uid')
	return df

def _save_data(df,filename):
	logger.info('Save to CSV')
	clean_filename='clean_{}'.format(filename)
	df.to_csv(clean_filename, index=True, encoding='utf-8')


def _print_add(df):
	print( ' ')
	print( '             R E S U L T A D O                      ')
	print(ll)
	print(df[['host','title', 'n_tokens_title', 'n_tokens_body']])
	print(ll)
if  __name__ =='__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument('filename',
						help=' The Argument is The path of the dirty dataset iin CSV Format',
						type=str
						)
	args= parser.parse_args()
	df = main(args.filename)
	_print_add(df)

