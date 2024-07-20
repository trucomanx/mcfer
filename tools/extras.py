#!/usr/bin/python3


#import sys
import os
import json
import csv

'''
git clone https://github.com/trucomanx/WorkingWithFiles.git
cd WorkingWithFiles/src
python3 setup.py sdist
pip3 install dist/WorkingWithFiles-*.tar.gz
cd ../../
rm -f -r WorkingWithFiles
'''
import WorkingWithFiles.WorkingWithFiles as wf


def generate_dict(in_dict, out_filepath, dir_base=None, format_list=[".png"], header=['filename', 'label']):

    info=dict();
    
    with open(out_filepath, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
    
        writer.writerow(header)
        
        for label in in_dict:
            info[label]=0;
            
            for dirpath in in_dict[label]:
                file_list = wf.get_all_files_in_dir(dirpath,
                                                    formats_search=format_list,
                                                    is_relative=True);
                
                info[label]=info[label]+len(file_list);
                
                for filepath in file_list:
                    if isinstance(dir_base, str):
                        absolute_path = os.path.join(dirpath,filepath);
                        relative_path = os.path.relpath(absolute_path, dir_base)
                        oh_list=[relative_path,label];
                    else:
                        oh_list=[os.path.join(dirpath,filepath),label];
                    writer.writerow(oh_list);

    with open(out_filepath+".json", 'w') as json_file:
        json.dump(info, json_file, indent=4)
    
    Total=0;
    for label in info:
        Total=Total+info[label];
    print('Total:',Total)
    
    return info;
