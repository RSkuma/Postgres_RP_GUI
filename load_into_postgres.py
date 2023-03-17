import click
import psycopg as pg
import threading
from udpRead import UdpReader

@click.command()
@click.option('--dbname', default='postgres', help="Name of database")
@click.option('--password', default='postgres', prompt=True, hide_input=True)
@click.option('--user', default='postgres', help="Postgres Username")
@click.option('--ecu-ip', help="IP Address of the ECU")
@click.option('--db-host', default='localhost', help="Host of database. Can be IP or Domain")
def start_loading(dbname, password, user, ecu_ip, db_host):
    udpReader = UdpReader(ecu_ip)
    thread = threading.Thread(target=udpReader.serialHandler)
    thread.start()
    while True:
        try:
            data = udpReader.getData(f"tc;sAll;")
            if (data is not None):
                data = str(data, encoding='utf-8')
                tc, sAll, sol, *extra = data.split(';')

                print("TC: ", tc)
                print("Solenoid: ", sAll)
                """print("RTT: ", time.time_ns() - last_actuation)
                last_actuation = time.time_ns()"""
        except Exception as e:
            print("fucked")
        with pg.connect(f'dbname={dbname}  user={user} password={password} host={db_host} port=5432') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM tilt;")
                sAll = sAll.split(',')
                cur.execute("INSERT INTO soleniods (he, lng, lox, pv1, pv2, mvas) VALUES (%s, %s, %s, %s, %s, %s);", 
                        sAll[0], sAll[1], sAll[2], sAll[3], sAll[4], sAll[5])
                # cur.fetchone()
                # for record in cur:
                #     print(record)

if __name__ == '__main__':
    start_loading()

