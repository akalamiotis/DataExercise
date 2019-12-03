import os
import datetime
import csv
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from data.models import Record, Meter
from django.core.files.storage import default_storage

class Command(BaseCommand):
    help = 'load the data from files in sample_data folder into the database'

    def handle(self, *args, **options):
        path = os.path.join(settings.MEDIA_ROOT, "sample_data")
        dateformat = "%Y%m%d"

        for file in os.listdir(path):
            with default_storage.open(os.path.join("sample_data", file), 'r') as csvfile:

                read_data = csv.reader(csvfile, delimiter=',')

                file_name = ""

                for row in read_data:
                    if row[0] == "HEADR" and len(row) == 6: 
                        timeformat = "%H%M%S"
                        file_name = row[5]
                        check_file_exist = Record.objects.filter(file_gen_number=file_name)
                        if len(check_file_exist) == 0:
                            new_record = Record.objects.create(
                                file_type_id = row[1],
                                company_id = row[2],
                                file_creation_date = datetime.datetime.strptime(row[3], dateformat),
                                file_upload_datetime = datetime.datetime.now(),
                                file_creation_time = datetime.datetime.strptime(row[4], timeformat),
                                file_gen_number = row[5]
                            )
                    
                    if row[0] == "CONSU" and len(row) == 5:
                        timeformat_cons = "%H%M"
                        check_file_exist = Record.objects.filter(file_gen_number=file_name)
                        if len(check_file_exist) == 0:
                            new_meter = Meter.objects.create(
                                record = Record.objects.last(),
                                meter_number = row[1],
                                measurement_date = datetime.datetime.strptime(row[2], dateformat),
                                measurement_time = datetime.datetime.strptime(row[3], timeformat_cons),
                                consumption = row[4]
                            )
                csvfile.close()



