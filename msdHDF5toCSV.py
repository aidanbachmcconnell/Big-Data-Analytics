"""
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
