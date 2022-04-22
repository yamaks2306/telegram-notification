FROM python:3.10-slim
COPY . /
RUN python -m pip install requests
ENTRYPOINT ["/entrypoint.sh"]
