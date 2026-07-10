FROM python:3.12-slim

WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copia o código do projeto
COPY . .

# Expõe a porta interna do container
EXPOSE 8000

# O comando final sobe o Gunicorn ao invés do runserver
CMD ["gunicorn", "gtreinos.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]