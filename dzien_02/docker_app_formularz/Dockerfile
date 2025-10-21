# Użyj oficjalnego obrazu Pythona 3.13
FROM python:3.13-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki
COPY . /app

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Otwórz port 5000
EXPOSE 5000

# Domyślne polecenie (niekonieczne, jeśli jest w docker-compose.yml)
# CMD ["flask", "run", "--host=0.0.0.0"]
