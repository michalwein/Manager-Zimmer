from models.config import connection

def get_all_zimers():
    # Get the connection object
    conn = connection()

    try:
        with conn.cursor() as cursor:
            # Query to retrieve all the Zimmers and the phone of the landlord from landlords table by using Join method
            query = """
            SELECT z.NameZim, z.LocationZim, z.IsPool, z.IsJacuzzi, z.MidweekPrice, z.TypeZim, l.PhoneLand, z.IMG
            FROM Zimmers z
            JOIN landlords l ON z.LandID = l.LandLordID;
            """
            cursor.execute(query)
            res = cursor.fetchall()

            # Insert the result into a list variable
            zimers_list = []
            for row in res:
                zimers_list.append({
                    "NameZim": row[0],
                    "LocationZim": row[1],
                    "IsPool": row[2],
                    "IsZacuzzi": row[3],
                    "MidweekPrice": row[4],
                    "TypeZim": row[5],
                    "Phone": row[6],
                    "IMG": row[7]
                }) #.fromat(*row)

            return zimers_list

    finally:
        conn.close()  # Close the connection when done

