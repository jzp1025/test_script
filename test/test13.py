# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test
from test_method import get_log_test

def test(run_time , test_name , log_number , log_path):


	print "start test 13 : "

	print "Test Content : cpp , 1 server , 1 client , get 2 ints sum"



	package_name = "rpc_cpp"

	server_name = ["server13"]

	client_name = ["client13"]



	

	time_test.time_test(server_name , client_name , package_name , run_time)
 
	get_log_test.get_log_test(server_name , client_name , package_name , test_name , log_number, log_path)

	
	
	print "all test finished !"

