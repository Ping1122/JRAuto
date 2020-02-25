from win32gui import GetWindowText, GetWindowRect, EnumWindows

window = []

def callback(hwnd, extra):
	global window
	if "MuMu" in GetWindowText(hwnd):
		window = GetWindowRect(hwnd)

def main():
    EnumWindows(callback, None)
    print(window)

if __name__ == '__main__':
    main()