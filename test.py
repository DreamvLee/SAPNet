import sys
caffe_root='../../../caffe-multlabel/'
sys.path.insert(0,caffe_root+'python')
import caffe
import numpy as np


model_file = 'sap_resnet_iter_12000.caffemodel'
net_file = 'SAP_ResNet_50_deploy.prototxt'
caffe.set_mode_gpu()
net = caffe.Net(net_file, model_file, caffe.TEST)
transformer = caffe.io.Transformer({'data':net.blobs['data'].data.shape})
#transformer.set_mean('data', np.load('../../python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1))
transformer.set_mean('data', np.array([97.83,106.76,109.48]))
transformer.set_transpose('data',(2,0,1))
transformer.set_raw_scale('data',255)
transformer.set_channel_swap('data',(2,1,0))
#net.blobs['data'].reshape(1,3,225,225)
imglist = open("/home/wule/Datasets/IDEA/val/val.txt","r")
img_path = imglist.readlines()
with open("result.txt","a+") as f:
    for i in img_path:
        ii = i.replace("\n","")
        a = ii.split(" ")
        img = caffe.io.load_image('/home/wule/Datasets/IDEA/val/images/'+a[0])
        net.blobs['data'].data[...] = transformer.preprocess('data',img)
        out = net.forward()
        out1 = out['sigmoid_wl'][0]
        error = ''
        error += a[0] + ' '
        error += '%.3f\n' %out1[0]
        f.write(error)
