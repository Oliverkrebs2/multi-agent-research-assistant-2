# Architecture

## System Flow

1. User submits a research question.
2. Planner Agent breaks the question into subtasks.
3. Research Agent gathers relevant information.
4. Fact Checker Agent reviews claims for consistency.
5. Summarizer Agent produces the final report.
6. Citation layer attaches source references and confidence scores.

## Core Components

- API Gateway
- Agent Orchestrator
- Planner Agent
- Research Agent
- Fact Checker Agent
- Summarizer Agent
- Citation Manager
- Vector Store
