from uuid import uuid4

from fastapi import APIRouter, Body, status

from workout_api.contrib.dependencies import DataBaseDependency
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut


router = APIRouter()

@router.post('/',
             summary='create categoria',
             status_code=status.HTTP_201_CREATED,
             response_model=CategoriaOut,
             )
async def post(db_session: DataBaseDependency,
               categoria_in:CategoriaIn = Body(...)) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())