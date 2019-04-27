import os
import sys
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
def main(argv):
    inputdir = argv[0]
    epochs = int(argv[1])
    xdim = int(argv[2])
    ydim = int(argv[3])
    feature = int(argv[4])

    outputdir = inputdir + '/feature' + str(feature) + '/'
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    for i in np.arange(1,epochs+1):
        print i
        wts = np.loadtxt(inputdir + "/output."+str(i)+".wts",comments='%')
        wts = wts.reshape([xdim,ydim,wts.shape[1]])
        feat = wts[:,:,feature]
        img = ndimage.gaussian_filter(feat,sigma=(1))
        plt.matshow(img, vmin =0.3, vmax=1)
        #plt.matshow(img)
        plt.axis('off')
        plt.colorbar()
        plt.savefig(outputdir + "/feat."+str(i).zfill(3)+".png", bbox_inches='tight')
        plt.close()


if __name__ == "__main__":
    main(sys.argv[1:])

