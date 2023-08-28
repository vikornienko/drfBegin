.PHONY: rs
rs:
	python3 manage.py runserver

.PHONY: mm
mm:
	python3 manage.py makemigrations

.PHONY: mig
mig:
	python3 manage.py migrate

.PHONY: csu
csu:
	python3 manage.py createsuperuser
