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
