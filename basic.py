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

# 新建文件夹(在当前路径下)
mkdir Projects

# 退出目前的进程
ctrl + z  
q

# 终止当前程序
ctrl + c  

# 进入当前路径下的某个文件夹
cd yoyo
cd /Applications/MAMP/COMP0022/

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

# 返回根目录
cd ~

# 返回上一级目录
cd ..

# 返回上2级目录
cd ../..

# 进入某路径
cd /Users/YoYo

# 查找某个文件的路径
which python
which anaconda

# 查找某一目录下文件的内容包含指定字符的文件名
ls alpha2**.csv
ls alpha2*.csv # 两者效果相同

# 强制关掉某个程序
ps -ax  # 查看所有进程
ps -ax | grep Chrome # 查看所有Chrome相关的进程
kill 9355 # 关掉9355这个进程

