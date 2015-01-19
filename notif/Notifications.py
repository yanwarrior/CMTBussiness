import wx

class Notifications:
	
	def __init__(self, message):
		self.message = message
		self.app = wx.App()
		
	def notifError(self):
		modal = wx.MessageDialog(
			None, self.message,
			'Error !', wx.ICON_ERROR
			)
		modal.ShowModal()
	
	def notifSuccess(self):
		modal = wx.MessageDialog(
			None, self.message,
			'Success !', wx.OK
			)
		modal.ShowModal()
	
	def notifInfo(self):
		modal = wx.MessageDialog(
			None, self.message,
			'Information', wx.ICON_INFORMATION
			)
		modal.ShowModal()
	
	def notifQuestion(self):
		modal = wx.MessageDialog(
			None, self.message,
			'Ask Question ?', wx.ICON_QUESTION
			)
		modal.ShowModal()
	
	def notifAccepting(self):
		modal = wx.MessageDialog(
			None, self.message,
			'Are You Sure, Broo ?', wx.YES_NO
			)
		ask = modal.ShowModal()
		
		if ask == wx.ID_YES:
			return True
		else:
			return False
	
	def notifWarning(self):
		modal = wx.MessageDialog(
				None, self.message,
				'Warning !', wx.ICON_WARNING
			)
		modal.ShowModal()
	
	def setMessage(self, message):
		self.message = message
	
	def __del__(self):
		self.app.MainLoop()
'''
notif = Notifications("Testing Questions")
notif.notifQuestion()
notif.setMessage("Testing Accepting")
print notif.notifAccepting()
'''
		
		

