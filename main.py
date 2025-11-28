from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import sys
import asyncio
import logging
import traceback
from src.memory.memory_bank import Memory_bank
from src.memory.session_service import Sessionservice

# ---------------- DEBUG LOGGER SETUP ----------------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("debug")
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "src"))

from src.orchestrator.orchestrator import orchestrator

app = FastAPI()
orch = orchestrator()
memory=Memory_bank()
templates = Jinja2Templates(directory="templates")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    message: str

class response(BaseModel):
    agent: str
    response: str


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    logger.debug("Serving chat UI")
    return templates.TemplateResponse("chat.html", {"request": request})


@app.post("/chat")
async def chat_endpoint(message: Message):
    logger.debug(f"Received message: {message.message}")

    try:
        loop = asyncio.get_event_loop()

        # determine agent
        agent_type = await loop.run_in_executor(None, orch.router.route, message.message)
        logger.debug(f"Selected Agent: {agent_type}")

        # run agent
        response = await loop.run_in_executor(None, orch.run, message.message)
        logger.debug(f"Agent Response: {response}")

        # memory.save_memory(f"User: {message.message}")
        # memory.save_memory(f"Agent ({agent_type}): {response}")

        return {"agent": agent_type, "response": response}

    except Exception as e:
        logger.error("Error in /chat endpoint")
        logger.error(str(e))
        logger.error(traceback.format_exc())

        return {
            "agent": "system",
            "response": f"⚠ Error occurred: {str(e)}"
        }


@app.get("/agents")
async def get_agents():
    try:
        logger.debug("Fetching list of agents")
        agents_info = [{
            "name": agent_name,
            "description": f"{agent_name.replace('_', ' ').title()} Agent"
        } for agent_name in orch.agents.keys()]

        logger.debug(f"Agents Available: {agents_info}")
        return {"agents": agents_info}

    except Exception as e:
        logger.error("Error fetching agents")
        logger.error(str(e))
        return {"agents": [], "error": str(e)}
    

