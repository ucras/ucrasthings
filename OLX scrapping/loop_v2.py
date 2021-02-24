import time
import subprocess
import csv
import win10toast

toaster =  win10toast.ToastNotifier()

infinite = 0
loops = 0

gpu_list = []
gpu_comparison = ['test']

# TO DO: FUNCTION THAT READ THE CSV FILE AND ---COMPARES THE VALUES WITH KEY WORDS---
def name_checker():
    global gpu_list
    global gpu_comparison
    gpu_comparison.clear()
    # JUST TO SKIP WHEN THERE WAS NO CHANGE
    with open("gpu.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for lines in csv_reader:
                gpu_comparison.append(lines[0])

    if gpu_list != gpu_comparison:
        print("OH LOOK THERE WAS A CHANGE HERE !!!!!!!!!!!!!!!!!!!!!!")
        gpu_list.clear()    # CLEAR THE LIST TO UPDATE IT AFTERWARDS
        with open("gpu.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for lines in csv_reader:
                gpu_list.append(lines[0])
    
        #print(gpu_list)

        toaster.show_toast('OLX', 'NOVA GPU, VAI MAS É VER QUAL É', duration=15)

    else:
        print('NO CHANGE AT ALL')


# runs the file to update the excel with all the gpus available
while infinite < 1:
    exec(open("olxscrapping.py").read())
    loops += 1
    print('Checks: ' + str(loops))

    name_checker()
    time.sleep(60)




