import uuid
from astronaut.domain.astronaut import Astronaut


def test_astronaut_model_init():
    code = uuid.uuid4()
    astronaut = Astronaut(code, size=200, price=10,
                          longitude='-0.09998975',
                          latitude='51.75436293')
    assert astronaut.code == code
    assert astronaut.size == 200
    assert astronaut.price == 10
    assert astronaut.longitude == -0.09998975
    assert astronaut.latitude == 51.75436293


def test_astronaut_model_from_dict():
    code = uuid.uuid4()
    astronaut = Astronaut.from_dict(
        {
            'code': code,
            'size': 200,
            'price': 10,
            'longitude': '-0.09998975',
            'latitude': '51.75436293'
        }
    )
    assert astronaut.code == code
    assert astronaut.size == 200
    assert astronaut.price == 10
    assert astronaut.longitude == -0.09998975
    assert astronaut.latitude == 51.75436293
