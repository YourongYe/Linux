命令

mkdir 创建目录
mkdir [-p] make directory, recursively make [-p]
rmdir [-p] remove directory(only empty directory)

touch 创建文件
touch [-选项] 文件名
Linux系统文件3个时间：
accesstime atime访问时间（只要被读取）  touch -a 修改访问时间
modifytime mtime 数据修改时间 touch -m touch -m 修改文件修改数据时间
changetime ctime 状态修改时间 touch -c 修改文件时间参数 三个都改 文件不存在不建立文件

ext4文件系统：两大块，小部分一块保存文件的inode信息，一部分保存block信息
inode(i节点)：记录文件权限（w、r、x）、block编号、时间。不记录文件名（文件名记录在文件所在目录的block里）。
block：实际的数据储存

读文件：目录中记录文件名找到inode，再找到block

ln 给文件创建链接
ln [-s/-f(default)] 源文件 目标文件
-s 软链接类似于快捷方式（绝对路径）
-f 硬链接指的就是给一个文件的 inode 分配多个文件名

cp 复制文件／目录 （没看完）
cp -i 是否覆盖
cp -r 复制目录
cp -d 复制软连接文件时，复制的是软链接（不加-d复制源文件）

rm [- ] 文件或目录 删除 永久性删除 破坏性文件或目录
-f:
-i:提示询问（默认）
-r:递归，用于删除子目录和文件
rm -r /test 删除目录，每个子目录都会询问
rm -rf /test 强制删除 整个删除

mv 移动文件或改名 破坏性命令 使用不当出问题
-f: 强制覆盖
-i: 交互移动
-n: 不覆盖
-u: 对比，更新则升级

例子：
Mv info/ logs （移动info文件夹下的所有到logs）

find 查找文件
 . -name 
w 查看登陆用户
