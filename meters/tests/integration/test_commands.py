import pytest
from django.core.management import call_command
from meters.models.reading import Reading
from unittest.mock import patch, mock_open


mock_data = ('026|1200023305967|V|\n'
            '028|TEST|D|\n'
            '030|S|20160222000000|56311.0|||T|N|\n'
            '026|1200023305967|V|\n'
            '028|TEST|D|\n'
            '030|S|20160222000000|56311.0|||T|N|\n')

@pytest.mark.django_db
def test_upload():
    with patch('builtins.open', mock_open(read_data=mock_data)):
        call_command('upload', 'file')
        reading = Reading.objects.get(mpan='1200023305967')
        assert reading.meter_id == 'TEST'
