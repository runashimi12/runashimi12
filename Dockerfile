FROM python:3.9
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . .

#COPY manage.py gunicorn-cfg.py requirements.txt .env ./
#COPY app app
#COPY authentication authentication
#COPY core core
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install -r requirements.txt

#RUN python manage.py makemigrations
RUN python manage.py migrate

#EXPOSE 5005
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]