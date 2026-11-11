from rest_framework.routers import SimpleRouter

# --- Example -------------------------------------------------------------------
# router.register("examples", ViewSetExample)              # /examples/ and /examples/{id}/
# path("stats/", APIViewExample.as_view(), name="stats"),  # goes inside urlpatterns
# -------------------------------------------------------------------------------

router = SimpleRouter()

urlpatterns = [
    *router.urls,
]
