# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test
from test_method import get_log_test

def test(run_time , test_name , log_number , log_path):

	print "start test 2 : "

	print "Test Content : cpp , 3 talker , 1 listener , 1 topic"



	package_name = "pub_and_sub_cpp"

	talker_name = ["talker2_1","talker2_2","talker2_3"]

	listener_name = ["listener2_1"]

	run_path = log_path[:-12]

	time_test.time_test(talker_name , listener_name , package_name , run_time , run_path)
 
	get_log_test.get_log_test(talker_name , listener_name , package_name , test_name , log_number, log_path , run_path)

	
	
	
	print "all test finished !"
		


