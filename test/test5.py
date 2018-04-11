# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test
from test_method import get_log_test

def test(run_time , test_name , log_number , log_path):

	print "start test 5 : "

	print "Test Content : cpp , 1 talker , 1 listener ,1 topic , payload = 256 and double everytime"




	package_name = "pub_and_sub_cpp"

	talker_name = ["talker5_1"]

	listener_name = ["listener5_1"]


	time_test.time_test(talker_name , listener_name , package_name , run_time)
 
	get_log_test.get_log_test(talker_name , listener_name , package_name , test_name , log_number, log_path)

	
	
	print "all test finished !"


