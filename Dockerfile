
FROM python:3
MAINTAINER xiaoniuhululu
COPY requirements.txt ./
EXPOSE 5000
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
