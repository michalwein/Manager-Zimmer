from models.config import connection

# Login page - Checking if the lessor's name and password exist in the system

def Is_landLord(name_land, password):
    # Get the connection object
    conn = connection()

    # Use the connection object to create a cursor
    with conn.cursor() as cursor:
        query = f"SELECT nameLand FROM landlords WHERE nameLand = '{name_land}' AND Password_L = '{password}';"
        cursor.execute(query)
        res = cursor.fetchone()  # Getting the first row of the result (if any)
        if res:
            return True
        return False
