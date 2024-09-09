# FROM python:3.11.9-alpine3.20      너무 가벼워서  git이 안됨
FROM python:3.11.9

WORKDIR app/

COPY .  app/

RUN pip install --upgrade pip
RUN pip install git+https://github.com/Mingk42/fishRegression.git@v0.5.0/api_merge

CMD ["uvicorn", "fishregression.main:app", "--host", "0.0.0.0", "--port", "8080"]
