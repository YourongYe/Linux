# 查询当前系统用户设置了哪些执行任务
crontab -l

# 清空当前系统用户设置的所有任务
crontab -r

# 创建 crontab 文件的最简单方法
root 身份登录到命令行
输入 crontab -e
按下 a 键进入到编辑模式
输入 0 */1 * * * /home/work/start-service.sh
同时按下 ctrl+c 退出编辑模式
按下 shift+: 输入 wq 退出 crontab
  
# 如果执行遇到问题，系统会自动发邮件给用户；终端会显示‘You have new mail’
# 邮件信息存在 /var/mail/YoYo 路径下
# 在Finder里找到Macintosh HD 并 按组合键：cmd + shift + '>', 即可找到文件并删除

SHELL=/bin/bash 
PATH=/sbin:/bin:/usr/sbin:/usr/bin 
MAILTO=root
*/2 * * * * root python /Users/YoYo/Desktop/Intelligent_Invest/program/AutoHTML.py
*/2 * * * * /anaconda3/bin/python.exe /Users/YoYo/Desktop/Intelligent_Invest/program/AutoHTML.py
# 编辑器改为nano
export EDITOR=/usr/bin/nano
