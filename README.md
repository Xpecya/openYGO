# openYGO - 创建最智障的牌佬(手动狗头)

- 本项目旨在基于深度学习技术，创建一个全自动组牌、打牌的AI。
- 单纯打牌这件事儿其实完全可以通过脚本做出很完善的AI，但是目前全自动组牌技术尚且无法完全基于脚本来进行。
  - 现有的自动组牌技术，我个人推测，恐怕是基于大数据技术，当你为卡组选择了一些牌以后，K社根据系统中同样使用了这些牌的其他玩家的牌组，根据卡片出现概率，从大到小，将高概率出现的牌塞进你的牌组。
  - 这就导致一个问题: 很可能某些现有牌组的构筑实际上进入了一个局部最优解，而非全局最优解之中，某些更优的配置，更出色的combo可能一直没有被人发掘。
    - 正如人工智障修炼过程中常见的情况那样。
- 此外还有一个问题：现有脚本对于手坑/陷阱等康的使用时机，实际上并不清楚。人类玩家可以轻易通过骗康手段骗出AI的康，这使得AI的牌技一直无法更进一步。
  - 这个问题理论上可以由更完备的脚本来解决，脚本针对当前环境各个主流牌组的构筑，分别配置交康点。
  - 但是这个人工工作量实在太大，并且需要长时间的人工介入，每次出新卡/改老卡，就要对应的修改脚本。
  - 我个人认为实际上这是不切实际的做法。
- 另外，在类似的游戏(德扑/桥牌等)中，人工智障的表现一向还不错，这给了作者能够创造一个不那么智障的成果的信心
- 基于上述两点原因，这个本世纪最智障的牌佬就此诞生。
---
- 技术方案: 
  - 智障将在YGOpro上进行无人工干预的自我对战
    - 先让智障一心二用，分别组好牌组，额外，side
    - 然后让智障跟自己完成BO3对战
    - 对战后总结对战数据，优化原本逻辑，然后继续上述流程
  - 为了避免智障坍缩到某个局部最优解，暂定方案如下：
    - 当人工智障A自战对弈一百万盘以后，从0开始再次训练一个新的人工智障B
    - 然后A再与B对弈一百万盘，当AB两者的等级分小于某个阈值(待定)后，保留其中一个作为卷王C留下。
    - 然后再从零开始训练一个新的人工智障D，C再与D对弈一百万盘...
    - 由于每次从零开始时，没有人工预输入的数据，最初智障的组牌逻辑会无限接近于随机搞一个合规的牌组
    - 因此经过足够长时间的内卷以后，最终诞生的卷王会无限接近那个卷王之王。
    - 而此方案的风险，预估为100万这个常量的设置可能并不一定合理，有可能真正的卷王之路仅靠100万盘是走不到头的，这个常量的设置理论上也应该基于某种逻辑来动态的调整，但是暂时没有想到一个合适的方案
    - 此外，每次从0开始训练100万盘，很可能前50万盘，甚至前90万盘，都在进行一个非常低水平的对弈，因此如何在不抹杀智障多样性的前提下，给牌佬输入一些必要的前提数据，让他更快速的进入一个相对高水平的自战对弈状态，这也是一个很伤脑筋的问题，暂时没有解决方案。
    - 另外，YGOpro尽管已经十分完善，但是偶尔还是会出现一些处理上与OCG不同的情况出现。
    - 由于程序的打牌逻辑完全由YGOpro负责，因此严格来说，本人工智障并不是一个OCG/TCG玩家，而是一个100%纯粹YGOpro玩家。
    - 本项目并不打算考虑YGOpro的bug对程序的影响，不过如果YGOpro有更新，本项目会第一时间跟进，永远以最新版本YGOpro为准。
---
- 更新计划: todo
---
- 目前进度: 
  - 创建代码仓库（已完成）
  - 完成全局配置（已完成）
  - 启动YGOpro进程(未开始)
