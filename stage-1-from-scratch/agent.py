"""
Stage 1: a minimal AI agent built from scratch with the raw Claude API.

We'll fill this in step by step. Each TODO matches a step in README.md.
"""

import os
from dotenv import load_dotenv
import anthropic

load_dotenv()  # reads ANTHROPIC_API_KEY from .env
client = anthropic.Anthropic()

MODEL = "claude-sonnet-5-5"


# --- Tools -------------------------------------------------------------------
# TODO (step 2): describe the tools the model is allowed to use.
TOOLS = []


# TODO (step 3): the Python functions that actually run each tool.
def run_tool(name, tool_input):
    raise NotImplementedError


# --- The agent loop ----------------------------------------------------------
def run_agent(goal):
    messages = [{"role": "user", "content": goal}]

    # TODO (step 1): send one request to the model and print the reply.

    # TODO (step 4): loop — while the model asks for a tool,
    #   run it, add the result to `messages`, and ask again.


if __name__ == "__main__":
    run_agent("What is 1234 * 5678?")
