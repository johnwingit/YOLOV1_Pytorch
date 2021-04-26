"""
time:2021.4.26
author:Jylyy

"""

import argparse
import torch

class Args(object):
    """
    设置命令行参数的接口
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def set_train_args(self):
        """options for train"""
        self.parser.add_argument("--batch_size", type=int, default=1)
        self.parser.add_argument("--lr", type=float, default=0.0001, help="learning rate")
        self.parser.add_argument("--weight_decay", type=float, default=1e-4)
        self.parser.add_argument("--epoch", type=int, default=60, help="number of end epoch")
        self.parser.add_argument("--start_epoch", type=int, default=1, help="number of start epoch")
        self.parser.add_argument("--use_GPU", action="store_true", help="identify whether to use gpu")
        self.parser.add_argument("--GPU_id", type=int, default=None, help="device id")
        self.parser.add_argument("--dataset_dir", type=str, default=r"D:\wangpan\VOC\VOCdevkit\VOC2012\voc2012_forYolov1")
        self.parser.add_argument("--checkpoints_dir", type=str, default="./checkpoints")
        self.parser.add_argument("--print_freq", type=int, default=10,
                            help="print training information frequency (per n iteration)")
        self.parser.add_argument("--save_freq", type=int, default=20, help="save model frequency (per n epoch)")
        self.parser.add_argument("--num_workers", type=int, default=0, help="use n threads to read data")
        self.parser.add_argument("--pretrain", type=str, default=r"C:\Users\Owen\Desktop\YOLOv1-from-scratch-master\checkpoints\epoch60.tar", help="pretrain model path")
        #self.parser.add_argument("--pretrain", type=str,default=None)
        self.parser.add_argument("--random_seed", type=int, default=0, help="random seed for split dataset")

        self.opts = self.parser.parse_args()

        if torch.cuda.is_available():
            self.opts.use_GPU = False
            self.opts.GPU_id = torch.cuda.current_device()
            print("use GPU %d to train." % (self.opts.GPU_id))
        else:
            print("use CPU to train.")

    def set_test_args(self):
        """options for inference"""
        self.parser.add_argument("--batch_size", type=int, default=1)
        self.parser.add_argument("--use_GPU", action="store_true", help="identify whether to use gpu")
        self.parser.add_argument("--GPU_id", type=int, default=None, help="device id")
        self.parser.add_argument("--dataset_dir", type=str, default=r"D:\wangpan\VOC\VOCdevkit\VOC2012\voc2012_forYolov1\testimg")
        self.parser.add_argument("--weight_path", type=str,
                             default=r"checkpoints\epoch60.tar",
                             help="load path for model weight")
        self.opts = self.parser.parse_args()
        if torch.cuda.is_available():
            self.opts.use_GPU = False
            self.opts.GPU_id = torch.cuda.current_device()
            print("use GPU %d to train." % (self.opts.GPU_id))
        else:
            print("use CPU to train.")

    def get_opts(self):
        return self.opts