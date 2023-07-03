import io

from fastapi import APIRouter
from fastapi.responses import Response

from app.services.paths import paths

router = APIRouter(
    prefix="/paths",
    tags=["paths"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{method}", response_model=list[paths.CartesianPoint3D])
async def get_path(method: paths.PathMethod, points: int):
    return paths.get_path(method, points)


@router.get("/{method}/preview")
def get_path(method: paths.PathMethod, points: int, index = None):
    image = paths.plot_points(paths.get_path(method, points), index)
    return Response(image, media_type="image/png")

@router.get("/adv/{method}",  response_model=list[paths.CartesianPoint3D])
async def get_adv_path(method: paths.PathMethod, num_points:int, num_rings:int, max_a:int, min_a:int):
        return paths.adv_get_path(method, num_points, num_rings, max_a, min_a)

@router.get("/adv/{method}/preview")
def adv_get_path(method: paths.PathMethod, num_points:int, num_rings:int, max_a:int, min_a:int, index = None):
    image = paths.plot_points(paths.adv_get_path(method,num_points, num_rings, max_a, min_a), index)
    return Response(image, media_type="image/png")