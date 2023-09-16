
#
pip3 install -t dependencies -r requirements.txt

(cd dependencies; zip ../aws_lambda_artifact.zip -r .)

zip aws_lambda_artifact.zip -u main.py

aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 865049059586.dkr.ecr.eu-north-1.amazonaws.com

https://zdpzgu3ctnqedk3haxlyrdxvym0qigsb.lambda-url.eu-north-1.on.aws/get_recomendations?age=45&surgery=ileostomy