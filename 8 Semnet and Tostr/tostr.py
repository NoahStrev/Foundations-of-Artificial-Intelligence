#	converts things to strings -- even tuples, lists, and dicts

import types
import string

def tostr(x):
	t = type(x)
	#print("type is ************************ ", t)
	if isinstance(x, dict):
		return '{' + string.join( \
			map( lambda k,d=x: tostr(k)+": "+tostr(d[k]), \
			x.keys() ), ", " ) + "}"

	if isinstance(x, list):  
		#print('okedoke sarge')
		stringv = ","
		return '[' + stringv.join(
	 		map( lambda i: tostr(i), x)) 	 + "]"
	return str(x)
