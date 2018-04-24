# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test

def test(run_time , test_name  , log_path):


	test_info =  "start test 1 : Test Content : cpp , 1 talker , 1 listener , 1 topic"


	package_name = "pub_and_sub_cpp"
        
        exec_name = ["talkerbase", "listenerbase"]

	start_list_name = ["talker1","listener1"]

	end_turn = [1,0]

	run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/" 
        log_index = "1"

        para_list = [ ["--name" , "talker1"],
                      ["--name" , "listener1"]
                    ]
        

        time_test.time_test(start_list_name , end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

	
	
	print "all test finished !"
        return 		


