from models.config import connection

def sort_by_name_Land(nameLand):
    conn = connection()

    try:
        with conn.cursor() as cursor:
            query ="""
                SELECT NameLand, PhoneLand, EmailLand
                FROM LandLords
                WHERE NameLand = ?
                """
            cursor.execute(query, (nameLand,))
            res = cursor.fetchall()

            Land_list = []
            for row in res:
                Land_list.append({
                    "NameLand": row[0],
                    "PhoneLand": row[1],
                    "EmailLand": row[2]
                })
            return Land_list
    finally:
        conn.close()


def sort_by_Phone_Land(PhoneLand):
    conn = connection()

    try:
        with conn.cursor() as cursor:
            query ="""
                SELECT NameLand, PhoneLand, EmailLand
                FROM LandLords
                WHERE PhoneLand = ?
                """
            cursor.execute(query, (PhoneLand,))
            res = cursor.fetchall()

            Land_list = []
            for row in res:
                Land_list.append({
                    "NameLand": row[0],
                    "PhoneLand": row[1],
                    "EmailLand": row[2]
                })
            return Land_list
    finally:
        conn.close()

