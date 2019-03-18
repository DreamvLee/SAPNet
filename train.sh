#!/usr/bin/env sh

CURRENT_DATE=$(date +%Y-%m-%d)

../../.build_release/tools/caffe.bin train -solver solver.prototxt -weights se_resnet_50_v1.caffemodel 2>&1 |tee train${CURRENT_DATE}.txt &