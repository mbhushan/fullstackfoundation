from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi


# import CRUD operations from lesson1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create sessiona and connect to db
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br></br>"
                output += "</body></html>"
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, "File not found: %s" % self.path)


def main():
    try:
        server = HTTPServer(('', 8080), WebServerHandler)
        print "WebServer runnning... open localhost:8080/restaurants \
            in your browser!"
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C was pressed.. Shutting webserver down!"
        server.socket.close()


if __name__ == '__main__':
    main()
