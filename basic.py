# 远程接入服务器
ssh root@129.186.0.232

# 查看进程
top
top之后再按1: 看到每个cpu的运行状态
  
example：
16.3%us, 62.3%sy

us：用户空间占用CPU百分比
sy：系统占用CPU百分比
# 查看当前路径
pwd

# 退出目前的进程
ctrl + z  
q

# 终止当前程序
ctrl + c  

# 进入当前路径下的某个文件夹
cd yoyo

# 查看当前文件夹下的所有文件
ls

# 用python运行当前路径下的某个文件
python3 main.py

# 进入python
python3

# 退出
exit（）

# 用指定CPU运行程序
taskset -pc 1 5662: 指定CPU 1
taskset -pc 0-3 5662：指定CPU 0-3

# 查看pid为5662的程序使用的CPU是哪个或者哪些
taskset -p 5662

