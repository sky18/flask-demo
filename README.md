# flask-demo
daydayup2022-python

一、建立 github 版本库
在 github 注册一个 github 账户, 这个不用我多说, 大家都知道注册.

二、然后添加你的一个 online 版本库 repository:

*起一个具有标识性的项目名称

三、添加好了以后, 根据github官方生成的页面里的代码，连接上本地版本库。

四、将本地的版本库推送到网上:

$ git remote add origin https://github.com/sky18/git-demo.git
$ git push -u origin master     # 推送本地 master 去 origin
$ git push -u origin dev        # 推送本地 dev  去 origin



五、推送修改
如果修改了本地版本库的代码， 先commit，再push

$ git commit -am "change XXXXXX"
$ git push -u origin master
