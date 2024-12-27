
# python wrapper for package sigs.k8s.io/controller-runtime/pkg/client/interceptor within overall package client
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy pkg sigs.k8s.io/controller-runtime/pkg/client

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _client
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from client import interceptor
# and then refer to everything using interceptor. prefix
# packages imported by this package listed below:

from . import client



# ---- Types ---


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---

# Python type for struct interceptor.Funcs
class Funcs(go.GoClass):
	"""Funcs contains functions that are called instead of the underlying client's methods.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_client.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_client.IncRef(self.handle)
		else:
			self.handle = _client.interceptor_Funcs_CTor()
			_client.IncRef(self.handle)
	def __del__(self):
		_client.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'interceptor.Funcs{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'interceptor.Funcs ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def NewClient(interceptedClient, funcs):
	"""NewClient(object interceptedClient, object funcs) object
	
	NewClient returns a new interceptor client that calls the functions in funcs instead of the underlying client's methods, if they are not nil.
	"""
	return client.WithWatch(handle=_client.interceptor_NewClient(interceptedClient.handle, funcs.handle))


