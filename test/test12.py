# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test
from test_method import get_log_test

def test(run_time , test_name , log_number , log_path):


	print "start test 12 : "

	print "Test Content : py , 3 talker , 3 listener ,3 topic"



	package_name = "pub_and_sub_py"

	talker_name = ["talker12_1" , "talker12_2" , "talker12_3"]

	listener_name = ["listener12_1" , "listener12_2" , "listener12_3"]



	

	time_test.time_test(talker_name , listener_name , package_name , run_time)
 
	get_log_test.get_log_test(talker_name , listener_name , package_name , test_name , log_number, log_path)

	
	
	print "all test finished !"

