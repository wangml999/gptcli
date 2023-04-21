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
usage: gptcli [-h] [-c] [-i] text [text ...]

positional arguments:
  text           the question to ask

options:
  -h, --help     show this help message and exit
  -c, --command  type the command directly to the terminal
  -i, --info     get information about the command
```

```bash
$ gptcli -i list all pods with tag abc in namespace xyz
```

```bash
$ gptcli -c Print the last 5 lines of "access.log". &
```