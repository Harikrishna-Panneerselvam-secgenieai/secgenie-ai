# Structured Logging Standard

**Project:** SecGenie.ai  
**Document Version:** 1.0.0  
**Status:** Approved  
**Owner:** Platform Engineering

---

# 1. Purpose

This document defines the standard logging schema used throughout the SecGenie.ai platform.

The objectives of structured logging are:

- Standardize log format across all services.
- Improve debugging and troubleshooting.
- Enable request tracing across distributed components.
- Support centralized log aggregation platforms.
- Improve observability and production monitoring.
- Support auditing and compliance requirements.
- Prepare the platform for distributed tracing (OpenTelemetry).

All application logs **MUST** follow this standard.

---

# 2. Scope

This standard applies to:

- FastAPI application
- API routes
- Middleware
- Services
- Repositories
- AI Agents
- Background workers
- Scheduled jobs
- Database operations
- External API integrations

---

# 3. Log Format

All logs MUST be emitted in JSON format.

Example:

```json
{
  "timestamp": "2026-07-29T10:15:23.125Z",
  "level": "INFO",
  "message": "Planner Agent execution started",
  "logger": "app.agents.planner",
  "module": "planner_agent",
  "function": "execute",
  "line": 128,
  "request_id": "req_9a2fd88b",
  "correlation_id": "inv_5dcab92d",
  "execution_id": "exec_b2d4c91a"
}
```

---

# 4. Required Fields

| Field | Type | Description |
|---------|------|-------------|
| timestamp | ISO-8601 String | UTC timestamp of log creation |
| level | String | Log severity level |
| message | String | Human-readable log message |
| logger | String | Logger name |
| module | String | Python module name |
| function | String | Function name |
| line | Integer | Source code line number |
| request_id | String | Unique HTTP request identifier |
| correlation_id | String | Investigation/workflow identifier |
| execution_id | String | Agent execution identifier |

---

# 5. Optional Fields

| Field | Type | Description |
|---------|------|-------------|
| process | Integer | Operating system process ID |
| thread | String | Thread name |
| hostname | String | Host machine name |
| environment | String | dev, test, staging, production |
| user_id | String | Authenticated user identifier |
| agent_name | String | Name of AI agent |
| investigation_id | String | Investigation UUID |
| duration_ms | Number | Execution duration |
| status | String | Operation status |
| exception | String | Exception type |
| stack_trace | String | Complete traceback |

Optional fields should be included whenever applicable.

---

# 6. Log Levels

The platform uses the following log levels.

| Level | Usage |
|--------|-------|
| DEBUG | Development diagnostics |
| INFO | Normal application events |
| WARNING | Recoverable or unexpected situations |
| ERROR | Operation failed but application continues |
| CRITICAL | Application cannot continue safely |

---

# 7. Identifier Standards

## Request ID

Purpose:

Track a single HTTP request.

Example:

```
req_9a2fd88b
```

Every request entering the FastAPI application receives a unique Request ID.

---

## Correlation ID

Purpose:

Track an entire investigation across multiple services and AI agents.

Example:

```
inv_5dcab92d
```

The Correlation ID must remain the same throughout the complete investigation lifecycle.

---

## Execution ID

Purpose:

Identify an individual execution of an AI agent.

Example:

```
exec_b2d4c91a
```

Each execution receives a new Execution ID.

Retries must generate a new Execution ID while retaining the same Correlation ID.

---

# 8. Naming Conventions

Field names MUST use snake_case.

Correct:

```json
{
  "request_id": "...",
  "execution_id": "...",
  "correlation_id": "..."
}
```

Incorrect:

```json
{
  "RequestId": "...",
  "requestId": "...",
  "Request_ID": "..."
}
```

---

# 9. Timestamp Standard

All timestamps MUST:

- Use UTC
- Follow ISO-8601 format
- Include milliseconds

Example:

```
2026-07-29T10:15:23.125Z
```

---

# 10. Error Logging

Errors must include:

- Error message
- Exception type
- Stack trace
- Correlation ID
- Request ID
- Execution ID (if available)

Example:

```json
{
  "timestamp": "2026-07-29T10:18:11.234Z",
  "level": "ERROR",
  "message": "Database connection failed",
  "exception": "ConnectionError",
  "stack_trace": "...",
  "request_id": "req_9a2fd88b",
  "correlation_id": "inv_5dcab92d",
  "execution_id": "exec_b2d4c91a"
}
```

---

# 11. Best Practices

Developers SHOULD:

- Log meaningful events.
- Use appropriate log levels.
- Include contextual information.
- Keep log messages concise and descriptive.
- Log exceptions with stack traces.

Developers MUST NOT:

- Log passwords.
- Log API keys.
- Log access tokens.
- Log secrets.
- Log sensitive personal information.
- Log database credentials.

---

# 12. Future Compatibility

This logging schema is designed to integrate with:

- Elasticsearch
- Logstash
- Kibana (ELK)
- Grafana Loki
- Splunk
- Datadog
- AWS CloudWatch
- Azure Monitor
- Google Cloud Logging
- OpenTelemetry

No schema changes should be required when integrating with these platforms.

---

# 13. Compliance

All newly developed modules must comply with this logging standard.

Code reviews should verify that:

- JSON logging is used.
- Required fields are present.
- Sensitive information is not logged.
- Appropriate log levels are selected.

---

# 14. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-29 | Initial structured logging standard |