import socket

import udpRead

while True:
    print("----------------")
    # Attempt to get data from Arduino
    udpReader = udpRead.UdpReader('ecu')
    try:
        data = udpReader.getData(f"tc;sAll;")

        if (data is not None):
            data = str(data, encoding='utf-8')
            tc, sAll, *extra = data.split(';')
            # tc = thermocouples, sAll = solenoid valve states, sol = control box switch states

            tc = tc.split(",")
            if not tc[-1]:
                del tc[-1]

            sAll = sAll.split(",")
            if not sAll[-1]:
                del sAll[-1]

            print("TC: ", tc)
            print("Solenoid: ", sAll)
    except Exception as e:
        print(e)



