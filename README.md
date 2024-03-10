## Getting started 

### Setting environment

Installed [Pytesseract-ocr](https://github.com/tesseract-ocr/tesseract) required

```shell
python3 -r requirements.txt

cp .env.example .env
```

create folder structure
```
root
|
| -- static -- uploads
|
```

### Running project

```shell
python3 -m flask --app web run --debug
```