# -*- conding: UTF-8 -*-

from test import test1
import os

cwd = os.getcwd()

test_cases = ["test1"]

if(os.path.exists(cwd+'/log') == False):
	os.makedirs(cwd+'/log') 


print "Please Input test cases : ('all' or 'testN.py')"

test_case_str = raw_input();

if(test_case_str == "all"):
	print "Please Input test time : (s)"

	run_time = input();

	print "Please Input number of logging : "

	log_number = input();


	for case in test_cases:
		locals()[case].test(run_time  , case , log_number, cwd)

else:
	print "Please Input test time : (s)"

	run_time = input();

	print "Whether to see the details : (Y/n)"

	detail_flag = raw_input();

	print "Please Input number of logging : "

	log_number = input();
	
	locals()[test_case_str].test(run_time , test_case_str , log_number , cwd)




