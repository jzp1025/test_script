# -*- conding: UTF-8 -*-

import logging, subprocess, signal , os

def get_log_test(pub_name , sub_name , package_name , test_name , log_number, log_path , tmp_path):


	if(os.path.exists(log_path + '/log/' + test_name + '.log')):
		os.remove(log_path + '/log/' + test_name + '.log')

	print "start Logging : "

	logger = logging.getLogger("loggingmodule.NomalLogger")  
    	handler = logging.FileHandler(log_path + '/log/' + test_name + '.log') 
    	formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")  
    	handler.setFormatter(formatter)  
    	logger.addHandler(handler)  
    	logger.setLevel(logging.DEBUG)  
	
	pub_list = []

	sub_list = []

	for name in pub_name:
	    run_pub_sh = tmp_path + '/install_isolated/' + package_name + "/lib/" + package_name + "/" + name
	    
	    logger.info(run_pub_sh)

	    p = subprocess.Popen(run_pub_sh,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	    pub_list.append(p)


	for name in sub_name:
	    run_sub_sh = tmp_path + '/install_isolated/' + package_name + "/lib/" + package_name + "/" + name 
		
	    logger.info(run_sub_sh)

	    q = subprocess.Popen(run_sub_sh,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	    sub_list.append(q)

	count = 0
	flag = 0

	while True:
		
		i = 0
	    	for p in pub_list:
		    line=p.stdout.readline().strip()
		    count += 1
		    logger.debug(str(count) + " --- " + line)

		    return_state = p.poll()
		
		    if return_state != None:
    			logger.error(pub_name[i] + " --- Error Code : " + str(return_state))
			flag = 1
			break
        	    i += 1

	    	i = 0
	   	for q in sub_list:
		    line=q.stdout.readline().strip()
		    count += 1

		    logger.debug(str(count) + " --- " + line)
		    return_state = q.poll()
		
		    if return_state != None:
    			logger.error(sub_name[i] + " --- Error Code : " + str(return_state))
			flag = 1
			break
	            i += 1
	    
	    	if(flag == 1):
			break

	   	if(count >= log_number):
			break
	
		
	i = 0
	for p in pub_list:
	    p.send_signal(signal.SIGINT)
	    logger.info(pub_name[i] + " --- return Code : " + str(p.poll()))
	    i += 1

	i = 0
	for q in sub_list:
	    q.send_signal(signal.SIGINT)
	    logger.info(sub_name[i] + " --- return Code : " + str(p.poll()))
	    i += 1

	print "Logging finished ! "





