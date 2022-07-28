from datetime import date, timedelta

JOURNEY_TYPE = {
    0xA0: 'single',
    0xA2: 'return',
    0x60: 'all-day'
}

COST = {
    0xA0: '£1.75',
    0xA2: '£3.30',
    0x60: '£4.20'
}

STATION = {
    0x1: 'Govan',
    0x2: 'Partick',
    0x3: 'Kelvinhall',
    0x4: 'Hillhead',
    0x5: 'Kelvinbridge',
    0x6: 'St. George\'s Cross',
    0x7: 'Cowcaddens',
    0x8: 'Buchanan Street',
    0x9: 'St. Enoch',
    0xA: 'Bridge Street',
    0xB: 'West Street',
    0xC: 'Shields Road',
    0xD: 'Kinning Park',
    0xE: 'Cessnock',
    0xF: 'Ibrox'
}

USES_LEFT = {
    0x3F: 2,
    0x7F: 1,
    0xFF: 0
}

def bytes_to_hexstr(data):
    return ' '.join([f'{x:02x}'.upper() for x in data])

class Ticket:
    def __init__(self, raw: str):
        self.raw = raw
        self.journey_type = None
        self.fare_type = None
        self.date = None
        self.last_station = None
        self.uses_left = None
        self.uid = None
        self.hash = None
        self._decode()

    def _decode(self):
        ticket_data = [int(char, base=16) for char in self.raw.strip().split()]
        self.journey_type = JOURNEY_TYPE.get(ticket_data[29])
        self.fare_type = 'adult'
        self.last_station = STATION.get(ticket_data[23], 'N/A')
        self.uses_left = USES_LEFT.get(ticket_data[12], 'Unlimited')
        self.uid = bytes_to_hexstr(ticket_data[:3] + ticket_data[4:8])
        self.hash = bytes_to_hexstr(ticket_data[-8:])
        self.cost = COST.get(ticket_data[29])
        ticket_days = int(bytes_to_hexstr(ticket_data[30:32]).replace(' ',''), base=16)
        origin_date = date(1997,1,1)
        self.date = origin_date + timedelta(days=ticket_days)

    def __str__(self) -> str:
        return f'UID: {self.uid}\n\tFare: {self.fare_type.upper()}\n\tJourney: {self.journey_type.upper()}\n\tStation: {self.last_station}'