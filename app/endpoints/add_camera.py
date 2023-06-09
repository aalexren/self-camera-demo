import fastapi
from fastapi import Body, Depends
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from app.db.connection import get_session
from app.db.models import CameraStorage
from app.schemas import AddCameraRequest, AddCameraResponse

from app.utils import validate_pat

api_router = fastapi.APIRouter()

@api_router.post(
    "/add_camera",
    response_model=AddCameraResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Authentication is required to perform this action!"
        },
    },
)
async def add_camera(
    model: AddCameraRequest = Body(..., ),
    session: AsyncSession = Depends(get_session),
    auth_token: dict = Depends(validate_pat)
):
    if not auth_token["active"]:
        raise fastapi.HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    camera_query = (
        sa.select(CameraStorage)
        .where(CameraStorage.serial_number == model.serial_number)
    )
    camera = await session.scalar(camera_query)
    if camera is not None:
        return AddCameraResponse.from_orm(camera)
    
    new_camera = CameraStorage(
        name=model.name,
        owner=model.owner,
        model=model.model,
        serial_number=model.serial_number
    )

    session.add(new_camera)
    await session.commit()
    await session.refresh(new_camera)

    return AddCameraResponse.from_orm(new_camera)