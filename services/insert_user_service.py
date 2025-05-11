""" SOAP Service for Inserting User Data """

# Python packages
from spyne import Application, rpc, ServiceBase, Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Database connection
from config.database import Database


class InsertUserService(ServiceBase):
    @rpc(Integer, Unicode, Unicode, Unicode, _returns = Unicode)
    def insert_user(ctx, user_id, user_name, user_email, user_phone):
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (id, name, email, phone) VALUES (%s, %s, %s, %s)",
                (user_id, user_name, user_email, user_phone),
            )
            conn.commit()
            return f"User {user_name} with ID {user_id} inserted successfully."

        except Exception as e:
            conn.rollback()
            return f"Failed to insert user: {str(e)}"

        finally:
            cursor.close()
            db.close_connection()


# Create the SOAP application
insert_user_app = Application(
    [InsertUserService],
    tns = "spyne.insertuserservice",
    in_protocol = Soap11(validator = "lxml"),
    out_protocol = Soap11(),
)

# WSGI application for the SOAP service
insert_user_wsgi_app = WsgiApplication(insert_user_app)
