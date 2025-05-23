"""
 ----------------------------------------------------------------- *
 * (C) Copyright IBM Corporation 2024.                               *
 *                                                                   *
 * The source code for this program is not published or otherwise    *
 * divested of its trade secrets, irrespective of what has been      *
 * deposited with the U.S. Copyright Office.                         *
 * -----------------------------------------------------------------

"""
# python wrapper for package github.ibm.com/Michael-Honaker/kubernetes-lite/kubernetes_lite/go_wrapper/pkg/envtest/server within overall package wrapper
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy pkg -no-make -author=Michael Honaker -email=michael.honaker@ibm.com -name=wrapper github.ibm.com/Michael-Honaker/kubernetes-lite/kubernetes_lite/go_wrapper/pkg/client github.ibm.com/Michael-Honaker/kubernetes-lite/kubernetes_lite/go_wrapper/pkg/envtest/setup github.ibm.com/Michael-Honaker/kubernetes-lite/kubernetes_lite/go_wrapper/pkg/envtest/server

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _wrapper
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from wrapper import server
# and then refer to everything using server. prefix
# packages imported by this package listed below:




# ---- Types ---


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---
DefaultContextName = "default-context"
"""
Default settings for the kube config

"""
DefaultNamespace = "default"
"""
Default settings for the kube config

"""


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---

# Python type for interface server.EnvTestEnvironment
class EnvTestEnvironment(go.GoClass):
	"""EnvTestEnvironment defines the interface for starting and stopping an EnvTest server as well as\nfetching a generic kube config\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_wrapper.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_wrapper.IncRef(self.handle)
		else:
			self.handle = 0
	def GetKubeConfig(self):
		"""GetKubeConfig() []int, str"""
		return go.Slice_byte(handle=_wrapper.server_EnvTestEnvironment_GetKubeConfig(self.handle))
	def Start(self):
		"""Start() []int, str"""
		return go.Slice_byte(handle=_wrapper.server_EnvTestEnvironment_Start(self.handle))
	def Stop(self):
		"""Stop() str"""
		return _wrapper.server_EnvTestEnvironment_Stop(self.handle)


# ---- Structs ---


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def NewEnvTestEnvironment():
	"""NewEnvTestEnvironment() object, str"""
	return EnvTestEnvironment(handle=_wrapper.server_NewEnvTestEnvironment())
def NewEnvTestEnvironmentWithPath(path):
	"""NewEnvTestEnvironmentWithPath(str path) object, str"""
	return EnvTestEnvironment(handle=_wrapper.server_NewEnvTestEnvironmentWithPath(path))


