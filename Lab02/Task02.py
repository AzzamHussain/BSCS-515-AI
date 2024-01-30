# (II)In a company ,worker efficiency is determined on the basis of the time required for a worker 
# to complete a particular job.If the time taken by the worker is between 2-3 hours then the worker 
# is said to be highly efficient. If the time required by the worker is between 3-4hours,then the worker 
# is ordered to improve speed. If the time taken is between 4-5 hours ,the worker is given training to 
# improve his speed ,and if the time taken by the worker is more than 5 hours ,then the worker haas 
# to leave the company, If the time taken by the worker is input through the keyboard,find the 
# efficiency of the worker
workerSpeed=int(input("Enter worker speed:"))
if workerSpeed>=2 and workerSpeed<=3:
    print("highly efficient")
elif workerSpeed>=4 and workerSpeed<=5:
    print("improve speed")
elif workerSpeed>=4 and workerSpeed<=5:
    print("Required training to improve speed")
else:
    print("fired")