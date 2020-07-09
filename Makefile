
install:
	@npm install
	@pipenv install

deploy:
	@serverless deploy -v

deploy-function-create:
	@serverless deploy function -f create

deploy-function-list:
	@serverless deploy function -f list

remove:
	@serverless remove
