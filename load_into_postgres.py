import click
import psycopg as pg
import threading

@click.command()
@click.option('--dbname', default='postgres', help="Name of database")
@click.option('--password', prompt=True, hide_input=True)
@click.option('--user', default='postgres', help="Postgres Username")
@click.option('--ecu-ip', help="IP Address of the ECU")
@click.option('--db-host', default='localhost', help="Host of database. Can be IP or Domain")
def start_loading(dbname, password, user, ecu_ip, db_host):
    udpReader = UdpReader(ecu_ip)
    thread = threading.Thread(target=udpReader.serialHandler)
    thread.start()
    while True:
        with pg.connect(f'dbname={dbname}  user={user} password={password} host={db_host} port=5432') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM tilt;")
                cur.fetchone()
                for record in cur:
                    print(record)

if __name__ == '__main__':
    start_loading()

