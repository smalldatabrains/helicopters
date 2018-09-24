import numpy as np
import cv2
import os

root_dir="downloads/"

def size_table():
	sizes_list=[]
	for d in os.listdir(root_dir):
		for image in os.listdir(root_dir+d):
			print(root_dir+d+'/'+image)
			data=cv2.imread(root_dir+d+'/'+image)
			error_count=0
			try:
				height,width=data.shape[:2]
				print(height," | ",width)
				sizes_list.append([image,height,width])
			except:
				print("Image size cannot be read, image deleted")
				error_count+=1
				# os.remove(root_dir+d+'/'+image)
				print(error_count, " images were deleted")
	np.save("sizes.npy",np.array(sizes_list))

if __name__ ==  '__main__':
	size_table()
