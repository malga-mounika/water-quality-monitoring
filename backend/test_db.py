from sqlalchemy import text

from app.database import engine


try:
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    current_database(),
                    current_schema(),
                    current_user,
                    version()
            """)
        ).fetchone()

        print("Database connected successfully!")
        print("Database:", result[0])
        print("Schema:", result[1])
        print("User:", result[2])
        print("PostgreSQL:", result[3])

except Exception as e:
    print("Database connection failed!")
    print(e)