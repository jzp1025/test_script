# test_script
自动化测试脚本  
Install:  
cd ~/ros2_ws  
git clone xxxxx   
cd test_script  

usege：   `python test_all.py -n <test_name/all> -t <runtime>`

若要查看core dumped file ， 首先在命令行输入`ulimit -c unlimited`  
会在根目录下产生core文件  
使用gdb可以调试  

（若要修改corefile的name和path，请在有权限的情况下按如下操作：  
$> mkdir -p /tmp/cores  
$> chmod a+rwx /tmp/cores  
$> echo "/tmp/cores/core.%e.%p.%h.%t" > /proc/sys/kernel/core_pattern  
）  
