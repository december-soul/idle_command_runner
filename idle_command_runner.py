import xprintidle
import subprocess
import time

CMD = '<YOUR COMMAND>'

running = False
TIMEOUT = 1000 * 60 * 5 # 5 min
#proc = subprocess.Popen("echo") # with this i could use proc.poll() to check if proc is running, not need the running var
proc = None


count = 0
while True:
        count += 1
        if count > 10:
                print("{:8} of {} sec of inactivity befor start command".format(int(xprintidle.idle_time()/1000), int(TIMEOUT/1000)))
                count = 0
        if xprintidle.idle_time() > TIMEOUT and running == False:
                running = True
                print("start command")
                proc = subprocess.Popen(CMD.split(), stdout=subprocess.PIPE)
                print(proc.pid)
        elif xprintidle.idle_time() < 1000 and running == True:
                running = False
                proc.terminate()
                print("stop command")

        time.sleep(1)
