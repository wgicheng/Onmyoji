# Onmyoji
本项目是基于阴阳师妖怪屋的探索玩法编写的。
目的是让使用者能够快速根据拥有的式神，组合出能让增强buff最大化的8人组合。
探索玩法可派遣8位式神进行不断探索。
不同式神可组成不同羁绊，羁绊在游戏中是固定的，式神组成羁绊可获得增强buff，即额外探索奖励。

本项目使用方法，只需规范输入内容，并进行分隔，在完成输入后以N或n结尾即可。
该项目结果只会出现第一个增强buff最大的组合，请知悉。

本项目计算过程：
1.获取使用者的式神录，进行处理后获得单个式神的集合，保存至使用者变量type中。
2.根据这些式神从式神字典中找到可以组成的羁绊，保存其在字典中位置至使用者变量loc中。
3.将不同羁绊可组成的组合(后续称为羁绊组合)，占用人数，增强buff放在一个字典中，保存至使用者变量total中。
4.对total中每个可组成羁绊组合，进行对比，占用人数合规(8位)，且增强等级最大的组合保存至best中，并输出。
