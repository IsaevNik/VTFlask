from logging import FileHandler, WARNING, Formatter

file_handler = FileHandler('logs/errorlog.txt', mode='a')
format_error = Formatter("##%(asctime)s - %(message)s\n", datefmt='%H:%M:%S %d/%m/%Y')
file_handler.setFormatter(format_error)
file_handler.setLevel(WARNING)
