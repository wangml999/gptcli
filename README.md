# gptcli

`gptcli` is a command-line tool that converts natural language commands into bash commands, making it easy to interact with your computer. 


### Install
```bash
pip install git+https://github.com/wangml999/gptcli.git
export OPENAI_API_KEY=xxxxxxxxxxx
```

### Uninstall
```bash
pip uninstall gptcli
```

### Usage
```bash
gptcli list all pods with tag abc in namespace xyz &
```

```bash
gptcli Print the last 5 lines of "access.log". &
```