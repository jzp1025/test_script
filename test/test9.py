# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test

def test(run_time , test_name , log_number , log_path):


	print "start test 9 : "

	print "Test Content : py , 3 talker , 3 listener , 1 topic"


	package_name = "pub_and_sub_py"

	talker_name = ["talker9_1" , "talker9_2" , "talker9_3"]

	listener_name = ["listener9_1" , "listener9_2" , "listener9_3"]


	run_path = log_path[:-12]

 
        time_test.time_test(talker_name , listener_name , package_name , test_name , log_number, log_path , run_path , run_time)

	
	
	
	print "all test finished !"


