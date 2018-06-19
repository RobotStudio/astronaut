import pytest
from unittest import mock

from rentomatic.domain.space import Space
from rentomatic.use_cases import space_use_cases as uc


@pytest.fixture
def domain_spaces():
    space_1 = Space(
        code='f853578c-fc0f-4e65-81b8-566c5dffa35a',
        size=215,
        price=39,
        longitude='-0.09998975',
        latitude='51.75436293',
    )

    space_2 = Space(
        code='fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
        size=405,
        price=66,
        longitude='0.18228006',
        latitude='51.74640997',
    )

    space_3 = Space(
        code='913694c6-435a-4366-ba0d-da5334a611b2',
        size=56,
        price=60,
        longitude='0.27891577',
        latitude='51.45994069',
    )

    space_4 = Space(
        code='eed76e77-55c1-41ce-985d-ca49bf6c0585',
        size=93,
        price=48,
        longitude='0.33894476',
        latitude='51.39916678',
    )

    return [space_1, space_2, space_3, space_4]


def test_space_list_without_parameters(domain_spaces):
    repo = mock.Mock()
    repo.list.return_value = domain_spaces

    space_list_use_case = uc.SpaceListUseCase(repo)
    result = space_list_use_case.execute()

    repo.list.assert_called_with()
    assert result == domain_spaces
