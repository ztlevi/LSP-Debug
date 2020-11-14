## Debug by attach

```
docker build --tag lsp-python-debug:latest .
docker run --rm -ti -p 5678:5678 lsp-python-debug:latest python3 app.py
```

## Debug in vscode

https://code.visualstudio.com/docs/containers/debug-python

```
code .
```

## Debug in Pycharm

Install pytest-pycharm
