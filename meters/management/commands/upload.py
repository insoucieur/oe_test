from datetime import datetime
from django.utils.timezone import make_aware
from django.core.management.base import BaseCommand, CommandParser
from meters.models.reading import Reading


def load_lines(file: str) -> list[str]:
    with open(file, "r", encoding='utf-8') as f:
        lines = f.readlines()

        return lines


def parse_lines(file: str) -> tuple:
    filename = file.split('/')[-1]
    meter_id = False

    for line in load_lines(file):
        if line.startswith('026'):
            mpan = line.split('|')[1]

        if line.startswith('028'):
            meter_id = line.split('|')[1]

        if meter_id:
            if line.startswith('030'):
                register_id, timestamp, reading = line.split('|')[1:4]
                timestamp = datetime.strptime(timestamp, "%Y%m%d%H%M%S")

                yield (mpan, meter_id, register_id, reading,
                       make_aware(timestamp), filename)


class Command(BaseCommand):
    help = "Process file and import to database"
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file', help="Path to file to process")
    

    def handle(self, *args, **options) -> None:
        file = options["file"]
        readings = [ Reading(
                        mpan=row[0],
                        meter_id=row[1],
                        register_id =row[2],
                        reading=row[3],
                        reading_timestamp=row[4],
                        filename=row[5]
                    ) for row in parse_lines(file) ]
        
        if not readings:
            print('Cannot find parsable data in file. Check file.')
        else:
            Reading.objects.bulk_create(readings)