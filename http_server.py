import http.server
import socketserver
import argparse
import logging

# Парсинг аргументов командной строки
parser = argparse.ArgumentParser(description='HTTP 1.1 Server')
parser.add_argument('-p', '--port', type=int, default=8000, help='Port number')
parser.add_argument('-d', '--directory', default='.', help='Directory to serve')
args = parser.parse_args()

# Конфигурация заголовков по умолчанию
DEFAULT_HEADERS = {
    'Access-Control-Allow-Origin': 'https://my-cool-site.com',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
}

# Настройка логирования
logging.basicConfig(filename='http_server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Класс обработчика запросов
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        for header, value in DEFAULT_HEADERS.items():
            self.send_header(header, value)
        super().end_headers()

# Создание и запуск сервера
handler_object = MyHttpRequestHandler
my_server = socketserver.TCPServer(("", args.port), handler_object)
logging.info(f"Server started on port {args.port}")
my_server.serve_forever()