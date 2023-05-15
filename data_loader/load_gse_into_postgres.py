import click
import psycopg2 as pg
import threading
from udpRead import UdpReader

# @click.command()
# @click.option('--dbname', default='postgres', help="Name of database")
# @click.option('--password', default='postgres', prompt=True, hide_input=True)
# @click.option('--user', default='postgres', help="Postgres Username")
# @click.option('--ecu-ip', default='192.168.0.6', help="IP Address of the ECU")
# @click.option('--db-host', default='localhost', help="Host of database. Can be IP or Domain")
def start_loading(dbname, password, user, ecu_ip, db_host):
    udpReader = UdpReader(ecu_ip)
    conn = pg.connect(f'dbname={dbname}  user={user} password={password} host={db_host} port=5432')

    while True:
        try:
            data = udpReader.getData(f"sAll;tc;pt;")
            if (data is not None):
                data = str(data, encoding='utf-8')
                sAll, tc, pt,  *extra = data.split(';')
                print(sAll)
                tc = [float(t) for t in tc.split(',') if t != '']
                sAll = [int(s) for s in sAll.split(',') if s != '']
                pt = [float(p) for p in pt.split(',') if p != '']

                print("PT: ", pt)
        except KeyboardInterrupt as k:
            conn.close()
            exit(0)
        except Exception as e:
            click.secho(f"fucked {e}", fg='red')
        with conn.cursor() as cur:
            cur.execute("INSERT INTO gse_pt (pt1, pt2, pt3, pt4) VALUES (%s, %s, %s, %s);", (pt[3], pt[4], pt[5] , pt[0]))
        conn.commit()

if __name__ == '__main__':
        print("GSE started")
        start_loading('postgres', 'postgres', 'postgres', '192.168.0.5', 'postgres')

