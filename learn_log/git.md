```
# 克隆
git clone git@github.com:CNmanyue/wangzai_bot.git
git clone https://github.com/CNmanyue/wangzai_bot.git

# 本地关联远程
git remote add origin git@github.com:CNmanyue/wangzai_bot.git

# (创建)本地分支关联远程分支
git checkout -b dev origin/dev

# 配置的是你个人的用户名称和电子邮件地址，这两条配置很重要，每次 Git 提交时都会引用这两条信息，说明是谁提交了更新，所以会随更新内容一起被永久纳入历史记录
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com

# 推送到远程库
git push
注意：
    github绑定公钥后，密钥对需要存在于~/.ssh

# 生成ssh并将pub添加到github
ssh-keygen
# Win7中设置rsa的名称，Win10中只能识别id_rsa
```

```
# 创建并切换分支
git checkout -b branchName

# 查看分支
git branch
```