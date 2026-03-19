from dotenv import load_dotenv
load_dotenv()
from crewai import Crew
from tasks import strategy_task, content_task, sales_script_task, analysis_task

crew = Crew(
    agents=[
        strategy_task.agent,
        content_task.agent,
        sales_script_task.agent,
        analysis_task.agent
    ],
    tasks=[
        strategy_task,
        content_task,
        sales_script_task,
        analysis_task
    ]
)

result = crew.kickoff()

print(result)