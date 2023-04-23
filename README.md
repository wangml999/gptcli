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
usage: gptcli.py [-h] [-c] [-i] [-m] text [text ...]

positional arguments:
  text            the question to ask

options:
  -h, --help      show this help message and exit
  -c, --command   type the command directly to the terminal
  -i, --info      get the information about the command
  -m, --markdown  show markdown syntax hightlighting
```

### Demo
```bash
$ gptcli -m create a demo busybox pod demo in namespace xyz with label tag=abc
```

```bash
$ gptcli -c show all the pods in namespace xyz with label tag=abc
```

![Alt Text](assets/demo.gif)