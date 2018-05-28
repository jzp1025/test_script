# -*- conding: UTF-8 -*-

from test import testbase

import os

import sys, getopt

def main(argv):

     cwd = os.getcwd()

     #test_cases = ["test1" , "test2" , "test3", "test4" , "test5" ,"test6" , "test7" , "test8" ,"test9", "test10" , "test11" , "test12" ,"testN1_cpp" , "testN1_py"]
     test_cases = ["testbase"]

     if(os.path.exists(cwd+'/log') == False):
         os.makedirs(cwd+'/log') 
         print("log dir build succeed !")

     print("log dir path is : " + cwd+'/log')



 
     msg_content = "This is a msg !"

     try:
        opts, args = getopt.getopt(argv, "hn:m",["test_name=","msg_content="])
     except getopt.GetoptError:
        print 'test_all.py -n <test_name all or testN.py>'
        sys.exit(2)

     for opt, arg in opts:
        if opt == '-h':
            print 'test_all.py -n <test_name all or testN.py>'
            sys.exit()
        elif opt in ("-n", "--test_name"):
            test_case_str = arg
	elif opt in ("-m","--msg_content"):
	    msg_content = arg


     if(test_case_str == "all"):

        for case in test_cases:
             print case
             globals()[case].test( case , cwd , msg_content)
             print case

     else:
        
	
        locals()[test_case_str].test( test_case_str , cwd, msg_content)

if __name__ == "__main__":
     main(sys.argv[1:])


