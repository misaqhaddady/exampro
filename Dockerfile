FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8500

CMD ["streamlit", "run", "ollama_ui.py", "--server.port=8500", "--server.address=0.0.0.0"]
