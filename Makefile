
install:
	@npm install
	@pipenv install

deploy:
	@export AWS_PROFILE=sls && export AWS_REGION=us-east-1 && serverless deploy -v

deploy-function-create:
	@serverless deploy function -f create

deploy-function-list:
	@serverless deploy function -f list

deploy-function-deco:
	@serverless deploy function -f deco

remove:
	@serverless remove
