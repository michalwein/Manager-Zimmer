from models.config import connection

def Add_Zimmer(NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, PhoneLand, NameLand, EmailLand):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            # Start transaction
            cursor.execute("BEGIN TRANSACTION")

            # Check if LandLord already exists
            check_landlord_query = """
                SELECT LandLordID 
                FROM LandLords 
                WHERE NameLand = ? AND PhoneLand = ? AND EmailLand = ?
            """
            cursor.execute(check_landlord_query, (NameLand, PhoneLand, EmailLand))
            result = cursor.fetchone()

            if result:
                LandID = result[0]
            else:
                # Add new LandLord if not exists
                add_landlord_query = """
                    INSERT INTO LandLords (NameLand, PhoneLand, EmailLand)
                    VALUES (?, ?, ?)
                """
                cursor.execute(add_landlord_query, (NameLand, PhoneLand, EmailLand))

                # Get the new LandLordID
                get_landlord_id_query = """
                    SELECT TOP 1 LandLordID 
                    FROM LandLords 
                    WHERE NameLand = ? AND PhoneLand = ? AND EmailLand = ? 
                    ORDER BY LandLordID DESC
                """
                cursor.execute(get_landlord_id_query, (NameLand, PhoneLand, EmailLand))
                LandID = cursor.fetchone()[0]

            # Add Zimmer Details with foreign key LandID
            add_zimmer_query = """
                INSERT INTO Zimmers (NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, LandID)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(add_zimmer_query,
                           (NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, LandID))

            # Commit transaction
            cursor.execute("COMMIT TRANSACTION")

    except Exception as e:
        # Rollback in case of error
        cursor.execute("ROLLBACK TRANSACTION")
        print(f"Error: {e}")

    finally:
        # Close the connection
        conn.close()

