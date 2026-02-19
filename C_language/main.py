
#!/usr/bin/python3
import ctypes

# Загружаем библиотеку
lib = ctypes.CDLL('./libexample.so')

# Обьявляем сигнатуру функции
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

lib.print_message.argtypes = [ctypes.c_char_p]

# Вызываем функци
result = lib.add(5, 3)
print(f"5 + 3 = {result}")

lib.print_message(b"Hello from Python")