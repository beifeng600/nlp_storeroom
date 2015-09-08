#coding=utf-8
#! python
#### 默认编码为UTF-8，若不是，请修改
#### Author: beifeng600

import sys;
import re;
import os;
import codecs;

def handle_file(input_path, output_path):
    if not os.path.exists(input_path):
        print "Error, "+input_path+" not exists!"
        return

    fpw = open(output_path, 'w')
    
    lineNum = 0
    with file(input_path) as f_obj:
        for line in f_obj.xreadlines():
            lineNum += 1
            #print str(lineNum)
            try:
                new_line = line[:-1].decode('utf-8')
            except UnicodeDecodeError, e:
                print e
                continue

            if lineNum == 1:
                new_line = new_line.lstrip(unicode(codecs.BOM_UTF8, "utf8"))

            #if not new_line:
            #    continue

            try:
                fpw.write(new_line.encode('utf-8')+"\n")
            except UnicodeEncodeError, e:
                print e
                continue
    fpw.close()

        
def handle_dir(input_path, output_path):
    if not os.path.exists(input_path):
        print "Error, "+input_path+" not exists!"
        return
    
    if not os.path.isdir(input_path):
        print "Error, "+input_path+" is not directory!"
        return
    
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    file_list = os.listdir(input_path)
    for file_name in file_list:
        if os.path.isdir(input_path+"/"+file_name):
            handle_dir(input_path+"/"+file_name, output_path+"/"+file_name)
        else:
            handle_file(input_path+"/"+file_name, output_path+"/"+file_name)
    
    print "Complete "+input_path+" !"


def handle(input_path, output_path):

    if os.path.isdir(input_path):
        handle_dir(input_path, output_path)
    else:
        handle_file(input_path, output_path)


if __name__ == '__main__':
    if len(sys.argv)!=3:
        print "Usage: python %s input_path, output_path" % sys.argv[0]

    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        handle(input_path, output_path)

