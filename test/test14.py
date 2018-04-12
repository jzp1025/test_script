# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test
from test_method import get_log_test

def test(run_time , test_name , log_number , log_path):


	print "start test 14 : "

	print "Test Content : cpp , 1 server , 3 client , get 2 ints sum"



	package_name = "rpc_cpp"

	server_name = ["server14_1"]

	client_name = ["client14_1" , "client14_2" , "client14_3"]


	run_path = log_path[:-12]

	time_test.time_test(talker_name , listener_name , package_name , run_time , run_path)
 
	get_log_test.get_log_test(talker_name , listener_name , package_name , test_name , log_number, log_path , run_path)

	
	
	print "all test finished !"

