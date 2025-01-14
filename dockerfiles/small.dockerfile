FROM python:3.11-slim

# install python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY requirements_small.txt requirements_small.txt
COPY main_small.py main_small.py
WORKDIR /
RUN pip install -r requirements_small.txt --no-cache-dir

ENTRYPOINT ["python", "-u", "main_small.py"]