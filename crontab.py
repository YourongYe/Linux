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
