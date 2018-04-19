# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test

def test(run_time , test_name , log_number , log_path):

	print "start test 10 : "

	print "Test Content : py , 1 talker , 1 listener , 1 topic , float payload"



	package_name = "pub_and_sub_py"

	talker_name = ["talker10"]

	listener_name = ["listener10"]

	
	run_path = log_path[:-12]

 
        time_test.time_test(talker_name , listener_name , package_name , test_name , log_number, log_path , run_path , run_time)

	
	
	
	print "all test finished !"

