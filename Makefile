# from https://lithic.tech/blog/2020-05/makefile-dot-env
ifneq (,$(wildcard ./.env))
    include .env
    export
endif


install:
	poetry install

run:
	poetry run python main.py


.PHONY: install run
