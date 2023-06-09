import fastapi
from fastapi import Depends
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from app.db.connection import get_session
from app.db.models import CameraStorage
from app.schemas import GetCameraListResponse, GetCameraListBase
from app.utils import validate_pat

api_router = fastapi.APIRouter()

@api_router.get(
    "/get_camera_list",
    response_model=GetCameraListResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Authentication is required to perform this action!"
        },
    },
)
async def get_camera_list(
    session: AsyncSession = Depends(get_session),
    auth_token: dict = Depends(validate_pat),
):
    if not auth_token["active"]:
        raise fastapi.HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    query = (
        sa.select(CameraStorage)
    )

    camera_orm_list = await session.scalars(query)

    camera_list = [
        GetCameraListBase.from_orm(camera) for camera in camera_orm_list
    ]

    return GetCameraListResponse(cameras=camera_list)