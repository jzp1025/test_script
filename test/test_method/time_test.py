# -*- conding: UTF-8 -*-

import time, subprocess,signal

def time_test(pub_name , sub_name , package_name , run_time):
	
	print "begin time_test : "

	time_start=time.time()


	pub_list = []

	sub_list = []

	for name in pub_name:
	    run_pub_sh = "ros2 run " + package_name + " " + name
	    p = subprocess.Popen(run_pub_sh,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	    pub_list.append(p)


	for name in sub_name:
	    run_sub_sh = "ros2 run " + package_name + " " + name  
	    q = subprocess.Popen(run_sub_sh,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	    sub_list.append(q)

	flag = 0

	while True:
	    time_end = time.time()
	    #print time_end - time_start
	    if(time_end-time_start >= run_time):
		break

	    i = 0
	    for p in pub_list:
		    return_state = p.poll()
		
		    if return_state != None:
    			print pub_name[i] + " --- Error Code : " + str(return_state)
			flag = 1
			break
        	    i += 1

	    i = 0
	    for q in sub_list:
		    return_state = q.poll()
		
		    if return_state != None:
    			print sub_name[i] + " --- Error Code : " + str(return_state)
			flag = 1
			break
	            i += 1
	    
	    if(flag == 1):
		break

	i = 0
	for p in pub_list:
	    p.send_signal(signal.SIGINT)
	    print pub_name[i] + " --- return Code : " + str(p.poll())
	    i += 1

	i = 0
	for q in sub_list:
	    q.send_signal(signal.SIGINT)
	    print sub_name[i] + " --- return Code : " + str(p.poll())
	    i += 1


	print "time_test : program finished in " + str(run_time) + "(s) !"


	
