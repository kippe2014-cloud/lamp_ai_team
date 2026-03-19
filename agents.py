from crewai import Agent

strategist = Agent(
    role="Бизнес-стратег магазина светильников",
    goal="Разрабатывать стратегию роста продаж и позиционирование",
    backstory="Эксперт по e-commerce и интерьерному рынку"
)

content_creator = Agent(
    role="Контент-маркетолог",
    goal="Создавать продающий контент для соцсетей",
    backstory="Специалист по Instagram и Reels"
)

sales_manager = Agent(
    role="AI-продажник",
    goal="Закрывать клиентов на покупку и делать апселлы",
    backstory="Опытный менеджер по продажам"
)

analyst = Agent(
    role="Финансовый аналитик",
    goal="Просчитывать маржу и эффективность акций",
    backstory="Эксперт по юнит-экономике"
)

sales_agent = Agent(
    role="Продавец светильников",
    goal="Помогать клиенту выбрать и купить светильник",
    backstory="Ты опытный продавец дизайнерских светильников",
    verbose=True
)