# API Documentation

## GET /health

Returns service health status.

## POST /research/run

Runs a mock multi-agent research pipeline.

## Example Response

```json
{
  "query": "What are the key trends in AI-assisted software development?",
  "plan": [],
  "agents": [],
  "final_report": "AI-assisted software development is moving toward agentic workflows.",
  "citations": []
}
