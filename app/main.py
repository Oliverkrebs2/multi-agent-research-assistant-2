from fastapi import FastAPI

from app.agents import run_research_pipeline

app = FastAPI(title="Multi-Agent Research Assistant")


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "multi-agent-research-assistant"}


@app.post("/research/run")
def run_research():
    return run_research_pipeline(
        "What are the key trends in AI-assisted software development?"
    )
