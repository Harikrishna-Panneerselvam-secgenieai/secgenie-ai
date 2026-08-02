from app.models.enums.investigation_priority import InvestigationPriority
from app.models.enums.investigation_status import InvestigationStatus
from app.models.investigation import Investigation


def test_investigation_creation():
    investigation = Investigation(
        title="Failed Login Investigation",
        description="Multiple failed login attempts detected",
        status=InvestigationStatus.CREATED,
        priority=InvestigationPriority.HIGH,
        owner_id="user-123",
        investigation_metadata={
            "source": "SIEM",
            "ip": "192.168.1.20",
        },
    )

    assert investigation.title == "Failed Login Investigation"

    assert investigation.status == InvestigationStatus.CREATED

    assert investigation.priority == InvestigationPriority.HIGH

    assert investigation.owner_id == "user-123"

    assert investigation.investigation_metadata["source"] == "SIEM"


def test_investigation_soft_delete():
    investigation = Investigation(title="Test Investigation")

    assert investigation.is_deleted is False

    investigation.soft_delete(deleted_by="admin")

    assert investigation.is_deleted is True
    assert investigation.deleted_by == "admin"


def test_investigation_restore():
    investigation = Investigation(title="Restore Test")

    investigation.soft_delete()

    assert investigation.is_deleted is True

    investigation.restore()

    assert investigation.is_deleted is False
    assert investigation.deleted_at is None
