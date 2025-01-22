from workout_api.contrib.schemas import BaseSchema
from pydantic import Field
from typing import Annotated

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', examples=['CT King'], max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', examples=['Rua X, Q02'], max_length=60)] #erro de tipo no examples
    poprietario: Annotated[str, Field(description='Proprietario do centro de treinamento', examples=['Marcos'], max_length=30)]
