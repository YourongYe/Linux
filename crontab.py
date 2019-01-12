# 查询当前系统用户设置了哪些执行任务
crontab -l

# 清空当前系统用户设置的所有任务
crontab -r

# 创建 crontab 文件的最简单方法
输入 crontab -e
按下 a或者i 键进入到编辑模式
按下 ctrl+c 退出编辑模式
按下 shift+: 输入 wq 退出 crontab
  
# 如果执行遇到问题，系统会自动发邮件给用户；终端会显示‘You have new mail’
# 邮件信息存在 /var/mail/YoYo 路径下
# 在Finder里找到Macintosh HD 并 按组合键：cmd + shift + '>', 即可找到隐藏文件并删除


PATH=/anaconda3/bin # 指定了python3的位置
35 17 * * * python3 /Users/YoYo/Desktop/Intelligent_Invest/program/AutoHTML.py # 每天下午5点35执行
*/2 * * * * python3 /Users/YoYo/Desktop/Intelligent_Invest/program/AutoHTML.py # 每隔两个分钟执行一次
0 0 * * 2-6 python3 /Users/YoYo/Desktop/Intelligent_Invest/program/AutoHTML.py # 每周二到周六midnight执行


# 编辑器改为nano或者vim
export EDITOR=/usr/bin/nano
export EDITOR=/usr/bin/vim


