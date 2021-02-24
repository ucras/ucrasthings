import time
import subprocess
import csv

infinite = 0
loops = 0

gpu_list = []

# TO DO: FUNCTION THAT READ THE CSV FILE AND ---COMPARES THE VALUES WITH KEY WORDS---
def name_checker():
    global gpu_list
    gpu_olx = []
    with open("gpu.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            gpu_list.append(lines[0]) 
    
    if gpu_olx != gpu_list:
        gpu_olx = gpu_list
        
        # FOR TO CHECK THE EXISTANCE OF A GOOD GPU
        for gpu in gpu_list:
            if 'RTX' in gpu:
                print("YAAAAAAAAAY")    # this way I can see some improvement

    print(gpu_list[1:])   #prints the updated gpu list



# runs the file to update the excel with all the gpus available
while infinite < 1:
    exec(open("olxscrapping.py").read())
    loops += 1
    print('Checks: ' + str(loops))

    name_checker()



    time.sleep(15)




