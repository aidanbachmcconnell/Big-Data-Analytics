featuresmap.py                                                                                      000644  000765  000024  00000001672 13023325644 015402  0                                                                                                    ustar 00sarahgerard                     staff                           000000  000000                                                                                                                                                                         import os
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

                                                                      hdf5_getters.py                                                                                     000644  000765  000024  00000052302 13023325644 015445  0                                                                                                    ustar 00sarahgerard                     staff                           000000  000000                                                                                                                                                                         """
Thierry Bertin-Mahieux (2010) Columbia University
tb2332@columbia.edu


This code contains a set of getters functions to access the fields
from an HDF5 song file (regular file with one song or
aggregate / summary file with many songs)

This is part of the Million Song Dataset project from
LabROSA (Columbia University) and The Echo Nest.


Copyright 2010, Thierry Bertin-Mahieux

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import tables


def open_h5_file_read(h5filename):
    """
    Open an existing H5 in read mode.
    Same function as in hdf5_utils, here so we avoid one import
    """
    return tables.openFile(h5filename, mode='r')


def get_num_songs(h5):
    """
    Return the number of songs contained in this h5 file, i.e. the number of rows
    for all basic informations like name, artist, ...
    """
    return h5.root.metadata.songs.nrows

def get_artist_familiarity(h5,songidx=0):
    """
    Get artist familiarity from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_familiarity[songidx]

def get_artist_hotttnesss(h5,songidx=0):
    """
    Get artist hotttnesss from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_hotttnesss[songidx]

def get_artist_id(h5,songidx=0):
    """
    Get artist id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_id[songidx]

def get_artist_mbid(h5,songidx=0):
    """
    Get artist musibrainz id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_mbid[songidx]

def get_artist_playmeid(h5,songidx=0):
    """
    Get artist playme id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_playmeid[songidx]

def get_artist_7digitalid(h5,songidx=0):
    """
    Get artist 7digital id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_7digitalid[songidx]

def get_artist_latitude(h5,songidx=0):
    """
    Get artist latitude from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_latitude[songidx]

def get_artist_longitude(h5,songidx=0):
    """
    Get artist longitude from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_longitude[songidx]

def get_artist_location(h5,songidx=0):
    """
    Get artist location from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_location[songidx]

def get_artist_name(h5,songidx=0):
    """
    Get artist name from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_name[songidx]

def get_release(h5,songidx=0):
    """
    Get release from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.release[songidx]

def get_release_7digitalid(h5,songidx=0):
    """
    Get release 7digital id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.release_7digitalid[songidx]

def get_song_id(h5,songidx=0):
    """
    Get song id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.song_id[songidx]

def get_song_hotttnesss(h5,songidx=0):
    """
    Get song hotttnesss from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.song_hotttnesss[songidx]

def get_title(h5,songidx=0):
    """
    Get title from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.title[songidx]

def get_track_7digitalid(h5,songidx=0):
    """
    Get track 7digital id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.track_7digitalid[songidx]

def get_similar_artists(h5,songidx=0):
    """
    Get similar artists array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.similar_artists[h5.root.metadata.songs.cols.idx_similar_artists[songidx]:]
    return h5.root.metadata.similar_artists[h5.root.metadata.songs.cols.idx_similar_artists[songidx]:
                                            h5.root.metadata.songs.cols.idx_similar_artists[songidx+1]]

