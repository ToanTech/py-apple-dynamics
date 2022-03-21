# **Py-Apple Dynamics** 全开源四足机器人通用控制软件
## 1 简介

  **菠萝动力开源四足控制软件（Py-Apple Dynamics ）**，集成了开发四足机器人所需要必须基础库，是一套完整的四足机器人控制软件程序。

  软件涵盖了从**步态、运动学、陀螺仪、姿态控制、WIFI遥控等和四足机器人控制相关的方方面面**。并且库文件全部开源，可以直接学习/移植代码。可移植性强，支持多种主控，包括ESP32、STM32、PYBOARD、K210等。

  **喜欢项目的话，请B站一键三连并 Star 项目哦**

## 2 **菠萝开源四足机器人项目的组成**

  您现在浏览的是[**菠萝开源四足机器人项目**](https://github.com/ToanTech/py-apple-quadruped-robot)的其中一个分项目的 Github **菠萝动力开源四足控制软件（Py-Apple Dynamics ）**。**菠萝开源四足机器人项目**，是一个大型全套四足机器人开源项目。主要由三个分项目构成：

- Py-Apple Dynamics 系列 开源四足控制软件（即本项目）
- [Py-Apple Controller 系列 开源四足万能控制器](https://github.com/ToanTech/py-apple-controller)
- [Py-Apple Structure 系列 开源四足机械结构](https://github.com/ToanTech/py-apple-structure)

## 3 用户支持和讨论论坛

- QQ群1（桌面级四足机器狗交流群 PY PY DOG）：**1071643412**
- QQ群2（无刷四足机器狗交流群 PY PY DOG）：**1005923565**

## 4 Py-Apple Dynamics 项目搭建方法

- http://padog.com.cn/ 是本项目的详细文档站，按照此处教程搭建项目，若有问题，请加入 **3 用户支持和讨论论坛** 中的Q群细聊

- TB店铺[灯哥开源](https://shop564514875.taobao.com/)也可找到**全套套件可供采买**

- 项目文件说明：

  | 文件夹名                         | 功能                                                         |
  | -------------------------------- | ------------------------------------------------------------ |
  | Py Apple Dynamics V7.3 SRC       | 菠萝狗7.3版本代码                                            |
  | Py-apple Dynamics Dev Tool(V7.3) | 快速烧录工具，可以利用它直接把ESP32环境一键配置完成并自动烧录菠萝狗代码 |
  | 软件环境                         | UpyCraft编程IDE+控制板串口驱动                               |
  | OpenMV支持                       | OpenMV连接菠萝狗实现图像识别功能的例程                       |
  | 图形化编程组件--测试版           | 菠萝狗的图形化积木编程环境                                   |
  | 古早版本                         | 老版本菠萝狗代码                                             |
  


## 5 **Py-Apple Dynamics** 贡献者

- [核心代码贡献者](contributors_m.md)
- [短期部分功能贡献者](contributors_s.md)
- [WIKI或者资料贡献者](contributors_w.md)

## 6 如何参与到 Py-Apple Dynamics 开源项目开发团队中

-  Py-Apple Dynamics 项目是开源的，我们鼓励参与和贡献代码，希望参与贡献代码的请加入 **3 用户支持和讨论论坛** 中的Q群细聊
-  需要的功能设想和bug可以发布到 Issue list [点击进入 ISSUE LIST](https://github.com/ToanTech/py-apple-dynamics/issues)

## 7 开源协议

**Py-Apple Dynamics** 项目采用 [GPL-3.0 License](https://github.com/ToanTech/Inverted_Pendulum_DengFOC/blob/main/LICENSE)

## 8 当前 Py-Apple Dynamics 实现的功能

目前的最新的版本是  <u>Py-Apple Dynamics V7.3</u> ，最新开源代码存放于根目录下，可自由下载。古早版本 文件夹中存放着之前的老版本代码, 包括早期测试用的 Arduino 版本、基于 Stm32 F4的 Pyboard 版本、以及早期外围程序（地面站、红外遥控）等等。

| 运动性能                     | 控制功能       | 平衡性能         | 二次开发接口       | AI 功能          |
| ---------------------------- | -------------- | ---------------- | ------------------ | ---------------- |
| 8DOF 运动学逆解              | 航模遥控器控制 | 静态自稳         | 串口通讯接口       | 巡线程序         |
| VMC算法                      | 网页在线遥控   | WALK步态动态自稳 | 少儿图形化积木编程 | 颜色识别跟踪程序 |
| 空间连杆角度补偿             | 网页在线调参   |                  |                    |                  |
| 俯仰、滚转姿态控制           | 低电量报警     |                  |                    |                  |
| 高度控制                     | 蜂鸣器提示音   |                  |                    |                  |
| 支持自行调节机械结构尺寸参数 |                |                  |                    |                  |

**Py-Apple Dynamics V7.3 相对于上个版本增加的功能 2021/12/23**

1. 改善浏览器兼容性，解决部分安卓浏览器的卡顿问题
2. 将串口控制和航模遥控功能直接整合进设置界面中，可以从设置界面直接打开，无需二次烧录附加程序
3. 优化在ESP32下的运行速度
4. 支持240MHZ ESP双核模式
5. 增加提示音功能
6. 支持ADC读取电压功能，低电量时自动关断舵机并蜂鸣，保证安全使用
7. 更新步态生成器(padog.py,PA_GAIT.py)，支持摆动腿延伸，作为后面增加足底传感器的基础
8. 一些小的bug fixed.

​     ![image1](/pic/Ver73.png)