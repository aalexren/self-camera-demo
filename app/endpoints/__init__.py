from app.endpoints.add_camera import api_router as add_camera_router
from app.endpoints.get_camera_list import api_router as get_camera_list_router

route_list = [
    add_camera_router,
    get_camera_list_router,
]

__all__ = [
    "route_list"
]