class CFType(object):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return '<%s "%s">' % (self.__class__.__name__, self.value)
	
	def __repr__(self):
		return '%s(%s)' % (self.__class__.__name__, self.value)

class CFBoolean(CFType):
	pass

class CFInteger(CFType):
	pass

class CFReal(CFType):
	pass

class CFDate(CFType):
	TIMESTAMP_APPLE = 0
	TIMESTAMP_UNIX  = 1;
	DATE_DIFF_APPLE_UNIX = 978307200
	
	def __init__(self, value, type=None):
		if type == None:
			type = self.__class__.TIMESTAMP_APPLE
		self.type = type
		super(CFDate, self).__init__(value)

class CFData(CFType):
	# Base64 encoded data
	DATA_BASE64 = 0
	# Raw data
	DATA_RAW = 1
	
	def __init__(self, value, type=None):
		if type == None:
			type = self.__class__.DATA_RAW
		self.type = type
		super(CFData, self).__init__(value)

class CFString(CFType):
	pass

class CFArray(CFType):
	pass

class CFDictionary(CFType):
	pass