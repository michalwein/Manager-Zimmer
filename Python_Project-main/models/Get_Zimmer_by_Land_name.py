from models.config import connection

def get_all_zimers_by_land_name(nameLand):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            query = """
            SELECT z.NameZim, z.LocationZim, z.IsPool, z.IsJacuzzi, z.MidweekPrice, z.TypeZim, l.PhoneLand, z.IMG
            FROM Zimmers z
            JOIN landlords l ON z.LandID = l.LandLordID
            WHERE l.NameLand = ?
            """
            cursor.execute(query, (nameLand,))
            res = cursor.fetchall()

            zimers_list = []
            for row in res:
                zimers_list.append({
                    "NameZim": row[0],
                    "LocationZim": row[1],
                    "IsPool": row[2],
                    "IsJacuzzi": row[3],
                    "MidweekPrice": row[4],
                    "TypeZim": row[5],
                    "Phone": row[6],
                    "IMG": row[7]
                })

            return zimers_list

    finally:
        conn.close()
