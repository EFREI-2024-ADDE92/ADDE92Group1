FROM python:3.8-slim-buster

WORKDIR /app

COPY . ./

RUN pip3 install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]