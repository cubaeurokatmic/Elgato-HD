# mod.zombi
from Components.Converter.Converter import Converter
from Components.Element import cached
from Tools.BoundFunction import boundFunction

class cnNameExtra(Converter, object):
	EXTENDED_DESCRIPTION = 0
	WideInfo = 1
	HDInfo = 2
	DolbyInfo = 3
	DolbyA = 4


	def __init__(self, type):
		Converter.__init__(self, type)
		if type == "ExtendedDescription":
			self.type = self.EXTENDED_DESCRIPTION
		elif type == "WideInfo":
			self.type = self.WideInfo
		elif type == "HDInfo":
			self.type = self.HDInfo
		elif type == "DolbyInfo":
			self.type = self.DolbyInfo		
		else:
			self.type = self.DolbyA

	@cached
	def getBoolean(self):
		event = self.source.event
		if not event:
			return False

		elif self.type == self.WideInfo:
			data = str(event.getComponentData())
			if "16:9" in data or "11" in data:
				return True
			return False
		elif self.type == self.HDInfo:
			data = str(event.getComponentData())
			if "11" in data or "HDTV" in data:
				return True
			return False
		elif self.type == self.DolbyInfo:
			data = str(event.getComponentData())
			if "dolby" in data or "AC3" in data:
				return True
			if "Dolby" in data or "AC3" in data:
				return True	
			if "DOLBY" in data or "AC3" in data:
				return True	
			return False		
		elif self.type == self.DolbyA:
			data = str(event.getComponentData())
			if "Dolby 5.1" in data or "AC3 5.1" in data:
				return True
			if "Dolby Digital 5.1" in data or "AC3 5.1" in data:
				return True	
			return False

	boolean = property(getBoolean)

	@cached
	def getText(self):
		event = self.source.event
		if event is None:
			return ""

		if self.type == self.EXTENDED_DESCRIPTION:
			desc = event.getShortDescription()
			if desc and desc[-1] != '\n' and desc[-1] != ' ':
				desc += ':>>  '
			return desc + event.getExtendedDescription()

	text = property(getText)
