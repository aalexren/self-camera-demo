from logging import getLogger

import fastapi
import uvicorn
from fastapi import FastAPI

from app.endpoints import route_list
from app.config.default import DefaultSettings
from app.config.utils import get_settings

logger = getLogger(__name__)

def bind_routes(application: FastAPI, settings: DefaultSettings) -> None:
    for route in route_list:
        application.include_router(route, prefix=settings.PATH_PREFIX)

def get_app() -> FastAPI:
    application = fastapi.FastAPI(
        title="Camera Service",
        docs_url="/swagger",
        openapi_url="/openapi",
    )
    
    settings = get_settings()
    bind_routes(application, settings)
    application.state.settings = settings

    return application

app = get_app()

# can't find module app
# https://github.com/tiangolo/fastapi/issues/2582#issuecomment-752845856

if __name__ == "__main__":
    uvicorn.run(
        "app.__main__:app",
        host="0.0.0.0",
        port=80,
        reload=True,
        reload_dirs=["app"],
        log_level="debug"
    )