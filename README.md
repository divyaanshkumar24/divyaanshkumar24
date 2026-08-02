<p align="center">
  <img src="banner.svg" alt="Divyaansh Kumar Gupta — systems that show their work" width="100%">
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/divyaanshkumargupta/"><img src="https://img.shields.io/badge/LinkedIn-divyaanshkumargupta-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:divyaanshkumargupta24@gmail.com"><img src="https://img.shields.io/badge/Email-divyaanshkumargupta24%40gmail.com-D14836?logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://divyaanshkumargupta.me"><img src="https://img.shields.io/badge/Portfolio-divyaanshkumargupta.me-4f9dff?logo=googlechrome&logoColor=white" alt="Portfolio"></a>
</p>

I build systems that make their own decisions checkable — pipelines with a trace, agents with an
independent verifier, orchestration engines that show every step instead of hiding it behind one
black-box call. That discipline shows up across everything below: a generic agent-orchestration
engine, a RAG pipeline that measures its own hallucination rate, a distributed job scheduler you
can watch execute live, and a couple of financial-systems and applied-AI projects that apply the
same idea to messier, real-world data.

**Currently exploring:**
- Multi-agent pipelines where a *second, independent* pass checks the first agent's work, instead
  of trusting one model's output at face value
- Lightweight orchestration primitives (routing, retries, structured tracing) built as reusable
  infrastructure, not one-off app glue
- Applying that same "inspectable pipeline" discipline to financial-data systems and real-time
  distributed workloads

---

### Agent orchestration & pipelines

| Project | What it does |
|---|---|
| **[stagechain](https://github.com/divyaanshkumar24/stagechain)** | A generic engine for chaining and routing tasks between AI agents or plain callables — triage/routing, retries with backoff, and a structured execution trace. Zero required dependencies in the core engine. |
| **[Regulatory Filing Intelligence Agent](https://github.com/divyaanshkumar24/Regulatory-Filing-Intelligence-Agent)** | A 3-agent RAG pipeline over real SEC filings: retrieval → grounded answer → an *independent* Claude call that checks whether the answer is actually supported by its cited source text, and flags it if not. |
| **[Conductor](https://github.com/divyaanshkumar24/Dc-conductor)** | A distributed job scheduler — jobs get decomposed and bin-packed across a fleet of Docker worker nodes with a Best-Fit-Decreasing algorithm, with execution streamed back live over WebSockets. |
| **[Clearline](https://github.com/divyaanshkumar24/clearline-backend)** | A call-analysis pipeline: transcribe a recording (faster-whisper), identify speakers (pyannote.audio diarization), and generate insights from the conversation — three inspectable stages, not one opaque call. |

### Financial systems & applied AI

| Project | What it does |
|---|---|
| **[TradedataPipeline](https://github.com/divyaanshkumar24/TradedataPipeline)** | A synthetic securities lending/repo trade pipeline — FastAPI REST API, analytics layer, SQLAlchemy (SQLite/Postgres), Docker, CI. All data is synthetic; built to demonstrate the systems design, not real trading. |
| **[Social Pal](https://github.com/divyaanshkumar24/social-autopilot)** | An AI-driven relationship-intelligence dashboard — analyzes messaging patterns, scores relationship health, detects anomalies, and generates actionable recommendations. |

Also shipped: **[Cipher Studio](https://github.com/divyaanshkumar24/Cipher-Studio)** (visual tool for understanding encryption/decryption ciphers) and **[attendease](https://github.com/divyaanshkumar24/attendease)** (Next.js 14 + Supabase attendance calculator).

---

### Tech stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Anthropic%20Claude-D97757?logo=anthropic&logoColor=white" alt="Anthropic Claude">
  <img src="https://img.shields.io/badge/Vector%20Search-Chroma-6A4C93" alt="Chroma vector search">
  <img src="https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white" alt="pytest">
</p>

### Activity

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=divyaanshkumar24&theme=dark&hide_border=true&background=0D1117&stroke=24303C&ring=4F9DFF&fire=34D399&currStreakLabel=E6EDF3" alt="GitHub streak stats" width="48%">
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/divyaanshkumar24/divyaanshkumar24/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/divyaanshkumar24/divyaanshkumar24/output/github-contribution-grid-snake.svg">
    <img alt="A snake animation eating through my GitHub contribution graph" src="https://raw.githubusercontent.com/divyaanshkumar24/divyaanshkumar24/output/github-contribution-grid-snake.svg" width="100%">
  </picture>
  <br>
  <sub><i>Generated by a GitHub Actions workflow in this repo (<code>.github/workflows/snake.yml</code>) — updates automatically every 12 hours.</i></sub>
</p>

<p align="center">
  <sub>Reach out on <a href="https://www.linkedin.com/in/divyaanshkumargupta/">LinkedIn</a>, by <a href="mailto:divyaanshkumargupta24@gmail.com">email</a>, or through <a href="https://divyaanshkumargupta.me">divyaanshkumargupta.me</a>.</sub>
</p>
