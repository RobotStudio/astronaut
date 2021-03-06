import pytest

from astronaut.shared.domain_model import DomainModel
from astronaut.repository import memrepo


space1 = {
    'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'size': 215,
    'price': 39,
    'longitude': '-0.09998975',
    'latitude': '51.75436293',
}

space2 = {
    'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
    'size': 405,
    'price': 66,
    'longitude': '0.18228006',
    'latitude': '51.74640997',
}

space3 = {
    'code': '913694c6-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 60,
    'longitude': '0.27891577',
    'latitude': '51.45994069',
}

space4 = {
    'code': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',
    'size': 93,
    'price': 48,
    'longitude': '0.33894476',
    'latitude': '51.39916678',
}


@pytest.fixture
def spaces():
    return [space1, space2, space3, space4]


def _check_results(domain_models_list, data_list):
    assert len(domain_models_list) == len(data_list)
    assert all([isinstance(dm, DomainModel) for dm in domain_models_list])
    assert set([dm.code for dm in domain_models_list]) == \
            set([d['code'] for d in data_list])


def test_repository_list_without_parameters(spaces):
    repo = memrepo.MemRepo(spaces)
    assert repo.list() == spaces


def test_repository_list_with_filters_unknown_key(spaces):
    repo = memrepo.MemRepo(spaces)
    with pytest.raises(KeyError):
        repo.list(filters={'name': 'aname'})


def test_repository_list_with_filters_unknown_operator(spaces):
    repo = memrepo.MemRepo(spaces)
    with pytest.raises(ValueError):
        repo.list(filters={'price__in': [20, 30]})


def test_repository_list_with_filters_price(spaces):
    repo = memrepo.MemRepo(spaces)
    _check_results(repo.list(filters={'price': 60}), [space3])
    _check_results(repo.list(filters={'price__eq': 60}), [space3])
    _check_results(repo.list(filters={'price__lt': 60}), [space1, space4])
    _check_results(repo.list(filters={'price__gt': 60}), [space2])


def test_repository_list_with_filters_size(spaces):
    repo = memrepo.MemRepo(spaces)
    _check_results(repo.list(filters={'size': 93}), [space4])
    _check_results(repo.list(filters={'size__eq': 93}), [space4])
    _check_results(repo.list(filters={'size__lt': 60}), [space3])
    _check_results(repo.list(filters={'size__gt': 400}), [space2])


def test_repository_list_with_filters_code(spaces):
    repo = memrepo.MemRepo(spaces)
    _check_results(
        repo.list(filters={'code': '913694c6-435a-4366-ba0d-da5334a611b2'}), [space3])
