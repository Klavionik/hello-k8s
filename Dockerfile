FROM python:3.10.5-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY r.txt .
RUN pip install -r r.txt
COPY main.py .
EXPOSE 7777
STOPSIGNAL SIGINT
CMD ["python3", "main.py"]
