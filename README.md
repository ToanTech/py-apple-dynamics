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
- 讨论论坛（机器狗工坊）：http://www.leggedrobot.cn/forum.php?mod=forumdisplay&fid=44

## 4 Py-Apple Dynamics 项目搭建方法

- 第一步：访问 [Py-Apple Structure Github](https://github.com/ToanTech/py-apple-structure)，选择并根据里面指导打印并配齐机械结构和零件
- 第二步：访问 [Py-Apple Controller Github](https://github.com/ToanTech/py-apple-controller),选择并根据里面指导制造主控板
- 第三步：根据 [此处指导](guidetoinstall.md) 安装好四足机器人全部硬件
- 第四步：下载 Github中   Py Apple Dynamics V6.5(最新版)   文件夹中的文件
- 第五步：根据[此处教程](https://www.bilibili.com/video/BV1b5411L7ks?p=6)烧录四足机器人控制程序
- 第六步：根据
- [舵机标定教程](https://www.bilibili.com/video/BV1b5411L7ks?p=10)、[重心标定和踏步效果调试](https://www.bilibili.com/video/BV1b5411L7ks?p=11)、[小跑和慢性步态效果调试](https://www.bilibili.com/video/BV1b5411L7ks?p=12)调试及标定四足机器人
- 第七步：根据[此处教程](https://www.bilibili.com/video/BV1b5411L7ks?p=13)遥控四足机器人，完成四足机器人配置
- **更进一步...如需二次开发**，访问[Py-Apple Dynamics 二次开发教程](https://www.bilibili.com/video/BV1Ut4y1D7s2/)

## 5 **Py-Apple Dynamics** 贡献者

- [核心代码贡献者](contributors_m.md)
- [短期部分功能贡献者](contributors_s.md)
- [WIKI或者资料贡献者](contributors_w.md)

## 6 如何参与到 Py-Apple Dynamics 开源项目开发团队中

-  Py-Apple Dynamics 项目是开源的，我们鼓励参与和贡献代码：[点击查看如何在Py-Apple Dynamics Github 仓库中贡献的指导](http://www.leggedrobot.cn/forum.php?mod=viewthread&tid=49&extra=page%3D1)
-  需要的功能设想和bug可以发布到 Issue list [点击进入 ISSUE LIST](https://github.com/ToanTech/py-apple-dynamics/issues)
-  参与完善项目文字资料和使用教程：[点击查看如何参与完善项目资料（此贴中的二楼）](http://www.leggedrobot.cn/forum.php?mod=viewthread&tid=49&extra=page%3D1)
-  有其他参与问题需要联系项目管理及贡献者 ：[点击查看联系方式](contributors_m.md)
-  菠萝狗开源四足机器人项目开发者交流QQ群：<u>**960502665**</u>

## 7 开源协议

**Py-Apple Dynamics** 项目采用 Apache 许可证，版本 2.0

[点击查看完整协议文档](LICENSE)

## 8 当前 Py-Apple Dynamics 实现的功能

目前的最新的版本是 **Py-Apple Dynamics V6.8 请在  Py Apple Dynamics V6.8(最新版)  文件夹中下载，最新开源代码存放于根目录下，可自由下载。**古早版本 文件夹中存放着之前的老版本代码, 包括早期测试用的 Arduino 版本、基于 Stm32 F4的 Pyboard 版本、以及早期外围程序（地面站、红外遥控）等等。

| 运动性能                     | 遥控功能       | 平衡性能         | 二次开发接口       | AI 功能          |
| ---------------------------- | -------------- | ---------------- | ------------------ | ---------------- |
| 8DOF 运动学逆解              | 航模遥控器控制 | 静态自稳         | 串口通讯接口       | 巡线程序         |
| VMC算法                      | 网页在线遥控   | WALK步态动态自稳 | 少儿图形化积木编程 | 颜色识别跟踪程序 |
| 空间连杆角度补偿             | 网页在线调参   | 摔倒自恢复       |                    |                  |
| 俯仰、滚转姿态控制           |                |                  |                    |                  |
| 高度控制                     |                |                  |                    |                  |
| 支持自行调节机械结构尺寸参数 |                |                  |                    |                  |

**Py-Apple Dynamics V6.8 相对于上个版本增加的功能 2021/8/17**

1. 网页遥控引入虚拟摇杆，增加控制灵活性和精确性

   ![image1](/pic/6.8index.png)

2. 增加陀螺仪自动校准功能，无需安装陀螺仪时机械校准

3. 一些小的bug fixed.