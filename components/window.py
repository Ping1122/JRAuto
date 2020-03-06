from win32gui import GetWindowText, GetWindowRect, EnumWindows

class Window:
	def __init__(self):
		self.window = []

	def _callback(self, hwnd, extra):
		global window
		if "夜神模拟器" in GetWindowText(hwnd):
			self.window = GetWindowRect(hwnd)
	
	def getWindow(self):
		EnumWindows(self._callback, None)
		return self.window

 
