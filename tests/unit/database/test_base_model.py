from app.models.investigation import Investigation


def test_investigation_inherits_base_fields():

    columns = Investigation.__table__.columns.keys()

    assert "id" in columns
    assert "created_at" in columns
    assert "updated_at" in columns
    assert "created_by" in columns
    assert "updated_by" in columns
    assert "deleted_at" in columns