def get_artist_terms(h5,songidx=0):
    """
    Get artist terms array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.artist_terms[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
    return h5.root.metadata.artist_terms[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                            h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

def get_artist_terms_freq(h5,songidx=0):
    """
    Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.artist_terms_freq[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
    return h5.root.metadata.artist_terms_freq[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                              h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

def get_artist_terms_weight(h5,songidx=0):
    """
    Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.artist_terms_weight[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
    return h5.root.metadata.artist_terms_weight[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                                h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

def get_analysis_sample_rate(h5,songidx=0):
    """
    Get analysis sample rate from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.analysis_sample_rate[songidx]

def get_audio_md5(h5,songidx=0):
    """
    Get audio MD5 from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.audio_md5[songidx]

def get_danceability(h5,songidx=0):
    """
    Get danceability from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.danceability[songidx]

def get_duration(h5,songidx=0):
    """
    Get duration from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.duration[songidx]

def get_end_of_fade_in(h5,songidx=0):
    """
    Get end of fade in from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.end_of_fade_in[songidx]

def get_energy(h5,songidx=0):
    """
    Get energy from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.energy[songidx]

def get_key(h5,songidx=0):
    """
    Get key from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.key[songidx]

def get_key_confidence(h5,songidx=0):
    """
    Get key confidence from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.key_confidence[songidx]

def get_loudness(h5,songidx=0):
    """
    Get loudness from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.loudness[songidx]

def get_mode(h5,songidx=0):
    """
    Get mode from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.mode[songidx]

def get_mode_confidence(h5,songidx=0):
    """
    Get mode confidence from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.mode_confidence[songidx]

def get_start_of_fade_out(h5,songidx=0):
    """
    Get start of fade out from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.start_of_fade_out[songidx]

def get_tempo(h5,songidx=0):
    """
    Get tempo from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.tempo[songidx]

def get_time_signature(h5,songidx=0):
    """
    Get signature from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.time_signature[songidx]

def get_time_signature_confidence(h5,songidx=0):
    """
    Get signature confidence from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.time_signature_confidence[songidx]

def get_track_id(h5,songidx=0):
    """
    Get track id from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.track_id[songidx]

def get_segments_start(h5,songidx=0):
    """
    Get segments start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_start[h5.root.analysis.songs.cols.idx_segments_start[songidx]:]
    return h5.root.analysis.segments_start[h5.root.analysis.songs.cols.idx_segments_start[songidx]:
                                           h5.root.analysis.songs.cols.idx_segments_start[songidx+1]]

def get_segments_confidence(h5,songidx=0):
    """
    Get segments confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_confidence[h5.root.analysis.songs.cols.idx_segments_confidence[songidx]:]
    return h5.root.analysis.segments_confidence[h5.root.analysis.songs.cols.idx_segments_confidence[songidx]:
                                                h5.root.analysis.songs.cols.idx_segments_confidence[songidx+1]]

def get_segments_pitches(h5,songidx=0):
    """
    Get segments pitches array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_pitches[h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:,:]
    return h5.root.analysis.segments_pitches[h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:
                                             h5.root.analysis.songs.cols.idx_segments_pitches[songidx+1],:]

def get_segments_timbre(h5,songidx=0):
    """
    Get segments timbre array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_timbre[h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:,:]
    return h5.root.analysis.segments_timbre[h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:
                                            h5.root.analysis.songs.cols.idx_segments_timbre[songidx+1],:]

def get_segments_loudness_max(h5,songidx=0):
    """
    Get segments loudness max array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_loudness_max[h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:]
    return h5.root.analysis.segments_loudness_max[h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:
                                                  h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx+1]]

def get_segments_loudness_max_time(h5,songidx=0):
    """
    Get segments loudness max time array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_loudness_max_time[h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:]
    return h5.root.analysis.segments_loudness_max_time[h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:
                                                       h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx+1]]

def get_segments_loudness_start(h5,songidx=0):
    """
    Get segments loudness start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_loudness_start[h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:]
    return h5.root.analysis.segments_loudness_start[h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:
                                                    h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx+1]]

def get_sections_start(h5,songidx=0):
    """
    Get sections start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.sections_start[h5.root.analysis.songs.cols.idx_sections_start[songidx]:]
    return h5.root.analysis.sections_start[h5.root.analysis.songs.cols.idx_sections_start[songidx]:
                                           h5.root.analysis.songs.cols.idx_sections_start[songidx+1]]

def get_sections_confidence(h5,songidx=0):
    """
    Get sections confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.sections_confidence[h5.root.analysis.songs.cols.idx_sections_confidence[songidx]:]
    return h5.root.analysis.sections_confidence[h5.root.analysis.songs.cols.idx_sections_confidence[songidx]:
                                                h5.root.analysis.songs.cols.idx_sections_confidence[songidx+1]]

