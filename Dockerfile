FROM python:3.9-slim

# aqui esta la carpeta con los scirpts
WORKDIR /calculatoe

# me ovldie de copiar xd creo que es por la minuscula
COPY . /app

RUN pip install flask

EXPOSE 5000
#este es el puerto

CMD ["python", "app.py"]s