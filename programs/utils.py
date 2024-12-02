import os, sys
from . import *

def wait_for_keypress():
	message = f"\n  {B_ON_W}Press a key to continue...{RESET}"
	if os.name == 'nt':  # Windows
		import msvcrt
		print(message, end = '', flush = True)
		msvcrt.getch()
	else:  # Linux y macOS
		print(message, end = '', flush = True)
		import termios
		import tty
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

__all__ = ['wait_for_keypress']