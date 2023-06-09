from pydantic import BaseModel, UUID4

class GetCameraListBase(BaseModel):
    id: UUID4
    owner: str
    name: str
    model: str
    serial_number: str

    class Config:
        orm_mode = True

class GetCameraListResponse(BaseModel):
    cameras: list[GetCameraListBase]

    class Config:
        orm_mode = True