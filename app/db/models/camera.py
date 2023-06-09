from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TEXT, UUID
from sqlalchemy.sql import func

from app.db import DeclarativeBase

class CameraStorage(DeclarativeBase):
    __tablename__ = "camera_storage"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(), # postgres function
        unique=True,
        doc="Unique id of camera in table",
    )

    owner = Column(
        TEXT,
        nullable=False,
        index=True,
        doc="Owner of the camera",
    )

    name = Column(
        TEXT,
        nullable=False,
        index=True,
        doc="Name of the camera, e.g. home-15"
    )

    model = Column(
        TEXT,
        nullable=False,
        index=True,
        doc="Model of the camera"
    )

    serial_number = Column(
        TEXT,
        nullable=False,
        index=True,
        unique=True,
        doc="Serial number of the camera"
    )

    def __repr__(self):
        columns = {}
        for column in self.__table__.columns:
            columns[column.name] = getattr(self, column.name)
        return f"<{self.__tablename__}:" \
                f"{', '.join((f'{x[0]}={x[1]}' for x in columns.items()))}>"