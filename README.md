# AI Agents Learning

A hands-on path to learning how AI agents work, built layer by layer, from a hand-written agent loop up to an evaluated, production-style agent.

## Stages

| Stage | What I build | What I learn | Status |
|---|---|---|---|
| [1. From scratch](stage-1-from-scratch/) | A ~100-line agent using only the raw Claude API, with 2–3 simple tools | The agent loop, tool calls, why tool descriptions matter | 🟡 In progress |
| 2. Real tools | My own MCP server exposing a real data source | How agents connect to real systems (MCP) | ⚪ To do |
| 3. Flagship project | An agent built with the Claude Agent SDK (subagents, permissions, context management) | Architecture decisions and trade-offs | ⚪ To do |
| 4. Make it credible | An eval suite, failure analysis, demo video | Measuring and improving agent quality | ⚪ To do |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install anthropic python-dotenv
cp .env.example .env   # then put your API key in .env
```

## Core idea

An agent is a loop:

1. Give the model a goal and a list of tools.
2. The model either answers, or asks to use a tool.
3. My code runs the tool and sends the result back.
4. Repeat until it's done.
