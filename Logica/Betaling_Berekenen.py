from datetime import datetime, time
from Services import Rest_Service
import time


def berekenBedrag(inrijtijd,uitrijtijd):
    fmt = '%H:%M'
    d1 = datetime.strptime(inrijtijd, fmt)
    d2 = datetime.strptime(uitrijtijd, fmt)

    # Convert to Unix timestamp
    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())

    uurTarief = 0
    dagTarief = 0

    minuten = int(d2_ts-d1_ts) / 60

    for tarief in Rest_Service.getTarieven(1)['response']:
        if tarief['type'] == 'Uur':
            uurTarief = tarief['waarde']
        if tarief['type'] == 'Dag':
            dagTarief = tarief['waarde']

    tariefMinuten = float(uurTarief)/60
    if (minuten*tariefMinuten) > float(dagTarief):
        return float(dagTarief)
    else:
        return minuten*tariefMinuten