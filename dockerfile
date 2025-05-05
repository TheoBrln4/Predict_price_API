FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY app.py .
COPY model_rf.pkl .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py
EXPOSE 8000
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]