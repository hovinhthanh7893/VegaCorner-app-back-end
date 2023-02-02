## Set up a Virtual Environment with Pipenv

> pip install --user pipenv

(for window)

> py -m pip install pipenv

## Install package

> pipenv install "fastapi"
> pipenv install "uvicorn[standard]"
> pipenv install pydantic

## Run server

> uvicorn main:app --reload
