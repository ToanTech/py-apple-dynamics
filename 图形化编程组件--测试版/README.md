## 1 图形化编程配置简介

要使用图形化编程

第一步：安装“MPython图形化编程软件”文件夹中的exe,注意选择32位和64位

第二步：到 Python 官网（www.python.org）下载最新 Python3 ，并安装

第三步：完成安装Python 3，并且确认Python已经成功配置到环境变量中后,点击开始>搜索"cmd"，打开命令行

第四步：命令行中输入：pip install adafruit-ampy 安装 adafruit-ampy  自动下载组件

第五步：在 Mpython ”扩展>添加“ 中导入”MPython 图形化编程导入包“ 中的 1.zip

第六步：熟悉 Mpython 基本操作后，即可开始用积木进行图形化编程

第七步：编程完成后，将代码命名为 my_code.py 放到桌面中

第八步：复制 Download_in.bat 到桌面上，右键编辑，将里面的COM口号改成自己机器狗的COM口号

第九步：双击 Download_in.bat  ，将自动下载 my_code.py 到机器狗

第十步：在机器狗 main.py 中添加图形化编程运行线程，代码如下：

```python
def app_2():
  try:
    exec(open('my_code.py').read())
  except:
    print('积木编程代码执行出错，跳过...')

thread.start_new_thread(app_2, ())

```

重启机器狗，机器狗将自动执行图形化编程的代码！！！

*完成首次配置后，只需要每次积木编程后保存为 my_code.py，每次积木编程完毕烧录时连接同一个usb口（保证COM口号一致），再双击 Download_in.bat ，就可以完成程序下载，重启后狗子就能自动运行积木编程中的代码，实现对应的控制效果！！

*图形化编程参考操作视频：https://www.bilibili.com/video/BV1uy4y1C7GK

*此为初版图形化编程，配置操作较为复杂，需要有一定基础的同学耐心配置完成，在配置过程中有任何疑问，欢迎加入开源四足机器人讨论Q群：1071643412 讨论，答疑。

*后面将开发无需配置一键安装式图形化编程，即将开源，敬请期待！！

