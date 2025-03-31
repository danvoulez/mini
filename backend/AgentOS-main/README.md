
# AgentOS - Microcity of Autonomous Agents

AgentOS is a modular, multi-agent operating system designed for real-world execution of tasks across sales, memory, communication, voice, AI reasoning, file systems, and more.  
Built to function like a **city of agents**, each with a defined role, shared memory, and autonomy, the system is powered by OpenAI and inspired by cutting-edge agentic architectures.

---

## 🚀 Overview

AgentOS enables you to:
- Automate operations with modular agents (`scout`, `memory`, `voice`, `tool_proxy`, `vision`, `orchestrator`)
- Monitor and improve itself using the Scout auto-evaluator (LLM-based)
- Generate plugins, agents, workflows, and dashboards from natural language
- Connect to APIs, cloud storage, WhatsApp, Stripe, and more

---

## 🌐 Architecture (Fractal View)

Each service is its own micro-agent:

```
                 [ PromptOS ]
                      |
    +-----------------+-----------------+
    |         |        |        |       |
 [API]   [Memory]  [Vision] [Scout] [Voice]
                     |
                [Tool Proxy]
                     |
                [External APIs]
```

---

## 🧠 Core Agents

### `promptos/`
The natural-language interface and reasoning brain of the system. Turns ideas into working modules, triggers workflows, and guides users through installation and automation.

### `scout/`
Self-monitoring agent. Pings all other services, logs failures, and generates markdown health reports using an LLM.

### `memory/`
Handles persistent storage and cache. Connects with MongoDB and other sources to keep long-term memory for the system.

### `vision/`
Web-based vision interface that generates UIs and dashboards dynamically.

### `voice/`
Voice command interpreter and speaker. Integrated with Vox and other agents for full interaction loop.

### `orchestrator/`
Connects, routes, and prioritizes tasks between agents.

### `tool_proxy/`
Responsible for executing tools (browser, Python, uploads, etc.) with safety and rate limiting.

---

## ✅ Status

| Service       | Status       | Tests | Docs |
|---------------|--------------|-------|------|
| promptos      | Ready        | ✅    | ✅   |
| scout         | Active       | ✅    | ✅   |
| vision        | Upgraded     | ✅    | ✅   |
| api           | Minimal      | ✅    | ⬜    |
| memory        | Operational  | ✅    | ⬜    |
| voice         | Functional   | ✅    | ✅   |

---

## 🧪 Tests

All services include `/tests/test_status.py` and pass `pytest`.  
Coverage reports available soon.

---

## 📦 Install & Run

**Local Setup:**

```bash
git clone https://github.com/voulezvous-ai/AgentOS.git
cd AgentOS
pip install -r requirements.txt
uvicorn main:app --reload
```

**Run All Services with PM2 or Docker:**

```bash
pm2 start ecosystem.config.js
# or
docker-compose up --build
```

---

## 🌍 Deployment

Supports deploy on:
- Railway
- Vercel (frontend)
- DigitalOcean droplets (with `deploy_to_ocean.py`)

Includes `.env.example`, `Dockerfile`, and GitHub Actions for CI/CD.

---

## 🧠 Scout Sample Output

```markdown
# AgentOS Health Report (2025-04-01)
- VISION: OK
- MEMORY: OK
- API: OK
- SCOUT: OK
- VOICE: OK
```

Reports saved in `scout/reports/`.

---

## 🔁 Releases

| Version | Date       | Highlights                          |
|---------|------------|-------------------------------------|
| v1.1.0  | 2025-04-01 | CI/CD, Scout, Modular Frontend      |
| v1.0.0  | 2025-03-26 | Core Agents, PromptOS, Voice, Setup |

---

## 🧠 Philosophy

AgentOS treats software like a city:  
Each agent is a worker. Each memory is a story. Each tool is a hand.  
Your role? Be the mayor.

---

## 🛠 Technologies

- Python 3.11+
- FastAPI
- MongoDB
- React / Vite (frontend)
- Railway, Vercel
- OpenAI / OpenRouter

---

## © License

MIT. Built by VoulezVous with love and LLMs.
