#Script para coletar informações de um bucket da S3 e ordenar os arquivos por nome
#Importante a ordenação no fim pois a API não possui função própria para organizar a lista de arquivos. 

#!/usr/bin/env python3

import boto3
from datetime import datetime,timezone,timedelta

t=datetime.now().astimezone(timezone(timedelta(hours=-3))) #Coletando o momento atual e formatando para o mesmo padrão da S3
passado = t - timedelta(hours=12) #Para este script em específico, preciso de uma janela de arquivos de até 12 horas 

#Necessário definir as credenciais abaixo
AWS_ACCESS_KEY_ID="Chave de acesso aqui"
AWS_SECRET_ACCESS_KEY="Chave secreta aqui"
BUCKET_NAME="Nome do bucket aqui"


session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID, 
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
)

s3 = session.resource('s3')

obj = s3.Bucket(BUCKET_NAME)

for my_bucket_object in obj.objects.all():
    if my_bucket_object.last_modified.strftime("%Y-%m-%d %H:%M:%S") > str(passado):
        if (my_bucket_object.key.find('.mp4') > 0):
            print( my_bucket_object.last_modified.strftime("%Y-%m-%d %H:%M:%S")+ " - " + my_bucket_object.key  )

