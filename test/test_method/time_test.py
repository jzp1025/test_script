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

def time_test(pub_name , sub_name , package_name , test_name , log_number, log_path , tmp_path , run_time):


	if(os.path.exists(log_path + '/log/' + test_name + '.log')):
		os.remove(log_path + '/log/' + test_name + '.log')

	print "start time test logging : "
	
        logger = logging.getLogger("loggingmodule.NomalLogger")  
    	handler = logging.FileHandler(log_path + '/log/' + test_name + '.log') 
    	formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")  
    	handler.setFormatter(formatter)  
    	logger.addHandler(handler)  
    	logger.setLevel(logging.DEBUG)  


        logger.debug("Test : Time Test")
        logger.debug("test begin , start run shell command :")

	
	pub_list = []

	sub_list = []


	for name in pub_name:
	    run_pub_sh =   tmp_path + '/install_isolated/' + package_name + "/lib/" + package_name + "/" + name  
                           
#            run_pub_sh = "ros2 run pub_and_sub_cpp talker1"                  
	    
	    logger.info(run_pub_sh)
            print run_pub_sh             
 
            p = subprocess.Popen([run_pub_sh]  , stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            #p.send_signal(signal.SIGINT)

           # p = subprocess.Popen(run_pub_sh,stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell = True)
	    pub_list.append(p)

            print p.pid


	for name in sub_name:
	    run_sub_sh = tmp_path + '/install_isolated/' + package_name + "/lib/" + package_name + "/" + name  
            

	    logger.info(run_sub_sh)

            q = subprocess.Popen([run_sub_sh] , stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            #q.send_signal(signal.SIGINT)

	    #q = subprocess.Popen(run_sub_sh,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell = True)
	    sub_list.append(q)

      

        time_start = time.time()
        flag = 0

        while True:
            time_end = time.time()
            #print time_end - time_start
            if(time_end-time_start >= run_time):
                break

            i = 0
            for p in pub_list:
                    return_state = p.poll()
                    #print i
                    #p.send_signal(signal.SIGINT)

                    if return_state != None:
                        print pub_name[i] + " --- Error Code : " + str(return_state)
                        logger.error(pub_name[i] + " --- Error Code : " + str(return_state))
                        flag = 1
                        break
#                    else:
 #                       p.send_signal(signal.SIGINT)
                    i += 1

            i = 0
            for q in sub_list:
                    return_state = q.poll()
                    #q.send_signal(signal.SIGINT)
 
                    if return_state != None:
                        print sub_name[i] + " --- Error Code : " + str(return_state)
                        logger.error(sub_name[i] + " --- Error Code : " + str(return_state))

                        flag = 1
                        break
  #                  else:
   #                     q.send_signal(signal.SIGINT)
                    i += 1

            if(flag == 1):
                break

        logger.debug("--------------Time Test Finished , Start Logging")     
                 

        i = 0
        
        for p in pub_list:
            print "try to kill " + str(p.pid)
            p.send_signal(signal.SIGINT) 
            p.wait()
               #time.sleep(5)
              
            print p.pid
            print p.poll()
            (out,err ) = p.communicate()
            print "communicate succeed"
            #err = p.communicate()[1]
            count = 0
            print "Log of " + pub_name[i]
            logger.debug("Logging " + pub_name[i])
            logger.info("\n" + out)
            logger.info("\n" + err)
            #while(count < log_number):
             #   line  = nonBlockRead(p.stdout)
                        #print line
              #  if line :
               #     print line
                #    logger.info("\n" + line)
              #  err = nonBlockRead(p.stderr)
              #  if err :
              #      logger.error("\n" + err)
              #  count += 1
            i += 1

        i = 0
        
        for q in sub_list:
            q.send_signal(signal.SIGINT)
            q.wait()
            print q.pid
            print q.poll()
            (out,err) = q.communicate()
           # err = q.communicate()[1]

            count = 0
            print "Log of " + sub_name[i]
            logger.debug("Logging " + sub_name[i])
            logger.info("\n" + out)
            logger.info("\n" + err) 
          # while(count < log_number):
            #    line  = nonBlockRead(q.stdout)
                        #print line
             #   if line :
              #      print line
             #       logger.info(" --- " + line)
             #   err = nonBlockRead(q.stderr)
             #   if err :
             #       logger.error("\n" + err)

              #  count += 1
            i += 1

        logger.debug("Logging Finished , Start quit the subprocess")

        logger.removeHandler(handler)


        return 

        i = 0
        for p in pub_list:
            return_state = p.poll()

            if return_state == None:
                #p.send_signal(signal.SIGINT)
            
                print p.pid
                while(p.poll() == None):
                     print "try to kill " + str(p.pid)
                     print p.poll()
                     time.sleep(1)
                     os.kill(p.pid, signal.SIGINT)              
                   

                return_state = p.poll()
                print pub_name[i] + str(return_state)
                logger.info(pub_name[i] + " --- return Code : " + str(return_state))
            else:
                logger.error(pub_name[i] + " --- Error Code : " + str(return_state))
            i += 1
            

        i = 0
        for q in sub_list:
            return_state = q.poll()

            if return_state == None:
                 while(q.poll() == None):
                      print "try to kill " + str(q.pid)
                      os.kill(q.pid, signal.SIGINT)
                 

                 return_state = q.poll()
                 print sub_name[i] + str(return_state)
                 logger.info(sub_name[i] + " --- return Code : " + str(return_state))
            else:
                logger.error(sub_name[i] + " --- Error Code : " + str(return_state))
  
            i += 1

        print "Test finished ! "

        logger.debug("Test Finished !")

        logger.removeHandler(handler)
