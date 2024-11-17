from models.config import connection

# sign up page

def sign_up(NameLand, PhoneLand, EmailLand, Password_L):
    conn = connection()
    try:
        # Use the connection object to create a cursor
        with conn.cursor() as cursor:
            add_landlord_query = """
                                INSERT INTO LandLords (NameLand, PhoneLand, EmailLand, Password_L)
                                VALUES (?, ?, ?, ?)
                            """
            cursor.execute(add_landlord_query, (NameLand, PhoneLand, EmailLand, Password_L))
            res = cursor.fetchall()
            if res:
                return True
            return False
    finally:
        conn.close()
