import bagpy
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
import math

b = bagreader('/home/hrithik/bagfiles/10_mins_stationary.bag')
b.topic_table
data = b.message_by_topic('/imu')
print("File saved:{}".format(data))
df_imu=pd.read_csv(data)
or_x = df_imu.iloc[:,9]
or_y = df_imu.iloc[:,10]
or_z = df_imu.iloc[:,11]
or_w = df_imu.iloc[:,12]
len(or_x)
roll =[]
for i in range(0,len(or_x)):
    t0 = +2.0 * (or_w[i]*or_x[i] + or_y[i]*or_z[i])
    t1 = +1.0 -2.0 *(or_x[i]*or_x[i]+or_y[i]*or_y[i])
    roll.append(math.degrees(math.atan2(t0,t1)))
roll 
pitch =[]
for i in range(0,len(or_x)):
     t2 = +2.0 * (or_w[i] * or_y[i] - or_z[i] * or_x[i])
     t2 = +1.0 if t2 > +1.0 else t2
     t2 = -1.0 if t2 < -1.0 else t2
     pitch.append(math.degrees(math.asin(t2)))
pitch    
yaw=[]
for i in range(0,len(or_x)):
     t3 = +2.0 * (or_w[i] * or_z[i] + or_x[i] * or_y[i])
     t4 = +1.0 - 2.0 * (or_y[i] * or_y[i] + or_z[i] * or_z[i])
     yaw.append(math.degrees(math.atan2(t3, t4)))      
yaw 
df_imu["Roll"] = roll
df_imu["Pitch"] = pitch
df_imu["Yaw"] = yaw
df_imu.to_csv(data,index=False)

fig, ax = bagpy.create_fig()
ax[0].scatter(x = 'Time', y = 'IMU.angular_velocity.x', data  = df_imu, s= 1, label = 'angular_velocity.x')
ax[0].set_ylabel('angular_velocity.x(rad/sec)')
ax[0].set_xlabel('Time(sec)')
ax[0].set_title('Angular Velocity  vs  Time')
fig, ay = bagpy.create_fig()
ay[0].scatter(x = 'Time', y = 'IMU.angular_velocity.y', data  = df_imu, s= 1, label = 'angular_velocity.y')
ay[0].set_ylabel('angular_velocity.y(rad/sec)')
ay[0].set_xlabel('Time(sec)')
ay[0].set_title('Angular Velocity  vs  Time')
fig, az = bagpy.create_fig()
az[0].scatter(x = 'Time', y = 'IMU.angular_velocity.z', data  = df_imu, s= 1, label = 'angular_velocity.z')
az[0].set_ylabel('angular_velocity.z(rad/sec)')
az[0].set_xlabel('Time(sec)')
az[0].set_title('Angular Velocity  vs  Time')
fig, lx = bagpy.create_fig()
lx[0].scatter(x = 'Time', y = 'IMU.linear_acceleration.x', data  = df_imu, s= 1, label = 'linear_acceleration.x')
lx[0].set_ylabel('linear_acceleration.x(m/s^2)')
lx[0].set_xlabel('Time(sec)')
lx[0].set_title('Linear Velocity  vs Time')
fig, ly = bagpy.create_fig()
ly[0].scatter(x = 'Time', y = 'IMU.linear_acceleration.y', data  = df_imu, s= 1, label = 'linear_acceleration.y')
ly[0].set_ylabel('linear_acceleration.y(m/s^2)')
ly[0].set_xlabel('Time(sec)')
ly[0].set_title('Linear Velocity  vs Time')
fig, lz = bagpy.create_fig()
lz[0].scatter(x = 'Time', y = 'IMU.linear_acceleration.z', data  = df_imu, s= 1, label = 'linear_acceleration.z')
lz[0].set_ylabel('linear_acceleration.z(m/s^2)')
lz[0].set_xlabel('Time(sec)')
lz[0].set_title('Linear Velocity  vs Time')
fig, mx = bagpy.create_fig()
mx[0].scatter(x = 'Time', y = 'MagField.magnetic_field.x', data  = df_imu, s= 1, label = 'magneticfield.x')
mx[0].set_ylabel('magnetic_field.x(gauss)')
mx[0].set_xlabel('Time(sec)')
mx[0].set_title('Magnetic Field  vs Time')
fig, my = bagpy.create_fig()
my[0].scatter(x = 'Time', y = 'MagField.magnetic_field.y', data  = df_imu, s= 1, label = 'magneticfield.y')
my[0].set_ylabel('magnetic_field.y(gauss)')
my[0].set_xlabel('Time(sec)')
my[0].set_title('Magnetic Field  vs Time')
fig, mz = bagpy.create_fig()
mz[0].scatter(x = 'Time', y = 'MagField.magnetic_field.z', data  = df_imu, s= 1, label = 'magneticfield.z')
mz[0].set_ylabel('magnetic_field.z(gauss)')
mz[0].set_xlabel('Time(sec)')
mz[0].set_title('Magnetic Field  vs Time')
fig, r = bagpy.create_fig()
r[0].scatter(x = 'Time', y = roll, data  = df_imu, s= 1, label = 'roll')
r[0].set_ylabel('roll(degrees)')
r[0].set_xlabel('Time(sec)')
r[0].set_title('Roll  vs  Time')
fig, p = bagpy.create_fig()
p[0].scatter(x = 'Time', y = 'Pitch', data  = df_imu, s= 1, label = 'pitch')
p[0].set_ylabel('pitch(degrees)')
p[0].set_xlabel('Time(sec)')
p[0].set_title('Pitch  vs  Time')
fig, y = bagpy.create_fig()
y[0].scatter(x = 'Time', y = 'Yaw', data  = df_imu, s= 1, label = 'yaw')
y[0].set_ylabel('yaw(degrees)')
y[0].set_xlabel('Time(sec)')
y[0].set_title('Yaw  vs  Time')

df_imu.hist("Roll")
plt.xlabel('roll(degrees)')
plt.ylabel('frequency')
df_imu.hist("Pitch")
plt.xlabel('pitch(degrees)')
plt.ylabel('frequency')
df_imu.hist("Yaw")
plt.xlabel('yaw(degrees)')
plt.ylabel('frequency')
df_imu.hist("IMU.angular_velocity.x")
plt.xlabel('angular_velocity_x(rad/sec)')
plt.ylabel('frequency')
df_imu.hist("IMU.angular_velocity.y")
plt.xlabel('angular_velocity_y(rad/sec)')
plt.ylabel('frequency')
df_imu.hist("IMU.angular_velocity.z")
plt.xlabel('angular_velocity_z(rad/sec)')
plt.ylabel('frequency')
df_imu.hist("IMU.linear_acceleration.x")
plt.xlabel('linear_velocity_x(m/s^2)')
plt.ylabel('frequency')
df_imu.hist("IMU.linear_acceleration.y")
plt.xlabel('linear_velocity_y(m/s^2)')
plt.ylabel('frequency')
df_imu.hist("IMU.linear_acceleration.z")
plt.xlabel('linear_velocity_z(m/s^2)')
plt.ylabel('frequency')
df_imu.hist("MagField.magnetic_field.x")
plt.xlabel('magnetic field_x(gauss)')
plt.ylabel('frequency')
df_imu.hist("MagField.magnetic_field.y")
plt.xlabel('magnetic field_y(gauss)')
plt.ylabel('frequency')
df_imu.hist("MagField.magnetic_field.z")
plt.xlabel('magnetic field_z(gauss)')
plt.ylabel('frequency')

plt.show()




