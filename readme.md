# 自用简易web服务器备忘录

## 说明

#### 1 使用

通过`run.py`启动服务器。

在`config.py`文件中选择导入模块和设置服务器配置。

#### 2 主模块

`modules`目录存放服务器的若干模块，其中`master`是主模块，必须载入。

在`master/config.py`中修改变量`LOGIN_REQUIRED = False`关闭**登录验证**。

主模块无ajax。

#### 3 模块

参考`media/__init__.py`，每个分模块都需要把部分模块信息加载入列表`active_modules`。

服务器开启时，需要根据`active_modules`中的模块信息生成网站主页。

每个模块需要有一个模块主页，网站主页仅仅是一个入口，能够索引到所有的模块主页。模块其他子页面的索引均由模块自治。