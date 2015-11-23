import routes

__author__ = 'Burgy Benjamin & Cornaz Jonathan'
__version__ = 0.1
__host__ = 'localhost'
__debug_mode__ = True

if __name__ == '__main__':
    routes.app.run(__host__, debug=__debug_mode__)
