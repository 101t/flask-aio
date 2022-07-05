FROM python:3.8-alpine as b

RUN apk --update add bash nano

COPY requirements.txt .

RUN pip install --user -r requirements.txt

# FROM python:3.8-alpine

WORKDIR /app

# COPY --from=b /root/.local /root/.local

# EXPOSE 5000

COPY src/ .

ENV PATH=/root/.local:$PATH

CMD python ./main.py