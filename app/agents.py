def run_research_pipeline(query: str):
    return {
        "query": query,
        "plan": [
            "Identify the main research question",
            "Collect relevant information",
            "Check claims against sources",
            "Summarize findings into a structured report",
        ],
        "agents": [
            {
                "name": "Planner Agent",
                "role": "Breaks the research request into clear subtasks.",
            },
            {
                "name": "Research Agent",
                "role": "Collects relevant information and extracts key points.",
            },
            {
                "name": "Fact Checker Agent",
                "role": "Flags weak claims and verifies source consistency.",
            },
            {
                "name": "Summarizer Agent",
                "role": "Produces a clear final research brief.",
            },
        ],
        "final_report": "AI-assisted software development is moving toward agentic workflows, automated code review, test generation, documentation support, and developer productivity tooling.",
        "citations": [
            {"source": "Engineering blog", "confidence": "medium"},
            {"source": "Technical report", "confidence": "medium"},
        ],
    }
