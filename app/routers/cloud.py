from typing import Optional
from fastapi import APIRouter

from app.controllers import projects

router = APIRouter(
    prefix="/cloud",
    tags=["cloud"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_cloud():
    return {}

@router.get("/{project_name}")
async def get_project(project_name: str):
    ...

@router.post("/{project_name}")
async def upload_project(project_name: str):
    ...
