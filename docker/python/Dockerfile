FROM python:3.11

WORKDIR /src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
#CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
#CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]