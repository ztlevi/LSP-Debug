## Debug by attach using [debugpy](https://github.com/microsoft/debugpy)

```
docker build --tag lsp-python-debug:latest .
docker run --rm -ti -p 5678:5678 -v $PWD:/code lsp-python-debug:latest bash

# Start python process
python3 -m debugpy --listen 0.0.0.0:5678 --wait-for-client app.py

# For pytest, it's hard to use two "-m" flags. So I basically use the second method to listen debugpy
python3 -m pytest test_dummy.py
```

## Debug in vscode

https://code.visualstudio.com/docs/containers/debug-python

```
code .
```

## Debug in Pycharm

Install pytest-pycharm
