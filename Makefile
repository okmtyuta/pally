format:
	black .

typecheck:
	mypy .

install-requirements:
	pip install -r requirements.txt

update-requirements:
	pip freeze > requirements.txt