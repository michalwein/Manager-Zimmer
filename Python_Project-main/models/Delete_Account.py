from models.config import connection

def Delete_account(nameLand):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            # Find LandLordID by nameLand
            query_to_find_id_land = """
                SELECT TOP 1 LandLordID
                FROM LandLords
                WHERE NameLand = ?
            """
            cursor.execute(query_to_find_id_land, (nameLand,))
            result = cursor.fetchone()
            if result:
                LandID = result[0]

                # Delete Zimmers associated with the LandLord
                query_to_delete_zimmer = """
                    DELETE FROM Zimmers WHERE LandID = ?
                """
                cursor.execute(query_to_delete_zimmer, (LandID,))

                # Delete the LandLord
                query_to_delete_land = """
                    DELETE FROM LandLords WHERE LandLordID = ?
                """
                cursor.execute(query_to_delete_land, (LandID,))

                # Commit the transaction
                conn.commit()
                print("Your account and associated Zimmers were deleted successfully.")
            else:
                print("No LandLord found with the provided name.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()

