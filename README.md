# SAPNet

This is an open-source project for the aesthetic evaluation of images based on the deep learning-caffe framework, which we completed in the [Victory team of Besti](http://kislab.besti.edu.cn/victory/).


The aesthetic quality assessment of image is a challenging work in computer vision field. The recent research work used the deep convolutional neural network to evaluate the aesthetic quality of images. However, the score of image data sets has a strongly normal distribution, which makes the training of neural network easy to be over-fitting. In addition, traditional deep learning methods usually pre-process images, which destroy the original aesthetic features of the picture, so that the network can only learn some superficial aesthetic features. This paper presents a new data set what images distributed evenly for aesthetics (IDEA). This data set has less statistical characteristics, which is helpful for the neural network to learn the deeper features. We propose a new spatial aggregation perception neural network architecture which can control channel weights automatically. Our experiments in different data sets can prove the advantages and effectiveness of our method.

**The IDEA dataset**

To create a more balanced set of aesthetic images, we collected several images and score tags from the professional photography website: dpchallenge and Flickr. Website’s scores are ranging from 0 to 9, we selected 1000 images for each segment as far as possible (Flickr’s label come from AADB). 

Specifically, we climbed all the pictures numbered below 800 thousand on dpchallenge which has 330 thousand pictures and we selected 1000 pictures per score. The method of selection is chosen according to the number of voters in the website, because the higher the voting is, the higher the reference value is. Through this method, we get 7961 pictures, mainly missing 1 and 2 points and 9 points, so we randomly select and supplement the images from the AADB data set, and finally form a complete set of data. Finally, our data set which is almost balance distributed, is named as the IDEA dataset. The IDEA data set has 9191 images, of which the number of 9 points number are 191 and the rest are 1,000. In the training, 8191 pictures were used for the training set and randomly selected 1000 images for testing.

**The way of test**

please use caffe test tools to test accuracy. The file test.py can help you quickly.

**Our paper**

Jin X, Wu L, Zhao G, et al. IDEA: A new dataset for image aesthetic scoring[J]. Multimedia Tools and Applications, 2018: 1-15.

If you find our model/method/dataset useful, please cite our work:

*************************************************************************************

@article{jin2018idea,

  title={IDEA: A new dataset for image aesthetic scoring},
  
  author={Jin, Xin and Wu, Le and Zhao, Geng and Zhou, Xinghui and Zhang, Xiaokun and Li, Xiaodong},
  
  journal={Multimedia Tools and Applications},
  
  pages={1--15},
  
  year={2018},
  
  publisher={Springer}
  
}

***************************************************************************************


Latest edit

Mar 18, 2019