def get_beats_start(h5,songidx=0):
    """
    Get beats start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.beats_start[h5.root.analysis.songs.cols.idx_beats_start[songidx]:]
    return h5.root.analysis.beats_start[h5.root.analysis.songs.cols.idx_beats_start[songidx]:
                                        h5.root.analysis.songs.cols.idx_beats_start[songidx+1]]

def get_beats_confidence(h5,songidx=0):
    """
    Get beats confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.beats_confidence[h5.root.analysis.songs.cols.idx_beats_confidence[songidx]:]
    return h5.root.analysis.beats_confidence[h5.root.analysis.songs.cols.idx_beats_confidence[songidx]:
                                             h5.root.analysis.songs.cols.idx_beats_confidence[songidx+1]]

def get_bars_start(h5,songidx=0):
    """
    Get bars start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.bars_start[h5.root.analysis.songs.cols.idx_bars_start[songidx]:]
    return h5.root.analysis.bars_start[h5.root.analysis.songs.cols.idx_bars_start[songidx]:
                                       h5.root.analysis.songs.cols.idx_bars_start[songidx+1]]

def get_bars_confidence(h5,songidx=0):
    """
    Get bars start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.bars_confidence[h5.root.analysis.songs.cols.idx_bars_confidence[songidx]:]
    return h5.root.analysis.bars_confidence[h5.root.analysis.songs.cols.idx_bars_confidence[songidx]:
                                            h5.root.analysis.songs.cols.idx_bars_confidence[songidx+1]]

def get_tatums_start(h5,songidx=0):
    """
    Get tatums start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.tatums_start[h5.root.analysis.songs.cols.idx_tatums_start[songidx]:]
    return h5.root.analysis.tatums_start[h5.root.analysis.songs.cols.idx_tatums_start[songidx]:
                                         h5.root.analysis.songs.cols.idx_tatums_start[songidx+1]]

def get_tatums_confidence(h5,songidx=0):
    """
    Get tatums confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.tatums_confidence[h5.root.analysis.songs.cols.idx_tatums_confidence[songidx]:]
    return h5.root.analysis.tatums_confidence[h5.root.analysis.songs.cols.idx_tatums_confidence[songidx]:
                                              h5.root.analysis.songs.cols.idx_tatums_confidence[songidx+1]]

