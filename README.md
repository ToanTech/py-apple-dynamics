# **Py-Apple Dynamics** 全开源四足机器人通用控制软件
## 1 简介

  **菠萝动力开源四足控制软件（Py-Apple Dynamics ）**，集成了开发四足机器人所需要必须基础库，是一套完整的四足机器人控制软件程序。

  软件涵盖了从**步态、运动学、陀螺仪、姿态控制、WIFI遥控等和四足机器人控制相关的方方面面**。并且库文件全部开源，可以直接学习/移植代码。可移植性强，支持多种主控，包括ESP32、STM32、PYBOARD、K210等。

## 2 **菠萝开源四足机器人项目的组成**

  您现在浏览的是[**菠萝开源四足机器人项目**](https://github.com/ToanTech/py-apple-quadruped-robot)的其中一个分项目的 Github **菠萝动力开源四足控制软件（Py-Apple Dynamics ）**。**菠萝开源四足机器人项目**，是一个大型全套四足机器人开源项目。主要由三个分项目构成：

- Py-Apple Dynamics 系列 开源四足控制软件（即本项目）
- [Py-Apple Controller 系列 开源四足万能控制器](https://github.com/ToanTech/py-apple-controller)
- [Py-Apple Structure 系列 开源四足机械结构](https://github.com/ToanTech/py-apple-structure)

## 3 用户支持和讨论论坛

- 用户支持QQ群（桌面级四足机器狗交流群 PY PY DOG）：**1071643412**
- 讨论论坛（机器狗工坊）：http://www.leggedrobot.cn/forum.php?mod=forumdisplay&fid=44

## 4 **Py-Apple Dynamics **项目搭建方法

- 第一步：访问 [Py-Apple Structure Github](https://github.com/ToanTech/py-apple-structure)，选择并根据里面指导打印并配齐机械结构和零件
- 第二步：访问 [Py-Apple Controller Github](https://github.com/ToanTech/py-apple-controller),选择并根据里面指导制造主控板
- 第三步：根据 [此处指导](guidetoinstall.md) 安装好四足机器人全部硬件
- 第四步：下载 Github中<u>Py Apple Dynamics V4.0(最新版)</u>文件夹中的文件
- 第五步：根据[此处教程](https://www.bilibili.com/video/BV1mv411B7dR/)烧录四足机器人控制程序
- 第六步：根据[此处教程](https://www.bilibili.com/video/BV1Qg4y1v78G/)遥控使用四足机器人

## 5 开源开发信息

- Py-Apple Dynamics Github仓库：https://github.com/ToanTech/py-apple-dynamics
- [Py-Apple Dynamics 二次开发教程](http://www.leggedrobot.cn/forum.php?mod=viewthread&tid=48)
- 菠萝狗开源四足机器人项目开发者交流QQ群：<u>**960502665**</u>

## 6 **Py-Apple Dynamics** 贡献者

- [核心代码贡献者](contributors_m.md)
- [短期部分功能贡献者](contributors_s.md)
- [WIKI或者资料贡献者](contributors_w.md)

## 7 如何参与到 Py-Apple Dynamics 开源项目开发团队中

-  Py-Apple Dynamics 项目是开源的，我们鼓励参与和贡献代码：[点击查看如何在Py-Apple Dynamics Github 仓库中贡献的指导](http://www.leggedrobot.cn/forum.php?mod=viewthread&tid=49&extra=page%3D1)
-  需要的功能设想和bug可以发布到 Issue list [点击进入 ISSUE LIST](https://github.com/ToanTech/py-apple-dynamics/issues)
-  参与完善项目文字资料和使用教程：[点击查看如何参与完善项目资料（此贴中的二楼）](http://www.leggedrobot.cn/forum.php?mod=viewthread&tid=49&extra=page%3D1)
-  有其他参与问题需要联系项目管理及贡献者 ：[点击查看联系方式](contributors_m.md)

## 8 开源协议

**Py-Apple Dynamics** 项目采用 Apache 许可证，版本 2.0

[点击查看完整协议文档](LICENSE)

## 9 当前 Py-Apple Dynamics 实现的功能

目前的最新的版本是 **Py-Apple Dynamics V4.0** 请在**Py Apple Dynamics V4.0(最新版)**文件夹中下载，最新开源代码存放于根目录下，可自由下载。**”老版本“**文件夹中存放着之前的老版本代码。

1. 运动学逆解
2. 踏步
3. 高度调节
4. 前后小跑步态
5. 转弯
6. 自稳定
7. 串联腿控制
8. 并连腿控制
9. 动态运动参数调整
10. WIFI遥控
11. WIFI参数调节