import sys
print(sys.platform)
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
m.click(x_dim//2, y_dim//2, 1)      #取整除 - 向下取接近除数的整数
k.type_string('Hello, World!')