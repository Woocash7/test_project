### test_project

Excel files uploader

## Runing dev server

- Install python3
- (Optional) Run virtualenv
    - Install virtualenv package `pip install virtualenv`
    - Create virtualenv `virtualenv venv`
    - Activate virtualenv:
        - Windows `venv/scripts/activate`
        - Linux `source venv/bin/activate`
- Clone this repository `git clone https://github.com/Woocash7/test_project.git` 
- Change dir to test_project project directory `cd test_project`
- Install dependencies from requirements.txt `pip install -r requirements.txt`
- Migrate `python manage.py migrate`
- (Optional) Load super admin fixtures `python manage.py loaddata credentials_fixtures.yaml`
    > Super user -> email: `admin@test.pl` , password: `test`
- Run dev server at localhost:8000 `python manage.py runserver`
- You can use `sample.xlsx` from this repo to upload file