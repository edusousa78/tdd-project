from pydantic import Field
from store1.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    name: str = Field(..., description="Product Name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")
