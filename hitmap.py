import os
import sys
import numpy as np
import scipy.ndimage as ndimage
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
def main(argv):
    inputdir = argv[0]
    epochs = int(argv[1])
    xdim = int(argv[2])
    ydim = int(argv[3])

    outputdir = inputdir + '/figs/'
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    epochstd = []
    for i in np.arange(1,epochs+1):
        print i
#    data = np.loadtxt("/Shared/bdagroup5/data/test.txt")
#    wts = np.loadtxt("output."+str(i)+".wts",comments='%')
#    wts = wts.reshape([50,50,221])
        bm = np.loadtxt(inputdir + "/output."+str(i)+".bm",comments='%')
        hitmap = np.zeros([xdim,ydim])
        numpts = bm.shape[0]
        pts = np.arange(0,numpts)
        total = 0
        for pt in pts:
            bmu = bm[pt]
            hitmap[int(bmu[1]),int(bmu[2])] += 1
        img = ndimage.gaussian_filter(hitmap,sigma=(1.5))
        plt.matshow(img, vmin =0, vmax=1000)
        plt.axis('off')
        plt.colorbar()
        plt.savefig(outputdir + "/hitmap."+str(i).zfill(3)+".png", bbox_inches='tight')
        plt.close()
        epochstd.append(np.std(hitmap.flatten()))
    plt.plot(epochstd)
    plt.ylim(0,3000)
    plt.xlabel("Epoch")
    plt.ylabel("Standard Deviation of Hitmap")
    plt.title("Hitmap Standard Deviation  vs Epoch Number")
    plt.savefig(outputdir+"/epochstd.png")

if __name__ == "__main__":
    main(sys.argv[1:])

