# Stepic: Automated testing using Selenium and Python

This repo contains the source code for [final task](https://stepik.org/lesson/228249/step/1?unit=200781) of the course.

To run this repo, please use following instructions:

1. Install virtual environmemt:
```
python -m venv venv
```

2. Activate environment:
```shell
source venv/bin/activate
```

3. Install requirements:
```shell
pip install -r requirements.txt
```

4. Download chromedriver to the root folder of the repo

5. Run the programm using the following command:
```shell
pytest -v --tb=line --language=en -m need_review
```
