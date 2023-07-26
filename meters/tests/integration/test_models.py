import pytest
import decimal
from datetime import datetime
from django.utils.timezone import make_aware
from meters.models.reading import Reading


@pytest.fixture
def reading(db):
    timestamp = datetime.strptime('20160222000000', "%Y%m%d%H%M%S")
    return Reading.objects.create(
        mpan="1200023305968",
        meter_id="TEST",
        register_id ="S",
        reading="10000.0",
        reading_timestamp=make_aware(timestamp),
        filename="test.uff"
    )

def test_filter(reading):
    assert Reading.objects.filter(mpan="1200023305968").exists()

def test_get(reading):
    assert Reading.objects.get(mpan="1200023305968").reading == decimal.Decimal("10000.0")
