# -*- conding: UTF-8 -*-


import os, sys, commands, subprocess, re , signal
from test_method import time_test


test_name = ""
log_path = ""

def test_1():
        print_name = "test_1"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 pub, 1 sub, 20hz , 2M data , 60s , valgrand used for memory leak , sub stopped first"

        run_time = 60


        package_name = "pub_and_sub_cpp"

        exec_name = ["talkerbase", "listenerbase"]

        end_turn = [1,0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "1_1"

        para_list = [ ["--name" , "talker1"],
                      ["--name" , "listener1"]
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "1 pub, 1 sub, 20hz , 2M data , 60s , valgrand used for memory leak , pub stopped first"
        end_turn = [0,1]
        log_index = "1_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name


def test_2():
        print_name = "test_2"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "3 pub, 1 sub, 20hz , 2M data , 60s  , sub stopped first"


        run_time = 60


        package_name = "pub_and_sub_cpp"

        exec_name = ["talkerbase", "talkerbase" , "talkerbase" ,"listenerbase"]

        end_turn = [3,0,1,2]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "2_1"

        para_list = [ ["--name" , "talker1"],
                      ["--name" , "talker2"],
                      ["--name" , "talker3"],
                      ["--name" , "listener1"]
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "3 pub, 1 sub, 20hz , 2M data , 60s , pub stopped first"

        end_turn = [0,1,2,3]
        log_index = "2_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name

def test_3():
        print_name = "test_3"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 pub, 3 sub, 20hz , 2M data , 60s  , sub stopped first"


        run_time = 60


        package_name = "pub_and_sub_cpp"

        exec_name = ["talkerbase", "listenerbase" , "listenerbase" ,"listenerbase"]

        end_turn = [1,2,3,0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "3_1"

        para_list = [ ["--name" , "talker1"],
                      ["--name" , "listener1"],
                      ["--name" , "listener2"],
                      ["--name" , "listener3"]
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "1 pub, 3 sub, 20hz , 2M data , 60s , pub stopped first"

        end_turn = [0,1,2,3]
        log_index = "3_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name

def test_4():
        print_name = "test_4"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "3 pub, 3 sub, 20hz , 2M data , 60s  , sub stopped first"


        run_time = 60


        package_name = "pub_and_sub_cpp"

        exec_name = ["talkerbase", "talkerbase" , "talkerbase" ,"listenerbase" , "listenerbase" , "listenerbase"]

        end_turn = [3,4,5,0,1,2]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "4_1"

        para_list = [ ["--name" , "talker1"],
                      ["--name" , "talker2"],
                      ["--name" , "talker3"],
                      ["--name" , "listener1"],
                      ["--name" , "listener2"],
                      ["--name" , "listener3"]
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "3 pub, 3 sub, 20hz , 2M data , 60s , pub stopped first"

        end_turn = [0,1,2,3,4,5]
        log_index = "4_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name


def test_5():
        print_name = "test_5"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 pub, 1 sub, 20hz , 256B - 2M data , 60s  , sub stopped first"

        run_time = 60

        package_name = "pub_and_sub_cpp"

        exec_name = ["talker5","listener5"]

        end_turn = [1,0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "5_1"

        para_list = [ [],
                      [],
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "1 pub, 1 sub, 20hz , 256B - 2M data , 60s , pub stopped first"

        end_turn = [0,1]
        log_index = "5_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name

def test_6():
        print_name = "test_6"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 pub, 1 sub, 20hz , 2M data , 60s  , sub stopped first"

        run_time = 60

        package_name = "pub_and_sub_py"

        exec_name = ["talker6","listener6"]

        end_turn = [1,0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "6_1"

        para_list = [ [],
                      [],
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "1 pub, 1 sub, 20hz , 2M data , 60s , pub stopped first"

        end_turn = [0,1]
        log_index = "6_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name

def test_7():
        print_name = "test_7"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "3 pub, 1 sub, 20hz , 2M data , 60s  , sub stopped first"

        run_time = 60

        package_name = "pub_and_sub_py"

        exec_name = ["talker7_1","talker7_2" , "talker7_3" , "listener7_1"]

        end_turn = [3,0,1,2]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "7_1"

        para_list = [ [],
                      [],
                      [],
                      []
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "3 pub, 1 sub, 20hz , 2M data , 60s , pub stopped first"

        end_turn = [0,1,2,3]
        log_index = "7_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name


def test_8():
        print_name = "test_8"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 pub, 3 sub, 20hz , 2M data , 60s  , sub stopped first"

        run_time = 60

        package_name = "pub_and_sub_py"

        exec_name = ["talker8_1", "listener8_1","listener8_2" , "listener8_3"]

        end_turn = [1,2,3,0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "8_1"

        para_list = [ [],
                      [],
                      [],
                      []
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "1 pub, 3 sub, 20hz , 2M data , 60s , pub stopped first"

        end_turn = [0,1,2,3]
        log_index = "8_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name


def test_9():
        print_name = "test_9"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "3 pub, 3 sub, 20hz , 2M data , 60s  , sub stopped first"

        run_time = 60

        package_name = "pub_and_sub_py"

        exec_name = ["talker9_1","talker9_2" , "talker9_3" , "listener9_1" , "listener9_2" , "listener9_3"]

        end_turn = [3,4,5,0,1,2]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "9_1"

        para_list = [ [],
                      [],
                      [],
                      [],
                      [],
                      []
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "3 pub, 3 sub, 20hz , 2M data , 60s , pub stopped first"

        end_turn = [0,1,2,3,4,5]
        log_index = "9_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name


def test_10():
        print_name = "test_10"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 pub, 1 sub, 20hz , 256B - 2M data , 60s  , sub stopped first"

        run_time = 60

        package_name = "pub_and_sub_py"

        exec_name = ["talker10" , "listener10"]

        end_turn = [1,0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "10_1"

        para_list = [ [],
                      []
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "1 pub, 1 sub, 20hz , 256B - 2M data , 60s , pub stopped first"

        end_turn = [0,1]
        log_index = "10_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name


def test_11():
        print_name = "test_11"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "3 pub, 3 sub, 3 topic , 20hz , 2M data , 300s  , sub stopped first"

        run_time = 300

        package_name = "pub_and_sub_cpp"

        exec_name = ["talkerbase" ,"talkerbase" , "talkerbase" ,  "listenerbase","listenerbase" , "listenerbase"]

        end_turn = [3,4,5,0,1,2]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "11_1"

        para_list = [ ["--name" , "talker1" , "--topic" , "chatter1"],
                      ["--name" , "talker2" , "--topic" , "chatter2"],
                      ["--name" , "talker3" , "--topic" , "chatter3"],
                      ["--name" , "listener1" , "--topic" , "chatter1"],
                      ["--name" , "listener2" , "--topic" , "chatter2"],
                      ["--name" , "listener3" , "--topic" , "chatter3"]
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "3 pub, 3 sub, 3 topic , 20hz , 2M data , 300s , pub stopped first"

        end_turn = [0,1,2,3,4,5]
        log_index = "11_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name


def test_12():
        print_name = "test_12"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "3 pub, 3 sub, 20hz , 2M data , 300s  , sub stopped first"

        run_time = 60

        package_name = "pub_and_sub_py"

        exec_name = ["talker12_1" , "talker12_2" , "talker12_3" , "listener12_1" , "listener12_2" , "listener12_3"]

        end_turn = [3,4,5,0,1,2]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "12_1"

        para_list = [ [],
                      [],
                      [],
                      [],
                      [],
                      []
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  " 3 pub, 3 sub, 20hz , 2M data , 300s , pub stopped first"

        end_turn = [0,1,2,3,4,5]
        log_index = "12_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name


def test_N1():
        print_name = "test_N1"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 pub, 1 sub, 20hz , 256B - 2M data , 60s  , sub stopped first"

        run_time = 60

        package_name = "pub_and_sub_cpp"

        exec_name = ["talkerN1","listenerN1"]

        end_turn = [1,0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "N1_1"

        para_list = [ [],
                      [],
                    ]


        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        test_info =  "1 pub, 1 sub, 20hz , 256B - 2M data , 60s , pub stopped first"

        end_turn = [0,1]
        log_index = "N1_2"

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list)

        print "finished " + print_name


def test_13():
        print_name = "test_13"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 server , 1 client , 100 requests "

        run_time = 300

        package_name = "rpc_cpp"

        exec_name = ["server13","client13"]

        end_turn = [0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "13"

        para_list = [ [],
                      [],
                    ]

        rpc_flag = True
        client_st = 1

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list , rpc_flag , client_st)

        print "finished " + print_name


def test_14():
        print_name = "test_14"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 server , 3 client in 3 process , 1 topic , 100 requests "

        run_time = 300

        package_name = "rpc_cpp"

        exec_name = ["server14_1","client14_1","client14_2" , "client14_3"]

        end_turn = [0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "14"

        para_list = [ [],
                      [],
                      [],
                      []
                    ]

        rpc_flag = True
        client_st = 1

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list , rpc_flag , client_st)

        print "finished " + print_name


def test_15():
        print_name = "test_15"

        print "start " + print_name

        global  test_name , log_path
        
        test_info =  "1 server , 3 client in 3 process , 3 topic , 100 requests "
        
        run_time = 300

        package_name = "rpc_cpp"
        
        exec_name = ["server15_1","client15_1","client15_2" , "client15_3"]
        
        end_turn = [0]
        
        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "15"

        para_list = [ [],
                      [],
                      [],
                      []
                    ]

        rpc_flag = True
        client_st = 1

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list , rpc_flag , client_st)

        print "finished " + print_name


def test_16():
        print_name = "test_16"

        print "start " + print_name

        global  test_name , log_path
        
        test_info =  "3 server , 3 client in 3 process , 3 topic , 100 requests "
        
        run_time = 300

        package_name = "rpc_cpp"
        
        exec_name = ["server16_1","server16_2" , "server16_3" , "client16_1","client16_2" , "client16_3"]
        
        end_turn = [0,1,2]
        
        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "16"

        para_list = [ [],
                      [],
                      [],
                      [],
                      [],
                      []
                    ]

        rpc_flag = True
        client_st = 3

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list , rpc_flag , client_st)

        print "finished " + print_name

def test_17():
        print_name = "test_17"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 server , 1 client , 100 requests "

        run_time = 300

        package_name = "rpc_py"

        exec_name = ["server17","client17"]

        end_turn = [0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "17"

        para_list = [ [],
                      [],
                    ]

        rpc_flag = True
        client_st = 1

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list , rpc_flag , client_st)

        print "finished " + print_name


def test_18():
        print_name = "test_18"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 server , 3 client in 3 process , 1 topic , 100 requests "

        run_time = 300

        package_name = "rpc_py"

        exec_name = ["server18_1","client18_1","client18_2" , "client18_3"]

        end_turn = [0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "18"

        para_list = [ [],
                      [],
                      [],
                      []
                    ]

        rpc_flag = True
        client_st = 1

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list , rpc_flag , client_st)

        print "finished " + print_name

def test_19():
        print_name = "test_19"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "1 server , 3 client in 3 process , 3 topic , 100 requests "

        run_time = 300

        package_name = "rpc_py"

        exec_name = ["server19_1","client19_1","client19_2" , "client19_3"]

        end_turn = [0]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "19"

        para_list = [ [],
                      [],
                      [],
                      []
                    ]

        rpc_flag = True
        client_st = 1

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list , rpc_flag , client_st)

        print "finished " + print_name


def test_20():
        print_name = "test_20"

        print "start " + print_name

        global  test_name , log_path

        test_info =  "3 server , 3 client in 3 process , 3 topic , 100 requests "

        run_time = 300

        package_name = "rpc_py"

        exec_name = ["server20_1","server20_2" , "server20_3" , "client20_1","client20_2" , "client20_3"]

        end_turn = [0,1,2]

        run_path = log_path[:-12] +  '/install_isolated/' + package_name + "/lib/" + package_name + "/"
        log_index = "20"

        para_list = [ [],
                      [],
                      [],
                      [],
                      [],
                      []
                    ]

        rpc_flag = True
        client_st = 3

        time_test.time_test( end_turn , exec_name , test_name , log_path , run_path , run_time , log_index , test_info , para_list , rpc_flag , client_st)

        print "finished " + print_name




def test(tmp_test_name  ,tmp_log_path):

        global  test_name , log_path
 
        test_name = tmp_test_name
        log_path = tmp_log_path


        test_1()

        test_2()

        test_3()
        test_4()
        test_5()
        test_6()
        test_7()
        test_8()
        test_9()
        test_10()
        test_11()
        test_12()
        test_13()
        test_14()
        test_15()
        test_16()
        test_17()
        test_18()
        test_19()
        test_20()
	
	
	print "all test finished !"
        return 		


