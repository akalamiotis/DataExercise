import datetime

from data.models import Meter, Record
from django.test import TestCase


class RecordTestCase(TestCase):
    def setUp(TestCase):
        dateformat = "%Y%m%d"
        timeformat = "%H%M%S"
        Record.objects.create(
            file_type_id = "SMRT",
            company_id = "GAZ",
            file_creation_date = datetime.datetime.strptime("20191203", dateformat),
            file_upload_datetime = datetime.datetime.strptime("20191204", dateformat),
            file_creation_time = datetime.datetime.strptime("000123", timeformat),
            file_gen_number = "PN007505"
        )
    
    def test_record(self):
        dateformat = "%Y%m%d"
        timeformat = "%H%M%S"
        test_record = Record.objects.get(
            file_creation_date = datetime.datetime.strptime("20191203", dateformat),
            file_upload_datetime = datetime.datetime.strptime("20191204", dateformat),
            file_creation_time = datetime.datetime.strptime("000123", timeformat),
            file_gen_number = "PN007505"
        )
        self.assertEqual(test_record.company_id, "GAZ")
        self.assertEqual(test_record.file_type_id, "SMRT")


class MeterTestCase(TestCase):
    def setUp(TestCase):
        dateformat = "%Y%m%d"
        timeformat = "%H%M"
        test_meter = Meter.objects.create(
            record = Record.objects.last(),
            meter_number = "0000000002",
            measurement_date = datedatetime.datetime.strptime("20191203", dateformat),
            measurement_time = datetime.datetime.strptime("2337", timeformat_cons),
            consumption = 9.89
        )
        self.assertEqual(test_meter.consumption, 9.89)
        self.assertEqual(test_meter.meter_number, "0000000002")
