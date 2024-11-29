import pydantic as pydantic

class TodoReq(pydantic.BaseModel):
    title: str
    completed: bool
