# AgentRx — One-Click Reliability Audit for AI Agents

Built with IBM Bob at the IBM Bob Hackathon · May 2026

## What it does
AgentRx audits any AI agent endpoint in three dimensions:
- **Structure** (Iron-Thread) — Does the agent return consistent, well-formed output?
- **Behavior** (TestThread) — Does the agent do what it is supposed to do?
- **Compliance** (PolicyThread) — Does the agent stay within defined rules?

Returns a Reliability Score (0-100) with specific failures and recommendations.

## Live Demo
https://agentrx-jmgwrtospmzmc8ka6grwxx.streamlit.app

## How to run locally
pip install streamlit httpx
streamlit run app.py

## Built on the Thread Suite
AgentRx connects to the [Thread Suite](https://github.com/eugene001dayne) — nine open-source AI agent reliability tools built by Eugene Dayne Mawuli (BiteLance).

## IBM Bob
Built using IBM Bob as the AI development partner throughout the hackathon.
