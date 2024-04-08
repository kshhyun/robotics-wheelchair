#!/usr/bin/env python
# -*- coding: utf-8 -*-

#로봇의 현재위치를 파악하고, 목적지까지 올바른 경로로 이동 test
import rospy
import tf
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from geometry_msgs.msg import Pose

# 노드 초기화
rospy.init_node('control_test', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
#변수 초기화
goal = MoveBaseGoal()
goalpos = '' #목적지 숫자 문자열
position = '' #현재 로봇 위치
#현재위치 관련 초기화
tf_listener = tf.TransformListener() 
tf_blistener = tf.TransformListener(tf_listener) 

#pt1, pt5 포인트 변경 필요
#목적지 설정 함수 (함수 이름의 spot으로 goal 설정)
def pt1():
     #goal=pt1 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.485
         goal.target_pose.pose.position.y = -0.0709
         goal.target_pose.pose.position.z = 0
         print("goal: pt1")
def pt2():
     #goal=pt2 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.485
         goal.target_pose.pose.position.y = -0.9833
         goal.target_pose.pose.position.z = 0
         print("goal: pt2")
def pt3():
     #goal=pt3 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0
         goal.target_pose.pose.position.x = 0.882
         goal.target_pose.pose.position.y = -1.205
         goal.target_pose.pose.position.z = 0
         print("goal: pt3")    
def pt5():
     #goal=pt5 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 1.279
         goal.target_pose.pose.position.y = 0.117
         goal.target_pose.pose.position.z = 0
         print("goal: pt5")
def pt6():
     #goal=pt6 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.5417
         goal.target_pose.pose.position.y = 0.3574
         goal.target_pose.pose.position.z = 0
         print("goal: pt6")
def desk():
     #goal=desk 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.0
         goal.target_pose.pose.position.y = 0.0
         goal.target_pose.pose.position.z = 0
         print("goal: desk")
def center():
      #goal=응급의료센터 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 1.3
         goal.target_pose.pose.position.y = -1.591
         goal.target_pose.pose.position.z = 0
         print("goal: center")
def CT():
      #goal=CT 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 1.3202
         goal.target_pose.pose.position.y = -0.461
         goal.target_pose.pose.position.z = 0
         print("goal: CT")
def Out_spot():
      #goal=Out 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.1943
         goal.target_pose.pose.position.y = -1.1960
         goal.target_pose.pose.position.z = 0
         print("goal: Out")
def In_spot():
      #goal=In 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.8685
         goal.target_pose.pose.position.y = -1.8902
         goal.target_pose.pose.position.z = 0
         print("goal: In")
'''
def 화장실()
def 치과()
def 이비인후과()
'''



#현재 로봇 위치 파악 함수 -> 현재 좌표를 확인해 position 변수에 현재 위치명 저장
def check_robot_position():
    print("check_robot_position 함수 호출 시작")
    global position 

    try:
        (trans, rot) = tf_listener.lookupTransform('/map', '/base_footprint', rospy.Time(0)) #현재 시간에 대한 로봇 위치 가져옴
       
        # x,y 좌표 확인
        x = trans[0]
        y = trans[1]

        #x,y 좌표에 따른 position 변수에 문자열 저장

        #좌측
        if (-1<= x <=0.34) and (-0.811<= y <= 0.034):
            position = 'desk' #접수처
            print("현재위치:", position)
        elif (0.6494 <= x <= 5 ) and (-0.730 <= y <= -0.271):
            position = 'CT' #CT촬영실
            print("현재위치:", position)
        elif (1.007 <= x <= 5 ) and (-2 <= y <= -1.4874): #y좌표 수정 필요
            position = 'center' #응급의료 센터
            print("현재위치:", position)

        elif (0.34<= x <=0.6496) and (-0.811<= y <= 0.034):
            position = 'pt1' 
            print("현재위치:", position)
        elif (0.34 <= x <= 0.6496) and (-1.707 <= y <= -0.811):
            position = 'pt2' 
            print("현재위치:", position)
        elif (0.649 <= x <= 1.007) and (-1.707<= y <= -0.811):
            position = 'pt3'
            print("현재위치:", position)
        elif (1.007 <= x <= 5 ) and (-1.487 <= y <= -0.731):
            position = 'pt4'
            print("현재위치:", position)
        elif (0.6494 <= x <= 5 ) and (-0.270 <= y <= 5):
            position = 'pt5'
            print("현재위치:", position)
        elif (0.34 <= x <= 0.6493 ) and (-0.034 <= y <= 5):
            position = 'pt6'
            print("현재위치:", position)
        
        #우측
        elif ( -5 <= x <= 0.1943 ) and ( -10 <= y <= 0.811 ):
            position = 'A'
            print("현재위치:", position)
        elif ( 0.1944 <= x <= 5 ) and ( -10 <= y <= -1.8902):
            position = 'B'
            print("현재위치:", position)

    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        rospy.logerr("예외발생")

#목적지로 이동하는 함수
def robot_move():
    print("robot_move 함수 호출 시()")

    global goal
    global goalpos

    ac.send_goal(goal)
    ac.wait_for_result()
      
#목적지 설정(디스플레이) 시 실행되는 함수
#현재 위치 확인 후 초기 목적지 설정
# !!!현재 왼쪽부분 목적지만 도착한다고 가정
def msg_callback(msg):

    print("msg_callback()")
    global position, goalpos, goal

    goalpos = msg.data #pub으로부터 전달받은 목적지를 문자열로 position  저장

    check_robot_position() #현재위치 파악 

    if position =='desk': #현재위치가 '접수처'일때
        pt1()
       
    elif position =='center': #현재위치가 center이면
        CT()

    elif position == 'CT': #현재위치가 CT촬영실이면
        pt5()
                
    elif position =='pt1': #현재위치가 pt1이면
        pt2()
        
    elif position =='pt2': #현재위치가 pt2이면
        if goalpos=='3' or goalpos=='4' or goalpos=='5': #목적지가 우측이면
             Out_spot()
             robot_move()
        else: #목적지가 좌측이면
             pt3()

    elif position =='pt3': #현재위치가 pt3이면 -
        if goalpos=='1': #목적지가 응급의료센터이면
              center()
        else: #목적지가 CT촬영실/접수처/우측이면
              CT()
             
    elif position=='pt4': #현재위치가 pt4이면
          if goalpos=='1': #목적지가 응급의료센터이면
                center()
          else: #목적지가 CT 촬영실/접수처/우측이면
                CT()

    elif position=='pt5': #현재위치가 pt5이면
          pt6()

    elif position=='pt6': #현재위치가 pt6이면
          if goalpos=='0': #목적지가 접수처이면
                desk()
          elif goalpos=='1' or goalpos=='2': #목적지가 응급의료 센터이거나 CT촬영실이면
                pt1()

    elif position=='A' or position=='B': #현재위치가 A/B 구역이고
         if goalpos=='3': #목적지가 이비인후과이면
              #이비인후과()
              pass
         elif goalpos=='4': #목적지가 치과이면
              #치과()
              pass
         elif goalpos=='5': #목적지가 화장실이면
                #화장실()
                pass
         else: #목적지가 좌측이면
              In_spot()
    
    
    else:
          print("잘못된 설정")

#경로 주행 함수
def rule():
    #방향 조작을 위한 설정
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    move_cmd = Twist()
    start_time = rospy.get_time()
    rate = rospy.Rate(10)
    
    check_robot_position() #현재위치 파악

    if position=='pt1': #현재위치가 pt1이고
        pt2()
        print('pt2')
        robot_move()
        if goalpos=='1' or goalpos=='2': #목적지가 응급의료센터, CT촬영실이면
            pt3()
            print('pt3')
            robot_move()
            if goalpos=='1': #목적지가 응급의료센터이면
              center()
              print('center')
              robot_move()
            elif goalpos=='2': #목적지가 CT촬영실이면
              CT()
              print('CT')
              robot_move()
        else: #목적지가 우측이면
             Out_spot()
             robot_move()
             if goalpos=='3': #목적지가 이비인후과 이면
                  #이비인후과()
                  robot_move()
             elif goalpos=='4': #목적지가 치과이면
                  #치과()
                  robot_move()
             elif goalpos=='5': #목적지가 화장실이면
                  #화장실()
                  robot_move()         
  
    elif position=='pt2': #현재위치가 pt2이고
          if goal=='3' or goal=='4' or goal=='5': #목적지가 우측이면
               Out_spot()
               robot_move()
               if goalpos=='3': #목적지가 이비인후과 이면
                  #이비인후과()
                  robot_move()
               elif goalpos=='4': #목적지가 치과이면
                  #치과()
                  robot_move()
               elif goalpos=='5': #목적지가 화장실이면
                  #화장실()
                  robot_move()        

          else: #목적지가 좌측이면             
            pt3()
            robot_move()
            if goal=='1': #목적지가 응급의료센터이면
                    center()
                    robot_move()
            elif goal=='2': #목적지가 CT촬영실이면
                    CT()
                    robot_move()
            elif goal=='0': #목적지가 접수처이면
                    CT()
                    robot_move()
                    pt5()
                    robot_move()
                    pt6()
                    robot_move()
                    desk()
                    robot_move()

    elif position=='pt3': #현재위치가 pt3이고
        if goalpos=='1': #목적지가 응급의료센터이면
              center()
              robot_move()
        elif goalpos=='2': #목적지가 CT촬영실이면
              CT()
              robot_move()
        else: #목적지가 접수처이거나 우측이면
              CT()
              robot_move()
              pt5()
              robot_move()
              pt6()
              robot_move()
              if goalpos=='0': #목적지가 접수처이면
                desk()
                robot_move()    
              else: #목적지가 우측이면
                   pt1()
                   robot_move()
                   pt2()
                   robot_move()
                   Out_spot()
                   robot_move()
                   if goalpos=='3': #목적지가 이비인후과 이면
                    #이비인후과()
                    robot_move()
                   elif goalpos=='4': #목적지가 치과이면
                    #치과()
                    robot_move()
                   elif goalpos=='5': #목적지가 화장실이면
                    #화장실()
                    robot_move()         
    
    elif position=='pt5': #현재위치가 pt5이고
        pt6()
        robot_move()
        if goalpos=='0': #목적지가 접수처이면
                desk()
                robot_move()
        else: #목적지가 응급의료센터, 우측이면
             pt1()
             robot_move()
             pt2()
             robot_move()
             if goalpos=='1': #목적지가 응급의료센터이면
                pt3()
                robot_move()
                center()
                robot_move()
             else:
                Out_spot()
                robot_move()
                if goalpos=='3': #목적지가 이비인후과 이면
                  #이비인후과()
                  robot_move()
                elif goalpos=='4': #목적지가 치과이면
                  #치과()
                  robot_move()
                elif goalpos=='5': #목적지가 화장실이면
                  #화장실()
                  robot_move()        

    elif position=='pt6': #현재위치가 pt6이고
          if goal=='0': #목적지가 접수처이면
                desk()
                robot_move()
          else: #목적지가 응급의료센터/CT촬영실/우측이면
               pt1()
               robot_move()
               pt2()
               robot_move()
               if goal=='1': #목적지가 응급의료센터이면
                pt3()
                robot_move()
                center()
                robot_move()
               elif goal=='2': #목적지가 CT촬영실이면
                    pt3()
                    robot_move()
                    CT()
                    robot_move()
               else: #목적지가 우측이면
                    Out_spot()
                    robot_move()
                    if goalpos=='3': #목적지가 이비인후과 이면
                        #이비인후과()
                        robot_move()
                    elif goalpos=='4': #목적지가 치과이면
                        #치과()
                        robot_move()
                    elif goalpos=='5': #목적지가 화장실이면
                        #화장실()
                        robot_move()   

    elif position =='CT': #현재위치가 CT촬영실이고
        pt5()
        robot_move()
        pt6()
        robot_move()
        if goalpos=='0': #목적지가 접수처이면
              desk()
              robot_move()
        else: #목적지가 우측이면
             pt1()
             robot_move()
             pt2()
             robot_move()
             Out_spot()
             robot_move()
             if goalpos=='3': #목적지가 이비인후과 이면
                  #이비인후과()
                  robot_move()
             elif goalpos=='4': #목적지가 치과이면
                  #치과()
                  robot_move()
             elif goalpos=='5': #목적지가 화장실이면
                  #화장실()
                  robot_move()  

    elif position=='A': #현재위치가 outSpot 일때
            if goalpos=='3': #목적지가 이비인후과 이면
                  #이비인후과()
                  robot_move()
            elif goalpos=='4': #목적지가 치과이면
                  #치과()
                  robot_move()
            elif goalpos=='5': #목적지가 화장실이면
                  #화장실()
                  robot_move()  

##Inspot 범위 설정 필요
    elif position=='Inspot': #현재위치가 inspot일때
         pt3()
         robot_move()
         if goalpos=='1': #목적지가 응급의료센터이면
              center()
              robot_move()
         elif goalpos=='2': #목적지가 CT촬영실이면
              CT()
              robot_move()
         elif goalpos=='0': #목적지가 접수처이면
              CT()
              robot_move()
              pt5()
              robot_move()
              pt6()
              robot_move()
              desk()
              robot_move()    

#주행 시작 버튼 클릭 시 실행
#정해진 목적지로 이동 
def goal_move(msg):
    print("goal_move()")

    global goal
    global goalpos

    ac.send_goal(goal)
    ac.wait_for_result()

    if (position == 'pt4' and goalpos == '1') or (position == 'pt4' and goalpos == '2') or (position == 'pt3' and goalpos == '1') or (position == 'pt3' and goalpos == '2') or (position == 'pt6' and goalpos == '0') or (position == 'center' and goalpos == '2'):
        print('end')
    else:
        rule()


if __name__ == '__main__':
    try:
        # MoveBaseAction 서버가 준비될 때까지 대기
        ac.wait_for_server(rospy.Duration(5))

        # 목적지 설정 시 토픽 발송 노드
        rospy.Subscriber('/rockstar', String, msg_callback, queue_size=1)

        # 주행 시작 시 토픽 발송 노드 구독
        rospy.Subscriber('/start', String, goal_move, queue_size=1)


        # 노드가 종료될 때까지 실행
        rospy.spin()

    except rospy.ROSInterruptException:
        pass