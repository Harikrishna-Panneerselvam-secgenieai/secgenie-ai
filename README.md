# SecGenie.ai

AI-Powered Multi-Agent Cybersecurity Investigation Platform


## Overview

SecGenie.ai is an enterprise-grade AI cybersecurity investigation platform
that uses multiple specialized AI agents to analyze security incidents,
correlate evidence, identify threats, assess risks, and generate automated
security investigation reports.


## Features

- Multi-Agent AI Investigation Framework
- Automated Security Incident Investigation
- Threat Intelligence Analysis
- Vulnerability and CVE Analysis
- MITRE ATT&CK Mapping
- Risk Scoring
- Security Recommendations
- AI Generated Investigation Reports


## Architecture Overview

SecGenie.ai follows a Clean Architecture based Multi-Agent AI design.

High-level flow:

User Request
    |
API Layer
    |
Investigation Service
    |
Workflow Engine
    |
Agent Orchestrator
    |
--------------------------------
|       |       |       |
Asset   Log   Threat   CVE
Agent   Agent Intelligence Agent
--------------------------------
    |
Risk Analysis
    |
Report Generation


## Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy 2.0 Async
- PostgreSQL


### AI Platform

- Large Language Models (LLMs)
- Multi-Agent Architecture
- RAG Pipeline
- Vector Database


### Infrastructure

- Docker
- Redis
- Celery


### Development

- Poetry
- Pytest
- Alembic

## Project Structure

secgenie-ai/

├── app/
│   ├── agents/
│   │   ├── base/
│   │   ├── planner/
│   │   ├── orchestrator/
│   │   ├── threat_intelligence/
│   │
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── tests/
├── docs/
├── scripts/
├── deployment/
├── data/
├── logs/
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md

---

# Installation Guide

## Prerequisites

Before installing SecGenie.ai, ensure the following software is installed:

- Python 3.12+
- Poetry
- PostgreSQL
- Docker
- Docker Compose
- Git

---

# Developer Setup


## Activate Virtual Environment

SecGenie.ai uses Poetry for environment management.

Activate the environment:

```bash
eval $(poetry env activate)


## Clone Repository

```bash
git clone <repository-url>

cd secgenie-ai

---

# Running the Application

## Activate Environment

```bash
eval $(poetry env activate)
