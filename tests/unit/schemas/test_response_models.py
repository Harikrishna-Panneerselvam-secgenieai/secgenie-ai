from app.schemas.responses import SuccessResponse


def test_success_response():

    response = SuccessResponse(
        data={"id": "123"}
    )

    assert response.success is True
    assert response.data["id"] == "123"
    assert response.metadata.timestamp is not None