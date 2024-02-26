#--param POSTGRES_URL $POSTGRES_URL
import psycopg

def main(args):

    response = {"body": {}}

    with psycopg.connect(args.get("POSTGRES_URL")) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Execute a command: this creates a new table
            cur.execute("""
                CREATE EXTENSION IF NOT EXISTS "pgcrypto";
                CREATE TABLE IF NOT EXISTS nuvolaris_table (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    message varchar(100)        
                );
                """)

            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no SQL injections!)
            cur.execute("INSERT INTO nuvolaris_table(message) VALUES(%(message)s)",{"message":"Nuvolaris Postgres is up and running!"})
            # Make the changes to the database persistent

            # Query the database and obtain data as Python objects.
            cur.execute("SELECT message FROM nuvolaris_table")
            record = cur.fetchone()[0]
            response["body"] = record
            conn.commit()

    return response