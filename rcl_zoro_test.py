# -*- conding: UTF-8 -*-


import os
import logging, subprocess, signal , time
import sys, getopt

def main(argv):

     cwd = os.getcwd()

     file_dir = cwd[:-12] + '/build_isolated/rcl/test'
     print file_dir

     try:
        opts, args = getopt.getopt(argv, "hn:",["test_name="])
     except getopt.GetoptError:
        print 'rcl_zoro_test.py -n <str which test contains>'
        sys.exit(2)

     for opt, arg in opts:
        if opt == '-h':
            print 'rcl_zoro_test.py -n <str which test contains>'
            sys.exit()
        elif opt in ("-n", "--test_name"):
            test_case_str = arg

     print "test_case_str: " + test_case_str

     for root, dirs, files in os.walk(file_dir):
        #print(root)
        #print(dirs)
        #print(files)
        break
 
     test_list = []
     
     for file_name in files:
         if test_case_str in str(file_name):
            if "client" in str(file_name):
                continue 
            if "service" in str(file_name):
                continue  
            if file_name.endswith("cpp"):
                test_list.append(file_name)


     print test_list

     log_path = cwd + '/rcl_zoro_test.log'
     print log_path

     if(os.path.exists(log_path)):
         os.remove(log_path)

     print("start time test logging : ")

     logger = logging.getLogger("loggingmodule.NomalLogger")
     handler = logging.FileHandler(log_path)
     formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
     handler.setFormatter(formatter)
     logger.addHandler(handler)
     logger.setLevel(logging.DEBUG)
  
     logger.debug("rcl_zoro_test start : ")
 

     for test_name in test_list : 
          
          print "start running : " + test_name

          run_sh = cwd[:-12] + '/build_isolated/rcl/test/' + test_name
          p = subprocess.Popen([run_sh]  , stdout=subprocess.PIPE,stderr=subprocess.PIPE)
          (out, err) = p.communicate()
          print out
          print err
          logger.debug('\n' + "start running : " + test_name)
          logger.debug('\n' + out)
          if(err != ''):
             logger.error('\n' + err)
             print "error :" + err
          
          time.sleep(2)

     logger.debug('\n' + "all test finished")
     logger.removeHandler(handler)
     logger.info('\n\n' )

if __name__ == "__main__":
     main(sys.argv[1:])

