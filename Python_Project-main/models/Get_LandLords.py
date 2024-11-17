from models.config import connection

def get_LandLords():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            query = """
            SELECT NameLand, PhoneLand, EmailLand 
            FROM LandLords
            """
            cursor.execute(query)
            res = cursor.fetchall()

            Land_list = []
            for row in res:
                Land_list.append({
                    "NameLand": row[0],
                    "PhoneLand": row[1],
                    "EmailLand": row[2],
                })

            return Land_list

    finally:
        conn.close()
