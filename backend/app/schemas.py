from pydantic import BaseModel


class NodeCreate(BaseModel):
    hostname: str
    ip_address: str
    ssh_username: str
    ssh_password: str
    ssh_port: int = 22


class NodeResponse(BaseModel):
    id: int
    hostname: str
    ip_address: str
    ssh_username: str
    ssh_port: int
    status: str

    class Config:
        from_attributes = True


class CommandRequest(BaseModel):
    command: str