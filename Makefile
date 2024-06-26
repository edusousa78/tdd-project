run:
	@uvicorn store1.main:app --reload

pre-commit-install:
	@poetry run pre-commit install
