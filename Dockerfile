FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN python -m pip install requests
ENTRYPOINT ["/app/entrypoint.sh"]
