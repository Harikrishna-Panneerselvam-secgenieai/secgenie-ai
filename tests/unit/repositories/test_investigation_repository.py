"""
Unit tests for InvestigationRepository.
"""

from datetime import datetime
from unittest.mock import AsyncMock, MagicMock
from uuid import UUID

import pytest

from app.models.enums.investigation_status import (
    InvestigationStatus,
)
from app.models.investigation import Investigation
from app.repositories.investigation import (
    InvestigationRepository,
)


@pytest.fixture
def mock_session() -> AsyncMock:
    """
    Create mocked async database session.
    """

    return AsyncMock()


@pytest.fixture
def repository(
    mock_session: AsyncMock,
) -> InvestigationRepository:
    """
    Create InvestigationRepository instance.
    """

    return InvestigationRepository(
        mock_session,
    )


def test_repository_initialization(
    repository: InvestigationRepository,
) -> None:
    """
    Repository should initialize correctly.
    """

    assert repository.model is Investigation


@pytest.mark.asyncio
async def test_get_by_status(
    repository: InvestigationRepository,
    mock_session: AsyncMock,
) -> None:
    """
    Should query investigations by status.
    """

    mock_result = MagicMock()

    mock_result.scalars.return_value.all.return_value = []

    mock_session.execute.return_value = mock_result

    result = await repository.get_by_status(
        InvestigationStatus.RUNNING,
    )

    assert result == []

    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_get_active(
    repository: InvestigationRepository,
    mock_session: AsyncMock,
) -> None:
    """
    Should return active investigations.
    """

    mock_result = MagicMock()

    mock_result.scalars.return_value.all.return_value = []

    mock_session.execute.return_value = mock_result

    result = await repository.get_active()

    assert result == []

    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_search(
    repository: InvestigationRepository,
    mock_session: AsyncMock,
) -> None:
    """
    Should search investigations.
    """

    mock_result = MagicMock()

    mock_result.scalars.return_value.all.return_value = []

    mock_session.execute.return_value = mock_result

    result = await repository.search(
        "login",
    )

    assert result == []

    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_get_recent(
    repository: InvestigationRepository,
    mock_session: AsyncMock,
) -> None:
    """
    Should return recent investigations.
    """

    mock_result = MagicMock()

    mock_result.scalars.return_value.all.return_value = []

    mock_session.execute.return_value = mock_result

    result = await repository.get_recent()

    assert result == []

    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_get_by_owner(
    repository: InvestigationRepository,
    mock_session: AsyncMock,
) -> None:
    """
    Should return investigations by owner.
    """

    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = []

    mock_session.execute.return_value = mock_result

    result = await repository.get_by_owner(
        UUID("11111111-1111-1111-1111-111111111111"),
    )

    assert result == []

    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_count_by_status(
    repository: InvestigationRepository,
    mock_session: AsyncMock,
) -> None:
    """
    Should count investigations by status.
    """

    mock_result = MagicMock()
    mock_result.scalar_one.return_value = 5

    mock_session.execute.return_value = mock_result

    result = await repository.count_by_status(
        InvestigationStatus.RUNNING,
    )

    assert result == 5

    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_get_statistics(
    repository: InvestigationRepository,
    mock_session: AsyncMock,
) -> None:
    """
    Should return investigation statistics.
    """

    mock_result = MagicMock()

    mock_result.scalar_one.return_value = 10

    mock_session.execute.return_value = mock_result

    result = await repository.get_statistics()

    assert result["total"] == 10

    mock_session.execute.assert_called()


@pytest.mark.asyncio
async def test_get_completed_between(
    repository: InvestigationRepository,
    mock_session: AsyncMock,
) -> None:
    """
    Should return completed investigations
    within date range.
    """

    mock_result = MagicMock()

    mock_result.scalars.return_value.all.return_value = []

    mock_session.execute.return_value = mock_result

    result = await repository.get_completed_between(
        datetime(2026, 1, 1),
        datetime(2026, 2, 1),
    )

    assert result == []

    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_get_stale(
    repository: InvestigationRepository,
    mock_session: AsyncMock,
) -> None:
    """
    Should return stale running investigations.
    """

    mock_result = MagicMock()

    mock_result.scalars.return_value.all.return_value = []

    mock_session.execute.return_value = mock_result

    result = await repository.get_stale()

    assert result == []

    mock_session.execute.assert_called_once()
