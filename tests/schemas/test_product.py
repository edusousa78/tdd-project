from uuid import UUID

from pydantic import ValidationError
import pytest
from store1.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_sucess():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Televisor LG 55 smart 4k"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {"name": "Televisor LG 55 smart 4k", "quantity": 15, "price": 3.600}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Televisor LG 55 smart 4k", "quantity": 15, "price": 3.6},
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }
