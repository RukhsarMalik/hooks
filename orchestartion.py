import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, handoff
from agents.run import RunConfig
from dotenv import load_dotenv


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
    )

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,)

query_agent = Agent (
    name = "Query Agent",
    instructions= "You are a query agent you always generate an arithematic question it will be an easy question of arithmetic",
    model=model
)

math_query = Runner.run_sync(query_agent, input="Generate an arithematic quetsion", run_config = config)
result1 = math_query.final_output

sol_agent = Agent (
    name = "Sol Agent",
    instructions= "you are a solver agent  You always solve arithematic questions you got a question and give its solution never give question of arithmetic always solve math questions",
    model=model
)

sol_query = Runner.run_sync(sol_agent, input=result1, run_config = config)
result2 = sol_query.final_output

print(result1)
print(result2)