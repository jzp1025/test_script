# -*- conding: UTF-8 -*-i

import logging, subprocess, signal , os  , time
import fcntl

def nonBlockRead(output):
    return '' 
    
    fd = output.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    try:
        return output.read()
    except:
        return ''

def time_test(end_turn , exec_name , test_name , log_path , tmp_path , run_time , log_index , test_info,para_list , rpc_flag = False , client_st = 0):

        log_name = log_path + '/log/' + test_name +'_' + log_index + '.log'

	if(os.path.exists(log_name)):
		os.remove(log_name)

	print "start time test logging : "
	
        logger = logging.getLogger("loggingmodule.NomalLogger")  
    	handler = logging.FileHandler(log_name) 
    	formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")  
    	handler.setFormatter(formatter)  
    	logger.addHandler(handler)  
    	logger.setLevel(logging.DEBUG)  

        
        logger.info('\n' + test_info + '\n')

        logger.debug('\n' + "Test : Time Test" + '\n')
        logger.debug('\n' + "test begin , start run shell command :" + '\n')

	
        start_process_list = []
	end_process_list = []


	for index in range(len(exec_name)):
	    run_start_sh = [ tmp_path + exec_name[index] ] 
            
            for para in para_list[index]:
                run_start_sh.append(para)
                                          
	    
	    logger.info(run_start_sh)
            print run_start_sh        
 
            p = subprocess.Popen(run_start_sh , stdout=subprocess.PIPE,stderr=subprocess.PIPE)
           

	    start_process_list.append(p)

            print p.pid


	for index in end_turn:
	    end_process_list.append(start_process_list[index])

      

        time_start = time.time()

        time_end = time_start + run_time
        wait_second = 1

        rpc_end_flag = False

        while True:
            time_now = time.time()
            
            if(time_now >= time_end):
                break

            if(rpc_flag == True):
                rpc_end_flag = True
                for index in range(len(start_process_list)):
                    if(index >= client_st && start_process_list[index].poll() == None):
                        rpc_end_flag = False
                        break;
                if(rpc_end_flag == True):
                    break;
        
            time.sleep(wait_second)


        flag = 0

        i = 0
        for p in start_process_list:
            return_state = p.poll()

            if return_state != None && i < client_st:
                print start_list_name[i] + " --- Error Code : " + str(return_state)
                logger.error('\n' + start_list_name[i] + " --- Error Code : " + str(return_state) + '\n')
                flag = 1
                break
            
            i += 1


        logger.debug('\n' + "--------------Time Test Finished , Start Logging" + '\n')     
        if(flag == 1):
            logger.error('\n' + "--------------Logger exit : terminal exit unnormally" + '\n')
            return



        
        for p in end_process_list:
            print "try to kill " + str(p.pid)
            p.send_signal(signal.SIGINT) 
            time.sleep(5)

        for p in start_process_list:
            if(p.poll() == None):
               print("Failed to kill -2 " + str(p.pid))
               logger.error('\n' + "Failed to Ctrl^C " + str(p.pid) + " , kill -9" + '\n')
               flag = 1
    
        if(flag == 1):
            logger.error('\n' + "Failed to exit subprocess , exit" + '\n')
            return
 
 
 
        i = 0
        for p in start_process_list:         
            print p.pid
            print p.poll()
           

            (out,err ) = p.communicate()
            print "communicate succeed"
            
            print "Log of " + exec_name[i]
            logger.debug('\n' + "Logging " + exec_name[i] + '\n')
            logger.info("\n" + out + '\n')
            logger.info("\n" + err + '\n')
            i += 1

        

        logger.debug('\n' + "Logging Finished , Start quit the subprocess" + '\n')

        logger.removeHandler(handler)


        return 

