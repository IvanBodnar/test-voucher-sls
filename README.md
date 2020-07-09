### Usage

- Add env vars to terminal session  
```bash
export AWS_PROFILE=<profile-name> && export AWS_REGION=<region>
```

- Install  
```bash
make install
```

- Deploy entire project  
```bash
make deploy
```

- Deploy individual function  
```bash
make deploy-function-<function-name>
```

- Destroy created aws stack  
```bash
make remove
```

### API calls

After the deployment serverless will return the created Api-gw url

- create endpoint - creates a code item  
```bash
curl --location --request POST 'https://qh782gawh9.execute-api.us-east-1.amazonaws.com/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "value": "111",
    "brand_id": "aaa"
}'
```

- list endpoint - list the created code items  
```bash
curl --location --request GET 'https://qh782gawh9.execute-api.us-east-1.amazonaws.com/list'
```
