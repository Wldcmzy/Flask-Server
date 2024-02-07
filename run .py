
# if __name__ == '__main__':

#     from config import *
#     from moduleslink import *
#     generate_home_html()

#     app.debug = DEBUG
#     app.run(HOST, PORT)


if __name__ == '__main__':
    from gevent import pywsgi
    from config import *
    from moduleslink import *
    generate_home_html()
    print(f'Running on Port: {PORT}')
    server = pywsgi.WSGIServer((HOST,PORT), app)
    server.serve_forever()
    