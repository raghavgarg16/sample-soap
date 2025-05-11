""" SOAP Service for Getting User Data """

# Python packages
from spyne import Application, rpc, ServiceBase, Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne import ComplexModel

# Database connection
from config.database import Database


class UserInfo(ComplexModel):
    id = Integer
    name = Unicode
    email = Unicode
    phone = Unicode

class GetUserService(ServiceBase):
    @rpc(Unicode, _returns = UserInfo)
    def get_user_by_name(ctx, name):
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor(dictionary = True)

        cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
        user = cursor.fetchone()

        cursor.close()
        db.close_connection()

        if user:
            return UserInfo(id = user["id"], name = user["name"], email = user["email"], phone = user["phone"])

        else:
            return UserInfo(id = 0, name="Not found", email = "N/A")


# Create the SOAP application
get_user_app = Application(
    [GetUserService],
    tns = "spyne.getuserservice",
    in_protocol = Soap11(validator="lxml"),
    out_protocol = Soap11(),
)

# WSGI application for the SOAP service
get_user_wsgi_app = WsgiApplication(get_user_app)
