FROM python:3.10

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

WORKDIR /bot
COPY . /bot

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /bot
USER appuser
ENV PYTHONPATH = /app

CMD ["python", "-m", "bot.main"]