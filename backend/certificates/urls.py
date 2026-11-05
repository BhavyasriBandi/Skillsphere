
from django.urls import path

from .views import (
    CertificateListCreateAPIView,
    CertificateDetailAPIView,
)


urlpatterns = [
    path(
        "",
        CertificateListCreateAPIView.as_view(),
        name="certificate-list-create",
    ),
    path(
        "<int:certificate_id>/",
        CertificateDetailAPIView.as_view(),
        name="certificate-detail",
    ),
]
