from pydantic import BaseModel


class Response(BaseModel):

    name: str
    comment: str
