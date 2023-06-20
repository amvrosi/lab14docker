# obraz bazowy
FROM python:3.9-slim AS base

# zaleznosci
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS builder
WORKDIR /app
COPY server.py .

# wykorzystanie alpine
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /app/server.py .
COPY --from=base /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# healthcheck
HEALTHCHECK --interval=5m --timeout=3s \
    CMD wget --quiet --tries=1 --spider http://localhost:8888 || exit 1

LABEL author="Ivan Sobol"

# lecimy
CMD ["python", "server.py"]