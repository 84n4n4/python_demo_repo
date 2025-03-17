import datetime as dt
import json



def main():
    qr = {
        'time': dt.datetime.now(),
        'id': 'asdf',
        'direction': 'min',
        'frequency': dt.timedelta(seconds=1),
    }

    if 'value' not in qr.keys():
        qr['value'] = None

    print(qr['id'])
    print(qr['value'])

    print(qr)
    # print(json.dumps(qr))

    qr['time'] = qr['time'].isoformat()
    qr['frequency'] = str(qr['frequency'])
    print(json.dumps(qr))


if __name__ == '__main__':
    main()