def get_artist_mbtags(h5,songidx=0):
    """
    Get artist musicbrainz tag array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.musicbrainz.songs.nrows == songidx + 1:
        return h5.root.musicbrainz.artist_mbtags[h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
    return h5.root.musicbrainz.artist_mbtags[h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                             h5.root.metadata.songs.cols.idx_artist_mbtags[songidx+1]]

def get_artist_mbtags_count(h5,songidx=0):
    """
    Get artist musicbrainz tag count array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.musicbrainz.songs.nrows == songidx + 1:
        return h5.root.musicbrainz.artist_mbtags_count[h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
    return h5.root.musicbrainz.artist_mbtags_count[h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                                   h5.root.metadata.songs.cols.idx_artist_mbtags[songidx+1]]

def get_year(h5,songidx=0):
    """
    Get release year from a HDF5 song file, by default the first song in it
    """
    return h5.root.musicbrainz.songs.cols.year[songidx]
                                                                                                                                                                                                                                                                                                                              hitmap.py                                                                                           000644  000765  000024  00000002657 13023325644 014354  0                                                                                                    ustar 00sarahgerard                     staff                           000000  000000                                                                                                                                                                         import os
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

                                                                                 missingValues.py                                                                                    000644  000765  000024  00000001502 13023325644 015707  0                                                                                                    ustar 00sarahgerard                     staff                           000000  000000                                                                                                                                                                         import pandas as pd
from sklearn.preprocessing import Imputer
import sklearn.preprocessing
dataorig = pd.read_csv("/Users/segerard/src/SOM/src/data/SongCSV.csv")
hd = dataorig.columns
feats = hd[0:-5]
labels = hd[-5:]
data = dataorig[feats]
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(data)
trans = imp.transform(data)

min_max_scaler = sklearn.preprocessing.MinMaxScaler()
transscale = min_max_scaler.fit_transform(trans)

transdf = pd.DataFrame(transscale)
labelsdf = dataorig[labels]
finaldf = pd.concat([transdf,labelsdf],axis=1)
finaldf.columns = hd
finaldf.to_csv('Song.csv',index=False,sep=',')

#transdf.columns = feats
#labelsdf.columns = labels
transdf.to_csv('Features.txt',index=False,header=False,columns=None,sep=' ')
labelsdf.to_csv('Labels.txt',index=False,header=False,columns=None,sep=' ')

                                                                                                                                                                                              msdHDF5toCSV.py                                                                                     000644  000765  000024  00000067473 13023325644 015212  0                                                                                                    ustar 00sarahgerard                     staff                           000000  000000                                                                                                                                                                         """
Alexis Greenstreet (October 4, 2015) University of Wisconsin-Madison

This code is designed to convert the HDF5 files of the Million Song Dataset
to a CSV by extracting various song properties.

The script writes to a "SongCSV.csv" in the directory containing this script.

Please note that in the current form, this code only extracts the following
information from the HDF5 files:
AlbumID, AlbumName, ArtistID, ArtistLatitude, ArtistLocation,
ArtistLongitude, ArtistName, Danceability, Duration, KeySignature,
KeySignatureConfidence, SongID, Tempo, TimeSignature,
TimeSignatureConfidence, Title, and Year.

This file also requires the use of "hdf5_getters.py", written by
Thierry Bertin-Mahieux (2010) at Columbia University

Credit:
This HDF5 to CSV code makes use of the following example code provided
at the Million Song Dataset website
(Home>Tutorial/Iterate Over All Songs,
http://labrosa.ee.columbia.edu/millionsong/pages/iterate-over-all-songs),
Which gives users the following code to get all song titles:

import os
import glob
import hdf5_getters
def get_all_titles(basedir,ext='.h5') :
    titles = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            titles.append( hdf5_getters.get_title(h5) )
            h5.close()
    return titles
"""

import sys
import os
import glob
import hdf5_getters
import re
import numpy as np
import shlex

class Song:
    songCount = 0
    # songDictionary = {}

    def __init__(self, songID):
        self.id = songID
        Song.songCount += 1
        # Song.songDictionary[songID] = self

        #self.albumName = None
        #self.albumID = None
        #self.artistID = None
        #self.artistLatitude = None
        #self.artistLocation = None
        #self.artistLongitude = None
        #self.artistName = None
        #self.danceability = None
        #self.duration = None
        #self.genreList = []
        #self.keySignature = None
        #self.keySignatureConfidence = None
        #self.lyrics = None
        #self.popularity = None
        #self.tempo = None
        #self.timeSignature = None
        #self.timeSignatureConfidence = None
        #self.title = None
        #self.year = None

        self.analysisSampleRate = None
        self.artistFamiliarity = None
        self.artistHotttnesss = None
        self.artistLatitude = None
        self.artistLongitude = None
        self.artistMbid = None
        self.barsConfidence = None
        self.barsStart = None
        self.beatsConfidence = None
        self.beatsStart = None
        self.danceability = None
        self.duration = None
        self.endOfFadeIn = None
        self.energy = None
        self.key = None
        self.keyConfidence = None
        self.loudness = None
        self.mode = None
        self.modeConfidence = None
        self.sectionsConfidence = None
        self.sectionsStart = None
        self.segmentsConfidence = None
        self.segmentsLoudnessMax = None
        self.segmentsLoudnessMaxTime = None
        self.segmentsLoudnessStart = None
        self.segmentsPitches = None
        self.segmentsStart = None
        self.segmentsTimbre = None
        self.songHotttnesss = None
        self.startOfFadeOut = None
        self.tatumsConfidence = None
        self.tatumsStart = None
        self.temp = None
        self.timeSignitureConfidence = None
        self.title = None
        self.year = None
        self.decade = None
        self.artistMbtags = None

    def displaySongCount(self):
        print "Total Song Count %i" % Song.songCount

    def displaySong(self):
        print "ID: %s" % self.id


def main(argv):
    if len(argv) != 1:
        print "Specify data directory"
        return
    basedir = argv[0]
    outputFile1 = open('SongCSV.csv', 'w')
    outputFile2 = open('TagsCSV.csv', 'w')
    csvRowString = ""
    csvLabelString = ""
    #################################################
    #if you want to prompt the user for the order of attributes in the csv,
    #leave the prompt boolean set to True
    #else, set 'prompt' to False and set the order of attributes in the 'else'
    #clause
    prompt = False
    #################################################
    if prompt == True:
        while prompt:

            prompt = False

            csvAttributeString = raw_input("\n\nIn what order would you like the colums of the CSV file?\n" +
                "Please delineate with commas. The options are: " +
                "AlbumName, AlbumID, ArtistID, ArtistLatitude, ArtistLocation, ArtistLongitude,"+
                " ArtistName, Danceability, Duration, KeySignature, KeySignatureConfidence, Tempo," +
                " SongID, TimeSignature, TimeSignatureConfidence, Title, and Year.\n\n" +
                "For example, you may write \"Title, Tempo, Duration\"...\n\n" +
                "...or exit by typing 'exit'.\n\n")

            csvAttributeList = re.split('\W+', csvAttributeString)
            for i, v in enumerate(csvAttributeList):
                csvAttributeList[i] = csvAttributeList[i].lower()

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"


                if attribute == 'AlbumID'.lower():
                    csvRowString += 'AlbumID'
                elif attribute == 'AlbumName'.lower():
                    csvRowString += 'AlbumName'
                elif attribute == 'ArtistID'.lower():
                    csvRowString += 'ArtistID'
                elif attribute == 'ArtistLatitude'.lower():
                    csvRowString += 'ArtistLatitude'
                elif attribute == 'ArtistLocation'.lower():
                    csvRowString += 'ArtistLocation'
                elif attribute == 'ArtistLongitude'.lower():
                    csvRowString += 'ArtistLongitude'
                elif attribute == 'ArtistName'.lower():
                    csvRowString += 'ArtistName'
                elif attribute == 'Danceability'.lower():
                    csvRowString += 'Danceability'
                elif attribute == 'Duration'.lower():
                    csvRowString += 'Duration'
                elif attribute == 'KeySignature'.lower():
                    csvRowString += 'KeySignature'
                elif attribute == 'KeySignatureConfidence'.lower():
                    csvRowString += 'KeySignatureConfidence'
                elif attribute == 'SongID'.lower():
                    csvRowString += "SongID"
                elif attribute == 'Tempo'.lower():
                    csvRowString += 'Tempo'
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += 'TimeSignature'
                elif attribute == 'TimeSignatureConfidence'.lower():
                    csvRowString += 'TimeSignatureConfidence'
                elif attribute == 'Title'.lower():
                    csvRowString += 'Title'
                elif attribute == 'Year'.lower():
                    csvRowString += 'Year'
                elif attribute == 'Exit'.lower():
                    sys.exit()
                else:
                    prompt = True
                    print "=============="
                    print "I believe there has been an error with the input."
                    print "=============="
                    break

                csvRowString += ","

            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString);
            csvRowString = ""
    #else, if you want to hard code the order of the csv file and not prompt
    #the user,
    else:
        #################################################
        #change the order of the csv file here
        #Default is to list all available attributes (in alphabetical order)
        #csvRowString = ("SongID,AlbumID,AlbumName,ArtistID,ArtistLatitude,ArtistLocation,"+
        #    "ArtistLongitude,ArtistName,Danceability,Duration,KeySignature,"+
        #    "KeySignatureConfidence,Tempo,TimeSignature,TimeSignatureConfidence,"+
        #    "Title,Year")
        csvRowString = ("ArtistFamiliarity,ArtistHotttnesss,"+
            "BarsConfidence,BarsStart,BeatsConfidence,BeatsStart,Duration,"+
            "EndOfFadeIn,Key,KeyConfidence,Loudness,Mode,ModeConfidence,"+
            "SectionsConfidence,SectionsStart,SegmentsConfidence,SegmentsLoudnessMax,"+
            "SegmentsLoudnessMaxTime,SegmentsLoudnessStart,SegmentsStart,"+
            "SongHotttnesss,StartOfFadeOut,TatumsConfidence,TatumsStart,Tempo,TimeSignature,TimeSignatureConfidence,"+
            "SegmentsPitches,SegmentsTimbre,Title,Year,Decade,ArtistMbtags")
        #################################################
        header = str()
        csvAttributeList = re.split('\W+', csvRowString)
        arrayAttributes = ["BarsConfidence","BarsStart","BeatsConfidence","BeatsStart",
                           "SectionsConfidence","SectionsStart","SegmentsConfidence","SegmentsLoudnessMax",
                           "SegmentsLoudnessMaxTime","SegmentsLoudnessStart","SegmentsStart",
                           "TatumsConfidence","TatumsStart"]
        for i, v in enumerate(csvAttributeList):
            csvAttributeList[i] = csvAttributeList[i].lower()
            if(v=="SegmentsPitches"):
                for i in range(90):
                    header = header + "SegmentsPitches" + str(i) + ","
            elif(v=="SegmentsTimbre"):
                for i in range(90):
                    header = header + "SegmentsTimbre" + str(i) + ","
            elif(v in arrayAttributes):
                header = header + v + str(0) + ","
                header = header + v + str(1) + ","
            else:
                header = header + v + ","
        outputFile1.write("SongNumber,");
        #outputFile1.write(csvRowString + "\n");
        outputFile1.write(header + "\n");
        csvRowString = ""

    #################################################


    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    #basedir = "MillionSongSubset/data/A/A/" # "." As the default means the current directory
    ext = ".h5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    #FOR LOOP
    all = sorted(os.walk(basedir))
    for root, dirs, files in all:
        files = sorted(glob.glob(os.path.join(root,'*'+ext)))
        for f in files:
            print f

            songH5File = hdf5_getters.open_h5_file_read(f)
            song = Song(str(hdf5_getters.get_song_id(songH5File)))

            #testDanceability = hdf5_getters.get_danceability(songH5File)
            # print type(testDanceability)
            # print ("Here is the danceability: ") + str(testDanceability)

            song.analysisSampleRate = str(hdf5_getters.get_analysis_sample_rate(songH5File))
            song.artistFamiliarity = str(hdf5_getters.get_artist_familiarity(songH5File))
            song.artistHotttnesss = str(hdf5_getters.get_artist_hotttnesss(songH5File))
            song.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
            song.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File))
            song.artistMbid = str(hdf5_getters.get_artist_mbid(songH5File))
            song.barsConfidence = np.array(hdf5_getters.get_bars_confidence(songH5File))
            song.barsStart = np.array(hdf5_getters.get_bars_start(songH5File))
            song.beatsConfidence = np.array(hdf5_getters.get_beats_confidence(songH5File))
            song.beatsStart = np.array(hdf5_getters.get_beats_start(songH5File))
            song.danceability = str(hdf5_getters.get_danceability(songH5File))
            song.duration = str(hdf5_getters.get_duration(songH5File))
            song.endOfFadeIn = str(hdf5_getters.get_end_of_fade_in(songH5File))
            song.energy = str(hdf5_getters.get_energy(songH5File))
            song.key = str(hdf5_getters.get_key(songH5File))
            song.keyConfidence = str(hdf5_getters.get_key_confidence(songH5File))
            song.loudness = str(hdf5_getters.get_loudness(songH5File))
            song.mode = str(hdf5_getters.get_mode(songH5File))
            song.modeConfidence = str(hdf5_getters.get_mode_confidence(songH5File))
            song.sectionsConfidence = np.array(hdf5_getters.get_sections_confidence(songH5File))
            song.sectionsStart = np.array(hdf5_getters.get_sections_start(songH5File))
            song.segmentsConfidence = np.array(hdf5_getters.get_segments_confidence(songH5File))
            song.segmentsLoudnessMax = np.array(hdf5_getters.get_segments_loudness_max(songH5File))
            song.segmentsLoudnessMaxTime = np.array(hdf5_getters.get_segments_loudness_max_time(songH5File))
            song.segmentsLoudnessStart = np.array(hdf5_getters.get_segments_loudness_start(songH5File))
            song.segmentsPitches = np.array(hdf5_getters.get_segments_pitches(songH5File))
            song.segmentsStart = np.array(hdf5_getters.get_segments_start(songH5File))
            song.segmentsTimbre = np.array(hdf5_getters.get_segments_timbre(songH5File))
            song.songHotttnesss = str(hdf5_getters.get_song_hotttnesss(songH5File))
            song.startOfFadeOut = str(hdf5_getters.get_start_of_fade_out(songH5File))
            song.tatumsConfidence = np.array(hdf5_getters.get_tatums_confidence(songH5File))
            song.tatumsStart = np.array(hdf5_getters.get_tatums_start(songH5File))
            song.tempo = str(hdf5_getters.get_tempo(songH5File))
            song.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
            song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
            song.songid = str(hdf5_getters.get_song_id(songH5File))
            song.title = str(hdf5_getters.get_title(songH5File))
            song.year = str(hdf5_getters.get_year(songH5File))
            song.artistMbtags = str(hdf5_getters.get_artist_mbtags(songH5File))
            #print song count
            csvRowString += str(song.songCount) + ","
            csvLabelString += str(song.songCount) + ","
            
            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"

                if attribute == 'AnalysisSampleRate'.lower():
                    csvRowString += song.analysisSampleRate
                elif attribute == 'ArtistFamiliarity'.lower():
                    csvRowString += song.artistFamiliarity
                elif attribute == 'ArtistHotttnesss'.lower():
                    csvRowString += song.artistHotttnesss
                elif attribute == 'ArtistLatitude'.lower():
                    latitude = song.artistLatitude
                    if latitude == 'nan':
                        latitude = ''
                    csvRowString += latitude
                elif attribute == 'ArtistLongitude'.lower():
                    longitude = song.artistLongitude
                    if longitude == 'nan':
                        longitude = ''
                    csvRowString += longitude
                elif attribute == 'ArtistMbid'.lower():
                    csvRowString += song.artistMbid
                elif attribute == 'BarsConfidence'.lower():
                    arr = song.barsConfidence
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'BarsStart'.lower():
                    arr = song.barsStart
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'BeatsConfidence'.lower():
                    arr = song.beatsConfidence
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'BeatsStart'.lower():
                    arr = song.beatsStart
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'Danceability'.lower():
                    csvRowString += song.danceability
                elif attribute == 'Duration'.lower():
                    csvRowString += song.duration
                elif attribute == 'EndOfFadeIn'.lower():
                    csvRowString += song.endOfFadeIn
                elif attribute == 'Energy'.lower():
                    csvRowString += song.energy
                elif attribute == 'Key'.lower():
                    csvRowString += song.key
                elif attribute == 'KeyConfidence'.lower():
                    csvRowString += song.keyConfidence
                elif attribute == 'Loudness'.lower():
                    csvRowString += song.loudness
                elif attribute == 'Mode'.lower():
                    csvRowString += song.mode
                elif attribute == 'ModeConfidence'.lower():
                    csvRowString += song.modeConfidence
                elif attribute == 'SectionsConfidence'.lower():
                    arr = song.sectionsConfidence
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'SectionsStart'.lower():
                    arr = song.sectionsStart
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'SegmentsConfidence'.lower():
                    arr = song.segmentsConfidence
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'SegmentsLoudnessMax'.lower():
                    arr = song.segmentsLoudnessMax
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'SegmentsLoudnessMaxTime'.lower():
                    arr = song.segmentsLoudnessMaxTime
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'SegmentsLoudnessStart'.lower():
                    arr = song.segmentsLoudnessStart
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'SegmentsStart'.lower():
                    arr = song.segmentsStart
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'SongHotttnesss'.lower():
                    hotttnesss = song.songHotttnesss
                    if hotttnesss == 'nan':
                        hotttnesss = 'NaN'
                    csvRowString += hotttnesss
                elif attribute == 'StartOfFadeOut'.lower():
                    csvRowString += song.startOfFadeOut
                elif attribute == 'TatumsConfidence'.lower():
                    arr = song.tatumsConfidence
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'TatumsStart'.lower():
                    arr = song.tatumsStart
                    if arr.shape[0] == 0:
                        arrmean = ''
                        arrnorm = ''
                    else:
                        arrmean = np.mean(arr)
                        arrnorm = np.linalg.norm(arr)
                    csvRowString += str(arrmean) + ',' + str(arrnorm)
                elif attribute == 'Tempo'.lower():
                    # print "Tempo: " + song.tempo
                    csvRowString += song.tempo
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += song.timeSignature
                elif attribute == 'TimeSignatureConfidence'.lower():
                    # print "time sig conf: " + song.timeSignatureConfidence
                    csvRowString += song.timeSignatureConfidence
                elif attribute == 'SegmentsPitches'.lower():
                    colmean = np.mean(song.segmentsPitches,axis=0)
                    for m in colmean:
                        csvRowString += str(m) + ","
                    cov = np.dot(song.segmentsPitches.T,song.segmentsPitches)
                    utriind = np.triu_indices(cov.shape[0])
                    feats = cov[utriind]
                    for feat in feats:
                        csvRowString += str(feat) + ","
                    lastIndex = len(csvRowString)
                    csvRowString = csvRowString[0:lastIndex-1]
                elif attribute == 'SegmentsTimbre'.lower():
                    colmean = np.mean(song.segmentsTimbre,axis=0)
                    for m in colmean:
                        csvRowString += str(m) + ","
                    cov = np.dot(song.segmentsTimbre.T,song.segmentsTimbre)
                    utriind = np.triu_indices(cov.shape[0])
                    feats = cov[utriind]
                    for feat in feats:
                        csvRowString += str(feat) + ","
                    lastIndex = len(csvRowString)
                    csvRowString = csvRowString[0:lastIndex-1]
                elif attribute == 'SongID'.lower():
                    csvRowString += "\"" + song.id + "\""
                elif attribute == 'Title'.lower():
                    csvRowString += "\"" + song.title + "\""
                elif attribute == 'Year'.lower():
                    csvRowString += song.year
                elif attribute == 'Decade'.lower():
                    yr = song.year
                    if yr > 0:
                        decade = song.year[:-1] + '0'
                    else:
                        decade = '0'
                    csvRowString += decade
                elif attribute == 'ArtistMbtags'.lower():
                    tags = song.artistMbtags[1:-1]
                    tags = "\"" + tags + "\""
                    tags = tags.replace("\n",'')
                    csvRowString += tags
                    tagsarray = shlex.split(tags)
                    for t in tagsarray:
                        csvLabelString += t + ","
                else:
                     csvRowString += "Erm. This didn't work. Error. :( :(\n"

                csvRowString += ","

                '''
                if attribute == 'AlbumID'.lower():
                    csvRowString += song.albumID
                elif attribute == 'AlbumName'.lower():
                    albumName = song.albumName
                    albumName = albumName.replace(',',"")
                    csvRowString += "\"" + albumName + "\""
                elif attribute == 'ArtistID'.lower():
                    csvRowString += "\"" + song.artistID + "\""
                elif attribute == 'ArtistLatitude'.lower():
                    latitude = song.artistLatitude
                    if latitude == 'nan':
                        latitude = ''
                    csvRowString += latitude
                elif attribute == 'ArtistLocation'.lower():
                    location = song.artistLocation
                    location = location.replace(',','')
                    csvRowString += "\"" + location + "\""
                elif attribute == 'ArtistLongitude'.lower():
                    longitude = song.artistLongitude
                    if longitude == 'nan':
                        longitude = ''
                    csvRowString += longitude
                elif attribute == 'ArtistName'.lower():
                    csvRowString += "\"" + song.artistName + "\""
                elif attribute == 'Danceability'.lower():
                    csvRowString += song.danceability
                elif attribute == 'Duration'.lower():
                    csvRowString += song.duration
                elif attribute == 'KeySignature'.lower():
                    csvRowString += song.keySignature
                elif attribute == 'KeySignatureConfidence'.lower():
                    # print "key sig conf: " + song.timeSignatureConfidence
                    csvRowString += song.keySignatureConfidence
                elif attribute == 'SongID'.lower():
                    csvRowString += "\"" + song.id + "\""
                elif attribute == 'Tempo'.lower():
                    # print "Tempo: " + song.tempo
                    csvRowString += song.tempo
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += song.timeSignature
                elif attribute == 'TimeSignatureConfidence'.lower():
                    # print "time sig conf: " + song.timeSignatureConfidence
                    csvRowString += song.timeSignatureConfidence
                elif attribute == 'Title'.lower():
                    csvRowString += "\"" + song.title + "\""
                elif attribute == 'Year'.lower():
                    csvRowString += song.year
                else:
                    csvRowString += "Erm. This didn't work. Error. :( :(\n"

                csvRowString += ","
                '''
            #Remove the final comma from each row in the csv
            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""
            
            lastIndex = len(csvLabelString)
            csvLabelString = csvLabelString[0:lastIndex-1]
            csvLabelString += "\n"
            outputFile2.write(csvLabelString)
            csvLabelString = ""

            songH5File.close()

    outputFile1.close()
    outputFile2.close()
if __name__ == "__main__":
    main(sys.argv[1:])
#main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     