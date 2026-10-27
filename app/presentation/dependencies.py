from app.application.use_cases.health_check import HealthCheck


def get_health_check() -> HealthCheck:
    return HealthCheck()
