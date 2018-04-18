import subprocess
import os
import signal ,time

run_pub_sh = "/home/tusimple/xinliu/ros2_ws/install_isolated/pub_and_sub_cpp/lib/pub_and_sub_cpp/talker1"

#run_pub_sh = "ros2 run pub_and_sub_cpp talker1"

p = subprocess.Popen(run_pub_sh, stdout=subprocess.PIPE, close_fds=True)
#p = subprocess.Popen(run_pub_sh)
#           pub_list.append(p)
#os.kill(p.pid, signal.SIGINT)


           # out = p.communicate()

            #print out
print p.pid

time.sleep(10)

os.kill(p.pid,signal.SIGINT)
