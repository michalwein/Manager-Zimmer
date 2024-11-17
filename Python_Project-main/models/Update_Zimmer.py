from models.config import connection

def Update_Zimmer(NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, IMG, NameZimmer):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            query = """
                UPDATE Zimmers
                SET 
                    NameZim = ?,
                    LocationZim = ?,
                    Area = ?,
                    IsPool = ?,
                    IsJacuzzi = ?,
                    MidweekPrice = ?,
                    EndWeekPrice = ?,
                    TypeZim = ?,
                    NumRoom = ?,
                    GeneralSpecific = ?,
                    IMG = ?
                WHERE
                    NameZim = ?
            """
            print("Executing query with values:")
            print(NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, IMG)
            cursor.execute(query, (NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, IMG, NameZimmer))
            conn.commit()
            print("The Zimmer updated successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()