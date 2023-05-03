#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import rospy as rp
import serial
from imu_driver.msg import imu_msg 



def parseIMU(data):

    sdata=data.decode('utf-8').split(",")
    #sdata=sdata0.split(",")
    if "VNYMR" in sdata[0]:
        # print(sdata)
        
        
        a_x = float(sdata[7])
        a_y = float(sdata[8])
        a_z = float(sdata[9])
        g_x = float(sdata[10])
        g_y = float(sdata[11])
        g_z = float(sdata[12][:-6])
        m_x = float(sdata[4])
        m_y = float(sdata[5])
        m_z = float(sdata[6])
        r = float(sdata[3])
        p = float(sdata[2])
        y = float(sdata[1])
          
        quat_data=euler_to_quaternion(y,p,r)
        qx=float(quat_data[0])
        qy=float(quat_data[1])
        qz=float(quat_data[2])
        qw=float(quat_data[3])
            
        sensorMsg_imu(a_x,a_y,a_z,g_x,g_y,g_z,m_x,m_y,m_z,qx,qy,qz,qw,sdata)
        
    else:
        pass    

def euler_to_quaternion(y,p,r):
    (yaw,pitch,roll) = (y,p,r)
    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    return [qx, qy, qz, qw]

def sys_time(self):
    time=str(self).split(".")
    secs= int(time[0])
    nsecs = int(time[1])    
    
    # frac,whole = math.modf(self)
    # secs=int(whole)
    # #nsecs=int(str(frac).split('.')[1])
    # nsecs=0
    return(secs,nsecs)



def sensorMsg_imu(a_x,a_y,a_z,g_x,g_y,g_z,m_x,m_y,m_z,qx,qy,qz,qw,sdata):
    pub =rp.Publisher('imu',imu_msg,queue_size=200)
   

    pub_data=imu_msg()
    
    secs,nsecs = sys_time(rp.get_time())
    pub_data.Header.stamp.secs=secs
    pub_data.Header.stamp.nsecs=nsecs
    pub_data.IMU.header.stamp.secs= secs
    pub_data.IMU.header.stamp.nsecs= nsecs
    pub_data.IMU.header.frame_id="IMU1_Frame"
    pub_data.IMU.orientation.x= qx 
    pub_data.IMU.orientation.y= qy 
    pub_data.IMU.orientation.z= qz 
    pub_data.IMU.orientation.w= qw     
    pub_data.IMU.angular_velocity.x=g_x
    pub_data.IMU.angular_velocity.y=g_y
    pub_data.IMU.angular_velocity.z=g_z
    pub_data.IMU.linear_acceleration.x=a_x
    pub_data.IMU.linear_acceleration.y=a_y
    pub_data.IMU.linear_acceleration.z=a_z
    pub_data.MagField.header.stamp.secs= secs
    pub_data.MagField.header.stamp.nsecs= nsecs
    pub_data.MagField.header.frame_id="IMU1_Frame"
    pub_data.MagField.magnetic_field.x=m_x
    pub_data.MagField.magnetic_field.y=m_y
    pub_data.MagField.magnetic_field.z=m_z
    pub_data.rawdata= str(sdata)
    

    pub.publish(pub_data)
    rp.loginfo(pub_data)
    #rp.sleep(1)
    rp.Rate(40)
# def read_serial_port():
    
#      data = ser.readline()
#      parseIMU(data)
       
        

port = rp.get_param("/driver/port")
rp.init_node("sensorMsg_imu")
print ("Receiving IMU data")
x= "$VNWRG,07,40*XX"
b=x.encode()

ser = serial.Serial(port,baudrate=115200,timeout=2)
ser.write(b)
data=[]

#a= ser.write(b)
#schedule.every(0.025).seconds.do(read_serial_port) 


while not rp.is_shutdown():
    #try:
        data = ser.readline()
        parseIMU(data)
        
        #schedule.run_pending()
        
    #except Exception as e:
     #   print(e)    