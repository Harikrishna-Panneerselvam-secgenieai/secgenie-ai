#!/usr/bin/env python3
"""
SecGenie.ai Enterprise Project Scaffolding

Usage:
    python3 scripts/scaffold.py

Creates the complete project folder structure and placeholder files.
Safe to run multiple times.
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    # ==========================
    # APP
    # ==========================
    "app",
    # API
    "app/api",
    "app/api/v1",
    "app/api/v1/auth",
    "app/api/v1/users",
    "app/api/v1/investigations",
    "app/api/v1/assets",
    "app/api/v1/findings",
    "app/api/v1/reports",
    "app/api/v1/health",
    "app/api/v1/admin",
    "app/api/dependencies",
    "app/api/routers",
    "app/api/errors",
    # Agents
    "app/agents",
    "app/agents/base",
    "app/agents/planner",
    "app/agents/orchestrator",
    "app/agents/workflow",
    "app/agents/asset",
    "app/agents/log_analysis",
    "app/agents/threat_intelligence",
    "app/agents/mitre",
    "app/agents/cve",
    "app/agents/risk",
    "app/agents/recommendation",
    "app/agents/report",
    "app/agents/memory",
    "app/agents/validator",
    # Core
    "app/core",
    "app/core/config",
    "app/core/logging",
    "app/core/exceptions",
    "app/core/cache",
    "app/core/constants",
    "app/core/security",
    "app/core/dependencies",
    "app/core/telemetry",
    # Database
    "app/database",
    "app/database/models",
    "app/database/repositories",
    "app/database/session",
    "app/database/migrations",
    "app/database/seed",
    "app/database/factories",
    # Domain
    "app/domain",
    "app/domain/investigation",
    "app/domain/investigation/entities",
    "app/domain/investigation/services",
    "app/domain/investigation/repositories",
    "app/domain/investigation/value_objects",
    "app/domain/investigation/events",
    "app/domain/investigation/exceptions",
    "app/domain/asset",
    "app/domain/asset/entities",
    "app/domain/asset/services",
    "app/domain/asset/repositories",
    "app/domain/asset/value_objects",
    "app/domain/asset/events",
    "app/domain/asset/exceptions",
    "app/domain/finding",
    "app/domain/finding/entities",
    "app/domain/finding/services",
    "app/domain/finding/repositories",
    "app/domain/finding/value_objects",
    "app/domain/finding/events",
    "app/domain/finding/exceptions",
    "app/domain/report",
    "app/domain/report/entities",
    "app/domain/report/services",
    "app/domain/report/repositories",
    "app/domain/report/value_objects",
    "app/domain/report/events",
    "app/domain/report/exceptions",
    "app/domain/user",
    "app/domain/user/entities",
    "app/domain/user/services",
    "app/domain/user/repositories",
    "app/domain/user/value_objects",
    "app/domain/user/events",
    "app/domain/user/exceptions",
    "app/domain/risk",
    "app/domain/risk/entities",
    "app/domain/risk/services",
    "app/domain/risk/repositories",
    "app/domain/risk/value_objects",
    "app/domain/risk/events",
    "app/domain/risk/exceptions",
    # Services
    "app/services",
    "app/services/investigation",
    "app/services/asset",
    "app/services/report",
    "app/services/auth",
    "app/services/workflow",
    "app/services/notification",
    # Workflow
    "app/workflow",
    "app/workflow/engine",
    "app/workflow/executor",
    "app/workflow/scheduler",
    "app/workflow/graph",
    "app/workflow/queue",
    "app/workflow/retry",
    "app/workflow/state",
    "app/workflow/events",
    # Providers
    "app/providers",
    "app/providers/openai",
    "app/providers/anthropic",
    "app/providers/gemini",
    "app/providers/ollama",
    "app/providers/azure_openai",
    # Integrations
    "app/integrations",
    "app/integrations/tenable",
    "app/integrations/openvas",
    "app/integrations/splunk",
    "app/integrations/elastic",
    "app/integrations/sentinel",
    "app/integrations/crowdstrike",
    "app/integrations/jira",
    "app/integrations/servicenow",
    "app/integrations/slack",
    "app/integrations/email",
    # Shared
    "app/schemas",
    "app/models",
    "app/middleware",
    "app/security",
    "app/events",
    "app/utils",
    "app/prompts",
    # ==========================
    # DOCS
    # ==========================
    "docs",
    "docs/architecture",
    "docs/api",
    "docs/database",
    "docs/deployment",
    "docs/development",
    "docs/workflows",
    "docs/diagrams",
    "docs/prompts",
    "docs/standards",
    # ==========================
    # TESTS
    # ==========================
    "tests",
    "tests/unit",
    "tests/integration",
    "tests/api",
    "tests/agents",
    "tests/database",
    "tests/workflow",
    "tests/security",
    "tests/performance",
    "tests/e2e",
    # ==========================
    # DEPLOYMENT
    # ==========================
    "deployment",
    "deployment/docker",
    "deployment/kubernetes",
    "deployment/terraform",
    "deployment/github_actions",
    "deployment/monitoring",
    # ==========================
    # ROOT SUPPORT
    # ==========================
    "scripts",
    "data",
    "data/samples",
    "data/fixtures",
    "data/uploads",
    "data/exports",
    "logs",
    "logs/api",
    "logs/agents",
    "logs/workflow",
    "logs/scheduler",
    "tmp",
]

FILES = [
    ".env",
    ".env.example",
    ".gitignore",
    "README.md",
    "LICENSE",
    "Dockerfile",
    "docker-compose.yml",
    "Makefile",
    "pyproject.toml",
    "alembic.ini",
]

created_dirs = 0
created_files = 0

print("=" * 60)
print("Creating SecGenie.ai Enterprise Structure")
print("=" * 60)

for directory in DIRECTORIES:
    path = ROOT / directory
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        created_dirs += 1

    if "migrations" not in directory:
        init_file = path / "__init__.py"
        if not init_file.exists():
            init_file.touch()

for file in FILES:
    path = ROOT / file
    if not path.exists():
        path.touch()
        created_files += 1

print()
print("=" * 60)
print("Project scaffolding completed.")
print(f"Directories created : {created_dirs}")
print(f"Files created       : {created_files}")
print("=" * 60)
