""" SOAP Service for Updating User Data """

# Python packages
from spyne import Application, rpc, ServiceBase, Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Database connection
from config.database import Database


class UpdateUserService(ServiceBase):
    @rpc(Integer, Unicode, Unicode, Unicode, _returns=Unicode)
    def update_user(ctx, user_id, user_name, user_email, user_phone):
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "UPDATE users SET name=%s, email=%s, phone=%s WHERE id=%s",
                (user_name, user_email, user_phone, user_id),
            )
            conn.commit()
            if cursor.rowcount:
                return f"User with ID {user_id} updated successfully."
            else:
                return f"No user found with ID {user_id}."

        except Exception as e:
            conn.rollback()
            return f"Failed to update user: {str(e)}"

        finally:
            cursor.close()
            db.close_connection()


# Create the SOAP application
update_user_app = Application(
    [UpdateUserService],
    tns="spyne.updateuserservice",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

# WSGI application for the SOAP service
update_user_wsgi_app = WsgiApplication(update_user_app)