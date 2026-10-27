from fastapi import APIRouter, Depends

from app.application.use_cases.health_check import HealthCheck
from app.presentation.dependencies import get_health_check
from app.presentation.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check(
    use_case: HealthCheck = Depends(get_health_check),
) -> HealthResponse:
    return HealthResponse(**use_case.execute())
