from datetime import datetime
from django.utils.timezone import make_aware
from meters.management.commands.upload import load_lines, parse_lines
from unittest.mock import patch, mock_open


mock_data = ('026|1200023305967|V|\n'
            '028|F75A 00802|D|\n'
            '030|S|20160222000000|56311.0|||T|N|\n')


def test_load_lines():
    with patch('builtins.open', mock_open(read_data=mock_data)):
        lines = ['026|1200023305967|V|\n' , '028|F75A 00802|D|\n',
                 '030|S|20160222000000|56311.0|||T|N|\n']
        
        assert load_lines('file') == lines


def test_parse_lines():
    with patch('builtins.open', mock_open(read_data=mock_data)):
        timestamp = datetime.strptime('20160222000000', "%Y%m%d%H%M%S")
        record = ('1200023305967', 'F75A 00802', 'S', '56311.0',
                  make_aware(timestamp), 'file')
        
        assert [r for r in parse_lines('file')] == [record]
