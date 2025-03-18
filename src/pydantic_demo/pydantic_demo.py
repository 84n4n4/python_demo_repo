import datetime as dt
from enum import Enum

from pydantic import BaseModel


class DirectionEnum(str, Enum):
    min = 'min'
    max = 'max'


class QueryResult(BaseModel):
    time: dt.datetime
    id: str
    direction: DirectionEnum
    frequency: dt.timedelta | None = None
    value: float | None = None


def main():
    dict_input = {
        'time': dt.datetime.now(),
        'id': 'asdf',
        'direction': DirectionEnum.min,
        'frequency': dt.timedelta(seconds=1)
    }

    qr = QueryResult.model_validate(dict_input)
    print(qr.id)
    print(qr.value)

    dict_qr = qr.model_dump()
    print(dict_qr)

    QueryResult.model_validate(dict_qr)

    # with open('tmp.schema.json', "w") as f:
    #     f.write(json.dumps(QueryResult.model_json_schema(), indent=2))


if __name__ == '__main__':
    main()
