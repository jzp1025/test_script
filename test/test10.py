# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test
from test_method import get_log_test

def test(run_time , test_name , log_number , log_path):

	print "start test 10 : "

	print "Test Content : py , 1 talker , 1 listener , 1 topic , float payload"



	package_name = "pub_and_sub_py"

	talker_name = ["talker10"]

	listener_name = ["listener10"]

	

	time_test.time_test(talker_name , listener_name , package_name , run_time)
 
	get_log_test.get_log_test(talker_name , listener_name , package_name , test_name , log_number, log_path)

	
	
	print "all test finished !"

