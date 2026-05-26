# AI FAQ API

Miniproject that uses openai stores prompts and responses in postgresql database

## Technologies/requirements
- fastapi
- openapi
- postgresql
- one /ask endpoint
- stores prompts, model answers in postgres
- dockerized

## What could be changed in next version:
- proper storage of conversation data with LLM
right now it is in minimalistic version
- improve structure of project
- adding tests
- adding description of methods
- adding ResponseModels

##instalation

```bash
git clone https://github.com/lukas5555510/AI_FAQ_API.git
```
add .env following example:
```
OPENAI_API_KEY=your_openai_api_key
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=ai_faq_db
```
```bash
docker-compose build
```
```bash
docker-compose up
```




