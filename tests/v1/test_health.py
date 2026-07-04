from langex.core.testing import discover_test, expects

from src.routes.api.v1.health import health_check

@discover_test
def test_health():
  (health_check) @expects ({
    "status": "working",
  })

