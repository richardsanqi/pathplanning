#coding=utf-8
import cv2
import motion_roadmap as mr
import numpy as np

# 图像路径，将 USER_NAME 改为计算机用户名
image_path = "/home/lipi/PathPlanning/motion_planning/map_1.bmp"
# 利用cv2读取图像
img = cv2.imread(image_path)
# 当图像过大时，调整尺寸。建议对PRM或RRT: 500*500; 对人工势场法：100*100
img = cv2.resize(img,(500,500))

demo_1 = mr.MotionRoadmap(img)
# 设置起点和终点，为numpy.mat格式
# demo_1.point_start = np.mat([5, 5])
demo_1.point_goal = np.mat([495, 400])
demo_1.rrt_planning()
cv2.waitKey(0)
