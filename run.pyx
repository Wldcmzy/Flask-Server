
if __name__ == '__main__':
    from config import *
    from moduleslink import *
    generate_home_html()

    app.debug = DEBUG
    app.run(HOST, PORT)
