import yaml
#Para no cargar cada momento los parametros en disco se parametriza una sola vez
__config = None

def config():
	global __config
	if not __config:
		with open('config.yaml', mode = 'r') as f:
			#Load is Deprecated
			#__config = yaml.load(f)
			__config = yaml.safe_load(f)
	return __config