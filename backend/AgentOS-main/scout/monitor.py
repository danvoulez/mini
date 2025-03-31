
import asyncio
import httpx
import sys, os; sys.path.append(os.path.dirname(__file__))
from logger import logger

AGENTS = {
    "api": "http://localhost:8001/status",
    "fine_tuning": "http://localhost:8002/status",
    "memory": "http://localhost:8003/status",
    "orchestrator": "http://localhost:8004/status",
    "tool_proxy": "http://localhost:8005/status",
    "voice": "http://localhost:8006/status",
    "vision": "http://localhost:8007/status",
    "promptos": "http://localhost:8008/status"
}

async def check_agent(name, url):
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            res = await client.get(url)
            if res.status_code == 200:
                logger.info(f"{name.upper()} OK: {res.json()}")
                return (name, "ok", res.json())
            else:
                logger.warning(f"{name.upper()} FAIL: HTTP {res.status_code}")
                return (name, "fail", {"code": res.status_code})
    except Exception as e:
        logger.error(f"{name.upper()} ERROR: {str(e)}")
        return (name, "error", str(e))

async def monitor_all_agents():
    logger.info("Scout is monitoring all agents...")
    results = await asyncio.gather(*(check_agent(name, url) for name, url in AGENTS.items()))
    return results

if __name__ == "__main__":
    asyncio.run(monitor_all_agents())
