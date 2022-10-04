#input: simpoint.bb.gz of each benchmark generated by gem5 runing on each benchmark with exe and input
#output: simpoints and weights

import os
from pathlib import Path

simpoint_bin = "/proj/snic2021-5-411/users/x_qisha/proj/simpoint/Simpoint3.2/bin/simpoint"
input_dir = "/proj/snic2021-5-411/users/x_qisha/data/gem5-results-2017-20220913-simpoint/512MB/"
output_dir = "/proj/snic2021-5-411/users/x_qisha/data/gem5-results-2017-20220913-simpoint/512MB"

def generate_simpoint_weight(input_dir,output_dir):
    for root, dirs, files in os.walk(input_dir):
        for benchmark in dirs:
            print ("benchmark: ", benchmark)
            in_file= os.path.join(root,benchmark,"simpoint.bb.gz")
            in_file_exists = Path(in_file)

            out_dir = os.path.join(output_dir,benchmark)

            if not os.path.isdir(out_dir):
                os.makedirs(out_dir)

            if in_file_exists.is_file():
                simpoints = os.path.join(out_dir,"simpoints")
                weights = os.path.join(out_dir,"weights")

                print (simpoints)
                print (weights)

                command = simpoint_bin + " -maxK 5 " + " -loadFVFile " + in_file\
                         + " -inputVectorsGzipped " + " -saveSimpoints "\
                         + simpoints + " -saveSimpointWeights " + weights

                print ("cmd: ",command);
                result = os.system(command)
            
generate_simpoint_weight(input_dir,output_dir)
