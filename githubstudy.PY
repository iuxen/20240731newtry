#  创建版本库
# $ mkdir learngit 
# $ cd name
# $ pwd
# $ git init


# 添加文件
# $ git add readme.txt
# $ git commit -m 'wrote a readme file'


# 时光机穿梭
# 文件更改后
# $ git status   #查看状态
# $ git diff readme.txt #查看变化
# $ git add readme.txt 后要 $ git commit -m '提交版本库变更说明' 才算完成


#版本回退
# $ git log  #版本历史
# $ git log -- pretty = oneline   # $ git reset -- hard ****编号前4个或5个能体现区别就能识别 退回
# $ git reset -- hard HEAD^  # 退回到初始版
# $ cat readme.txt  #显示内容
# $ git reflog 注意和 git reflog的区别


# 工作区和暂存区
# 新的文件，没有经过 add  commit -m，状态是untracted
# 文件更改后，没有经过 add,及commit -m 会提醒
# 个人总结，add是提交到暂存区Stage, 执行commit 就可以一次性的提交到分支，一旦提交后，工作区就是干净的


#git 管理的是记录修改，而不是文件本身 
#只有被提交add到暂存区的，才能执行commit提交被识别修改
# $ git diff HEAD -- readme.txt,可以查看工作区和版本库里面最新版本的区别 


#撤销修改
# $ git checkout -- readme.txt ,没有放到暂存，执行就是撤销修改，回到初始版本库
# 已经存放暂存区，又作了修改，执行，则是回到暂存区后的状态
# 执行就是让其回到最近一次 git add 或 git commit


# 删除文件
#删除文件的方式 在文件管理器中直接删除或者在GIT中 用 $ rm test.txt 后用 $ git commit -m 
#删错了的情况下，因为版本库里面还有，$ git check -- test.txt
#手动删除，和 $ git rm  是一样的，其原理和 $ git add 是一样，然后要 $ git commit -m 


#远程仓库
# 先在用户主目录下看有没有 .ssh目录。如有，看有否id_rsa 和 rd_rsa.pub, 如有，直接下一步
# 如没有，打开shell(windows下打开 Git bash),创建ssh key: $ ssh-keygen -t rsa -C 'yourmail@example.com'
#接上，然后一路回车， 由于这个Key也不是用于军事目的，所以也无需设置密码
#接上，如顺利，找到.ssh,里面会有 id_rsa 和 id_rsa.pub,前者是私钥，不可示人，后者公钥则可。
#接上，此为第二步，登入github,打开 account settings  ssh keys 页面
#接上，点 Add SSH Key,填上任意Title, 在Key文本里粘贴 id_rsa.pub 内容，允许添加多个，推送前，必有此步
#接上，github免费托管的仓库，大家都能看到，要是变成私有的，就要交费了。也可以自己动手搭建一个Git服务器，相当简单哈


#添加远程仓库
#本地仓库运行bush, $ git remote add origin git @github.com:***/***.git
#接上 $ git push -u origin master  加了-u,第一次推送，本地分支内容推送到远程，还会建立master关联，以后推送可以简化
# 只要本地作了提交，就可以通过 $ git push origin master
# SSH警告 第一次使用git的clone或push连接Github,会得到一个警告，输入yes即可，
# 接上：输入之前也可对照github的rsa key是否与ssh给出的一致
#总结，关联后第一次加上-u,以后就不要如上所述。
# $ git pull origin master  抓取远程master分支到本地分支



#从远程库克隆
#之前现有本地库，后有远程库的案例
#接上  现在是从0开始，克隆远程库
#接上 $ git clone git@github.com:michaelliao/gitskills.git
#接上，clone,must know the address of remote repository, .ssh,most fast,https,slow. 
# 切换分支 $ git checkout -b dev  相当于 $ git branch dev 创建分支  $ git checkout dev  切换分支


#在本地仓库版本库中，建立新的文件夹
#接上 mkdir newfolder   
#接上 git add new folder 
#接上 git commmit -m 'add a new folder to the repository'


#创建与合并分支
#$ git checkout -b dev  git switch -c dev表示创建并切换，相当于 $git branch dev  $ git checkout dev   git switch dev
#查看分支 $git branch
#合并分支dev成果并到master分支上  $ git checkout master    $git merge dev
#接上 合并完成后就可以删除dev $ git branch -d dev  查看后 git branch ,就只剩下master
# 合并分支 fastward 快进模式，直接指向分支提交


