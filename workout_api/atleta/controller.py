from uuid import uuid4

from datetime import datetime
from fastapi import APIRouter, Body, status
from sqlalchemy.future import select

from workout_api.categorias.models import CategoriaModel
from workout_api.contrib.dependencies import DataBaseDependency
from workout_api.atleta.schemas import AtletaIn, AtletaOut
from workout_api.atleta.models import AtletaModel


router = APIRouter()

@router.post('/',
             summary='/create atleta',
             status_code=status.HTTP_201_CREATED,
             response_model=AtletaOut)
async def post(db_session: DataBaseDependency,
               atleta_in: AtletaIn = Body(...)) -> AtletaOut:
    
    categoria = (
        await db_session.execute(
            select(CategoriaModel).filter_by(nome=atleta_in.categoria.nome)
        )
    ).scalars().first()
    atleta_out = AtletaOut(
        id=uuid4(),
        created_at=datetime.utcnow(),
        **atleta_in.model_dump(),
        )
    
    # atleta_model = AtletaModel(**atleta_out.model_dump())
    atleta_model = AtletaModel(
        id=atleta_out.id,
        created_at=atleta_out.created_at,
        nome=atleta_out.nome,
        idade=atleta_out.idade,
        categoria_id=categoria.id  # Use o ID da categoria
    )
    
    db_session.add(atleta_model)
    await db_session.commit()
    
    
    return atleta_out