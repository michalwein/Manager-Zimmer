from models.config import connection

def Delete_Zimmer(NameZim):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            query_to_delete = "DELETE FROM Zimmers WHERE NameZim = ?"
            cursor.execute(query_to_delete, (NameZim,))
            rows_deleted = cursor.rowcount

            if rows_deleted == 0:
                print(f"No Zimmer found with the name '{NameZim}'.")
            else:
                conn.commit()
                print("The Zimmer deleted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()

