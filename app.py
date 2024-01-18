import tornado.web
import tornado.ioloop

D = {
    "alice": {"name": "Alice Smith", "dob": "Jan. 1", "email": "alice@example.com"},
    "bob": {"name": "Bob Jones", "dob": "Dec. 31", "email": "bob@bob.xyz"},
    "carol": {"name": "Carol Ling", "dob": "Jul. 17", "email": "carol@example.com"},
    "dave": {"name": "Dave N. Port", "dob": "Mar. 14", "email": "dave@dave.dave"},
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            L = self.request.path.split("/")
            uname = L[2]
            info = D.get(uname)
            if info:
                self.render("profilepage.html",
                            name=info.get("name"),
                            dateOfBirth=info.get("dob"),
                            email=info.get("email")
                            )
            else:
                self.write("User not found")
        except Exception as e:
            self.set_status(500)
            self.write(f"Internal Server Error: {str(e)}")


def make_app():
    return tornado.web.Application([
        ("/profile/.*", ProfileHandler),
    ], template_path="templates")


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

