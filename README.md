# AWS Keys
```
Access key
AKIATT425LKZHOLLPSPH

Secret access key
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
```

# Install CLI AWS
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
/usr/local/bin/aws --version

aws configure

AWS Access Key ID: <твій access key>
AWS Secret Access Key: <твій secret>
Default region name: eu-central-1
Default output format: json

aws s3 ls

apt install python3-pip
pip --version

py -m venv .venv
#python3 -m venv .venv

.venv\Scripts\activate.sh
#source .venv/bin/activate

python.exe -m pip install --upgrade pip
 
pip install “boto3[crt]”
#pip3 install “boto3[crt]”

pip freeze > requirements.txt
#pip3 freeze > requirements.txt

python main.py
python3 main.py
```