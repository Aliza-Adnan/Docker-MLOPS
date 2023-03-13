FROM python:3.8
WORKDIR /salary_training
COPY . .
RUN pip install -r requirements.txt
CMD ["python","salary_training.py"]
