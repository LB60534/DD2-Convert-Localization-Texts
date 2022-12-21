# DD2-Convert-Localization-Texts
Convert Darkest Dungeon 2 text files in localization into csv format for easy query

DD2仍在抢先体验阶段，因此会有频繁的文本更新。这个工具用于自动转换DD2的台词文本到csv格式，方便使用筛选条件方便地查看对应角色或条件的台词内容。

仅包含一个py文件。目前只有处理角色台词的功能，旁白和其他文本暂不包括在内。

没有exe因为打包出来有点大，没经验不知道咋回事哥们

# 使用说明

通过python运行文件后会要求输入目标文本的文件夹路径，通常在安装文件夹下的这个路径内（抢先体验阶段应该统一为Epic游戏安装路径）..\Epic Games\DDIIExperimental\Darkest Dungeon II_Data\StreamingAssets\Localization\Sources

如果想避免反复输入，可以直接把这个exe文件放到上述路径下（和文本txt文件并列）

<img width="527" alt="image" src="https://user-images.githubusercontent.com/115997829/208922372-534f3c7b-b422-4bda-854d-b46bf8755866.png">


第二项要求选择输出模式。如果选择1，会统一输出到同一个Output-barks_act_outs.csv文件内；如果选择1，会分别用Output-原文件名.csv的格式输出到多个csv文件内。默认选择模式1.

<img width="645" alt="image" src="https://user-images.githubusercontent.com/115997829/208919292-4204c620-b8a6-4481-8bab-f2c2f48c09c5.png">

模式1输出文件应如下：
  <img width="177" alt="image" src="https://user-images.githubusercontent.com/115997829/208914219-7d33c97b-a9e7-47d7-9788-578e7a4af3c3.png">
  
文件内容格式如下：
  <img width="596" alt="image" src="https://user-images.githubusercontent.com/115997829/208914454-012c5e0f-f3d1-4ae2-8bd6-75a8659a241c.png">
  
(可自行用excel的筛选功能形成表头的下拉菜单选项)
