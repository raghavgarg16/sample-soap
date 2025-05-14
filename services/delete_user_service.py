""" SOAP Service for Deleting User Data """

# Python packages
from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Database connection
from config.database import Database


class DeleteUserService(ServiceBase):
    @rpc(Integer, _returns = Unicode)
    def delete_user(ctx, user_id):
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM users WHERE id = %s",
                (user_id,),
            )
            conn.commit()
            if cursor.rowcount:
                return f"User with ID {user_id} deleted successfully."
            else:
                return f"No user found with ID {user_id}."
        except Exception as e:
            conn.rollback()
            return f"Failed to delete user: {str(e)}"
        finally:
            cursor.close()
            db.close_connection()


# Create the SOAP application
delete_user_app = Application(
    [DeleteUserService],
    tns = "spyne.deleteuserservice",
    in_protocol = Soap11(validator="lxml"),
    out_protocol = Soap11(),
)

# WSGI application for the SOAP service
delete_user_wsgi_app = WsgiApplication(delete_user_app)
