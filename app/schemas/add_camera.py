from pydantic import BaseModel, Field, UUID4

class AddCameraRequest(BaseModel):
    owner: str = Field(..., title="Owner of the camera")
    name: str = Field(..., title="Name of the camera")
    model: str = Field(..., title="Model of the camera")
    serial_number: str = Field(..., title="Serial number of the camera")

class AddCameraResponse(BaseModel):
    id: UUID4

    class Config:
        orm_mode = True