from crewai import Task
from agents import strategist, content_creator, sales_manager, analyst, sales_agent

client_message = "Клиент ищет красивый светильник для гостиной"

sales_task = Task(
    description=f"Ответь клиенту: {client_message}",
    expected_output="дружелюбный ответ с предложением подходящего светильника",
    agent=sales_agent
)
strategy_task = Task(
    description="Разработать стратегию роста продаж светильников на 3 месяца",
    expected_output="Подробная стратегия продаж, позиционирование бренда и идеи новых коллекций",
    agent=strategist
)

content_task = Task(
    description="Создать 10 идей постов для Instagram магазина светильников",
    expected_output="Список из 10 идей постов с кратким описанием",
    agent=content_creator
)

sales_script_task = Task(
    description="Создать скрипт ответа клиенту, который спрашивает цену светильника",
    expected_output="Готовый текст ответа клиенту с мягким закрытием на покупку",
    agent=sales_manager
)

analysis_task = Task(
    description="Просчитать эффективность скидки 15% на 1 месяц",
    expected_output="Финансовый анализ акции и прогноз роста продаж",
    agent=analyst
)