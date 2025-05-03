FROM python:3.9-slim
WORKDIR /app
COPY ollama_ui.py .
RUN pip install streamlit requests
CMD ["streamlit", "run", "ollama_ui.py", "--server.port", "8500"]
