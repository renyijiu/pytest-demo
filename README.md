# 介绍

这个项目对 pytest 进行探索测试，主要是对 pytest 对于提取测试用例的方式进行探索。pytest 提供了 plugin 的机制，可以通过
plugin 的方式来扩展 pytest 的功能，这个项目就是通过 plugin 的方式来实现对测试用例的提取。

python 版本为 python 2.7.18

# 项目结构

```bash
├── README.md
├── cal.py
├── conftest.py
├── main.py
├── output
│   ├── collect-format.json
│   ├── custom_log.json
│   ├── json_report.json
│   └── report_log.json
├── plugins
│   ├── __init__.py
│   ├── pytest_collect_formatter.py
│   ├── pytest_custom_plugin.py
│   └── pytest_reportlog.py
├── requirements.txt
├── robot
│   ├── Cal.py
│   ├── Test.robot
│   ├── add.py
│   ├── log.html
│   ├── output.xml
│   └── report.html
└── test
    └── test_cal.py
```

# 项目依赖

针对 python2.7, 目前 pytest 支持的版本是 4.6.x，更高的版本并不支持 python2.7

具体的可以查看 requirements.txt 文件

# 项目运行

### pythonic

```bash
# 可以编写自定义的plugin, 具体查看 plugins/pytest_custom_plugin.py 代码示例，生成自定义的日志

$ python main.py -o output/custom_log.json 
```

具体的接口执行结果可以查看 output/custom_log.json 文件

### pytest

pytest 存在很多类似的插件，但是这些插件基本都不支持 python2.7，所以这里只是简单的介绍一下这些插件的使用方式，具体的业务逻辑支持后续还是需要自己实现

#### pytest_collect_formatter

使用 pytest_collect_formatter 这个插件来提取测试用例,代码是从开源代码复制修改兼容 python2.7 测试,生成 json 格式的测试用例信息

```bash
# 使用 pytest 的方式来运行测试用例

$ python -m pytest --collect-only -q --collect-output-file output/collect-format.json --collect-format json

```

具体的接口可以查看 output/collect-format.json 文件

#### pytest_reportlog

使用 pytest_reportlog 这个插件来提取测试用例,代码是从开源代码复制修改兼容 python2.7 测试,生成 json 格式的测试用例信息

```bash
# 使用 pytest 的方式来运行测试用例

$ python -m pytest --collect-only -q --report-log=output/report_log.json

```        

具体的接口可以查看 output/report_log.json 文件

#### pytest-json-report
https://github.com/numirias/pytest-json-report

这个 pytest_json_report 插件有版本能够支持 python2.7，可以安装进行测试验证

```bash
$ pip install pytest-json-report==1.2.2 

$ python -m pytest --collect-only -q --json-report --json-report-file output/json_report.json
```

# 参考

pytest 提供了 plugin 的机制，可以通过 plugin 的方式来扩展 pytest 的功能，具体的可以参考 pytest
的官方文档 [https://docs.pytest.org/en/4.6.x/writing_plugins.html](https://docs.pytest.org/en/4.6.x/writing_plugins.html)


# Robot framework

robot 目录下增加了 robot 测试框架的使用示例，测试用例可以查看 `Test.robot` 文件，

```bash
$ python -m robot -d robot/ robot/Test.robot  
```

执行的接口可以查看 robot 目录下的 `log.html`、`report.html` 文件
