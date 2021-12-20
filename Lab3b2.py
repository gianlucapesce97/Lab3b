import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rw3=np.zeros((1,1000))

counter1=[]
counter2x=[]
counter2y=[]

for i in range(1000):
    rr=np.random.choice([1,-1],1000).reshape(2,500)
    #print(rr.ndim) #Per controllare che sia effettivamente 2D
    #print(rr)
    
    rw2=np.cumsum(rr,axis=1,dtype=int)
    rw3=np.append(rw3,[rw2.flatten()],axis=0)
   
    
    print("Percorso X:")
    print(rw2[0,:])
    print("Percorso Y:")
    print(rw2[1,:])
    
    print('\n\n')
   
    counter2x.append(rw2[0,499])
    counter2y.append(rw2[1,499])
    
    
    checkx=np.sort(np.array([np.abs(np.min(rw2[0,:])),np.abs(np.max(rw2[0,:]))]))
    checky=np.sort(np.array([np.abs(np.min(rw2[1,:])),np.abs(np.max(rw2[1,:]))]))
    
    if(checkx[1]>checky[1]):
        print("Il percorso X ha la maggior distanza")
        counter1.append(checkx[1])
    else:
        print("Il percorso Y ha la maggior distanza")
        counter1.append(checky[1])
        
    step=np.arange(500)
    
    

    if(i==1):
        plt.plot(step,rw2[0,:],label="RW->x",marker=".",color='green')
        plt.plot(step,rw2[1,:],label="RW->y",marker=".",color='red')
        plt.legend()
        plt.savefig("RW2D")
        plt.close()   #Un altro modo è creare due oggetti separati con fig1=plt.figure....fig1.savefig(..)     e poi fig2=plt.figure...fig2.savefig(...)

        fig=plt.figure()
        ax1=fig.add_subplot(111,autoscale_on=False,xlim=(0,50),ylim=(np.min(rw2[0,:]),np.max(rw2[0,:])),label="rw->x")
        ax1.grid()
        ax1.set_xlabel("Steps")
        ax1.set_ylabel("Positions")
        ax2=fig.add_subplot(111,autoscale_on=False,xlim=(0,50),ylim=(np.min(rw2[1,:]),np.max(rw2[1,:])),label="rw->y")
        ax2.grid()
        #plt.legend()
        plt.title("RW2D")
        
        line1, *_ = ax1.plot(step[0],rw2[0,0],'--',lw=2)
        ball1, *_ = ax1.plot([0],[0],'o-',lw=2,color='red')

        line2, *_ = ax2.plot(step[0],rw2[1,0],'--',lw=2)
        ball2, *_ = ax2.plot([0],[0],'o-',lw=2,color='red')

        def update_plots1(i):
            line1.set_data(step[:i],rw2[0,:i])
            ball1.set_data(step[i],rw2[0,i])
            return line1,ball1

        def update_plots2(i):
            line2.set_data(step[:i],rw2[1,:i])
            ball2.set_data(step[i],rw2[1,i])
            return line2,ball2

        ani1=animation.FuncAnimation(fig,update_plots1,np.arange(1,len(step)),interval=50,blit=True,repeat=True)
        ani2=animation.FuncAnimation(fig,update_plots2,np.arange(1,len(step)),interval=50,blit=True,repeat=True)
        #ani1.save("RW2Dx.gif",writer='imagemagick',fps=30)
        #ani2.save("RW2Dy.gif",writer='imagemagick',fps=30)
        plt.close()


       
        #n,bins,patches=plt.hist(rw2.flatten(),bins=2*step,facecolor="magenta",label="All Distances covered")
        #plt.xlabel("Position on Z")
        #plt.ylabel("Frequency")
        #plt.xlim(-50,50)
        #plt.legend()
        #plt.savefig("IstogrammaRWAllDistances")
        #plt.close()

   
    
        
    


n,bins,patches=plt.hist(counter2x,bins=len(set(counter2x)),facecolor="red",label="Final Distances x")
n,bins,patches=plt.hist(counter2y,bins=len(set(counter2y)),facecolor="green",label="Final Distances y")
plt.xlabel("Position on Z")
plt.ylabel("Frequency")
plt.xlim(-1000,1000)
plt.legend()
plt.savefig("IstogrammaRWFinalDistances")
plt.close()

n,bins,patches=plt.hist(counter1,bins=len(set(counter1)),facecolor="blue",label="Max Distances xy")
plt.xlabel("Position on Z")
plt.ylabel("Frequency")
plt.xlim(-1000,1000)
plt.legend()
plt.savefig("IstogrammaRWMaxDistances")
plt.close()


print(rw3)
for k in range(1000):
    plt.plot(rw3[k,:])
plt.grid()
plt.xlabel('Step')
plt.ylabel("Positions")
plt.xlim(-10,500)
plt.ylim(-90,90)
plt.savefig("AllDistances")
plt.close()





