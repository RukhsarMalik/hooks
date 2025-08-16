
from agents.lifecycle import RunHooks, AgentHooks

class MyRunHooks(RunHooks):
    async def on_agent_start(self, context, agent):
        print(f"🚀 Agent Start: {agent.name}")

    async def on_agent_end(self, context, agent, output):
        print(f"🏁 Agent End: {agent.name}, Output: {output}")

    async def on_handoff(self, context, from_agent, to_agent):
        print(f"🤝 Handoff: {from_agent.name} ➡ {to_agent.name}")

    async def on_tool_start(self, context, agent, tool):
        print(f"🔧 Tool Start: {tool.name} by {agent.name}")

    async def on_tool_end(self, context, agent, tool, result):
        print(f"✅ Tool End: {tool.name}, Result: {result}")


