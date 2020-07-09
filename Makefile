SHELL := bash

install:
	@npm install
	@pipenv install

deploy:
	@export AWS_PROFILE=sls && export AWS_REGION=us-east-1
