# ML_ImageAnnotation Application

------------------------------------------------------
TEST APPLICATION: *Currently under implementation stage*


## Table of contents:
1. [Installation](#installation)
2. [Requirements](#requirements)
3. [Tools](#tools)

## Installation: 
- __1. Git Clone:__
<pre>-- open terminal --
git clone https://reconext@dev.azure.com/reconext/TallinnSoftware/_git/ML_ImageAnnotation
cd ML_ImageAnnotation</pre>
- __2. Run virtual environment:__
<pre>-- linux -- 
python3 -m venv env
source env/bin/activate 
-- windows --
python -m venv env
env/Scripts/activate</pre>
- __3. Install packages for frontend:__
<pre>cd ImageAnnotationUI
npm i 
cd.. </pre>
- __4. Backend setup:__
<pre>pip install django
pip install djangorestframework
python -m pip install Pillow
python -m pip install django-cors-headers</pre>
- __5. Migrate the states:__
<pre>-- linux -- python3 manage.py migrate
-- windows -- python manage.py migrate</pre> 
- __6. Deploy frontend:__
<pre>cd ImageAnnotationUI
npm run build
npm run dev
cd..</pre>
- __7. Run backend server:__
<pre> -- linux -- python3 manage.py runserver
-- windows -- python manage.py runserver</pre>
- __8. Admin panel user creation:__
<pre>-- linux -- python3 manage.py createsuperuser
-- windows -- python manage.py createsuperuser
-- visit localhost:8000/admin or http://127.0.0.1:8000/admin --</pre>

## Requirements:
Extension | Version
--- | ---
`asgiref` | 3.5.2
`backports.zoneinfo` | 0.2.1
`Django` | 4.0.6
`django-cors-headers` | 3.13.0
`django-svelte` | 0.1.6
`djangorestframework` | 3.13.1
`Pillow` | 9.2.0
`pytz` | 2022.1
`sqlparse` | 0.4.2
</pre>

## Tools:
- Svelte - frontend part javascript framework 
- Django - server part python framework
- Node JS - for npm package
- Pillow Library - python library for uploading and working with pictures
- Django Cors Headers - package to work with django api
- MongoDB - our required database (would be implemented in future)

