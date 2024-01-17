FROM python:3.8-slim-buster

WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]