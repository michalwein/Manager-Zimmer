from models.config import connection

def specific_Zimmer(ZimID):

    conn = connection()
    try:
        with conn.cursor() as cursor:
            query = f"""SELECT z.NameZim, z.LocationZim, z.Area, z.IsPool, z.IsJacuzzi, z.MidweekPrice, z.TypeZim, z.NumRoom, z.GeneralSpecific, l.PhoneLand, l.NameLand
                        FROM Zimmers z
                        JOIN LandLords l
                        ON z.LandID = l.LandLordID
                        WHERE z.ZimID = {ZimID} """

            cursor.execute(query)
            res = cursor.fetchall()

            #Insert the result into a list variable
            zimmers_list = []
            for row in res:
                zimmers_list.append({
                    "NameZim": row[0],
                    "LocationZim": row[1],
                    "Area": row[2],
                    "IsPool": row[3],
                    "IsJacuzzi": row[4],
                    "MidweekPrice": row[5],
                    "TypeZim": row[6],
                    "NumRoom": row[7],
                    "GeneralSpecific": row[8],
                    "Phone": row[9],
                    "NameLand": row[10]
                })
            return zimmers_list

    finally:
        conn.close()



