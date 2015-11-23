import constants
import routes

if __name__ == '__main__':
    routes.app.run(constants.__host__, debug = constants.__debug_mode__)
