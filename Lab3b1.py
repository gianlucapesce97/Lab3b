import numpy as np
import random 
import matplotlib.pyplot as plt
import matplotlib.animation as animation



rr=np.random.choice([1,-1],999)
rr=np.insert(rr,0,0)
rw=np.cumsum(rr)
print(rw)


print("Max assoluto:",(np.max(np.cumsum(rr))),"\t#Step per il 1° Max:",np.argmax(np.cumsum(rr)),"\nMin assoluto:",np.min(np.cumsum(rr)),"\t#Step per il 1° min:",np.argmin(np.cumsum(rr)))
#print(np.min(np.cumsum(rr)))

step=np.arange(1000)

print("Steps ai quali il RW è uguale a 20: ",np.where(rw==20))

plt.plot(step,rw,label="RW1D",marker=".")
plt.savefig("RW1D")


fig=plt.figure()
ax=fig.add_subplot(111,autoscale_on=False,xlim=(0,1000),ylim=(np.min(rw),np.max(rw)))
ax.grid()
ax.set_xlabel("Steps")
ax.set_ylabel("Positions")
plt.title("RW1D")

line, *_ = ax.plot(step[0],rw[0],'--',lw=2)
ball, *_ = ax.plot([0],[0],'o-',lw=2,color='red')

def update_plots(i):
    line.set_data(step[:i],rw[:i])
    ball.set_data(step[i],rw[i])
    return line,ball

ani=animation.FuncAnimation(fig,update_plots,np.arange(1,len(step)),interval=50,blit=True,repeat=True)


ani.save("RW1D.gif",writer='imagemagick',fps=30)


