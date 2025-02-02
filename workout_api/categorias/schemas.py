from workout_api.contrib.schemas import BaseSchema
from pydantic import Field, UUID4
from typing import Annotated

class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', examples=['Scale'], max_length=10)]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Indentificador da categoria')]