# -*- conding: UTF-8 -*-

from test import test1 , test2 , test3

import os

import sys, getopt

def main(argv):

     cwd = os.getcwd()

     #test_cases = ["test1" , "test2" , "test3"]
     test_cases = ["test1"]

     if(os.path.exists(cwd+'/log') == False):
         os.makedirs(cwd+'/log') 
         print("log dir build succeed !")

     print("log dir path is : " + cwd+'/log')


#     print "Please Input test cases : ('all' or 'testN.py')"



     try:
        opts, args = getopt.getopt(argv, "hn:t:l:",["test_name=","test_time=","log_number="])
     except getopt.GetoptError:
        print 'test_all.py -n <test_name all or testN.py> -t <test_time> -l <log_number>'
        sys.exit(2)

     for opt, arg in opts:
        if opt == '-h':
            print 'test_all.py -n <test_name all or testN.py> -t <test_time> -l <log_number>'
            sys.exit()
        elif opt in ("-t", "--test_time"):
            run_time = arg
        elif opt in ("-l", "--log_number"):
            log_number = arg
        elif opt in ("-n", "--test_name"):
            test_case_str = arg

     if(test_case_str == "all"):

        for case in test_cases:
             print case
             globals()[case].test(run_time  , case , log_number, cwd)
             print case

     else:
        
	
        locals()[test_case_str].test(run_time , test_case_str , log_number , cwd)

if __name__ == "__main__":
     main(sys.argv[1:])


