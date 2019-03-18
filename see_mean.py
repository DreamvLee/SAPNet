import sys
import caffe
import numpy as np

np.set_printoptions(threshold='nan')

MEAN_FILE = 'mean.binaryproto'
means_txt = "means.txt"
mf = open(means_txt, 'w')


mean_blob = caffe.proto.caffe_pb2.BlobProto()
mean_blob.ParseFromString(open(MEAN_FILE, 'rb').read())

arr = np.array( caffe.io.blobproto_to_array(mean_blob) )
mean_npy=arr[0]
print mean_npy
print mean_npy.mean(axis=1).mean(axis=1)
#mean_npy = caffe.io.blobproto_to_array(mean_blob)

#mean_npy.shape = (-1, 1)

#for m in mean_npy:

#

#    mf.write("%ff," % m)

#

#mf.close