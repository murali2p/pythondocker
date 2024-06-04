FROM python
LABEL authors="mohan"
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python","main.py"]