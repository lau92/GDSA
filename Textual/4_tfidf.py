# -*- coding: utf-8 -*-
import os
from modules.features.TfidfExtractor import TfidfExtractor
from modules.features.TextVocabulary import TextVocabulary

from modules.socialevent.classification.GroundTruth import GroundTruth
from modules.socialevent.classification.Metadata import Metadata

print "funcio inicial"

def processLabel(TfidfExtractor, pathDirTfidfs, datasetLabel):
    
    print "ha entrat"
   # Directory where the images are located
    pathDirImages = os.path.join( pathDirImagesBase, datasetLabel ) 
    if not os.path.exists(pathDirImages):
        print 'ERROR: Image directory not found ' + pathDirImages
        return
     
    # File containing the image IDs   
    pathFileDataset = os.path.join( pathDirDatasets, datasetLabel + '.txt' )
    if not os.path.exists(pathFileDataset):
        print 'ERROR: Dataset file not found ' + pathFileDataset
        return    
        
    print 'Extracting Tfidf from ' + pathFileDataset + "..."

    # Directory for Tfidfs
    pathDirTfidfLabel = os.path.join( pathDirTfidfs, datasetLabel )    
    if not os.path.exists(pathDirTfidfLabel):
        os.makedirs(pathDirTfidfLabel)
        
    TfidfExtractor.processTxtFile( pathFileDataset, pathDirTfidfLabel)

   
# Main
if __name__ == "__main__":
    print "Hello"
    pathHome = os.path.abspath('C:\Users\Adria\Documents\upc_temp\gdsa\Projecte\proves_proj\emohe-pyxel-deb01cc5202e')
        
    pathWork = os.path.join(pathHome, 'tools','socialevent','mediaeval2013','classification' )
    pathDirImagesBase = os.path.join(pathWork, '1_images')
    pathDirDatasets = os.path.join(pathWork, '2_datasets')
    #pathFileVocabulary = os.path.join( pathWork, '3_vocabulary','vocabulary.p' )
    pathDirTfidfs = os.path.join(pathWork, '4_tfidf')
    
    pathFileMetadata = os.path.join(pathDirDatasets,'sed2013_task2_dataset_train.csv')
    #    pathFileDatasetTrain = os.path.join(pathWork, '2_datasets/train.txt')
    pathFileTags = os.path.join(pathDirDatasets,'sed2013_task2_dataset_train_tags.csv')
    
    
    # -------------------------------------------------------

    GROUND_TRUTH_FILE = 'sed2013_task2_dataset_train_gs.csv'
    gtPath = os.path.join(pathDirDatasets, GROUND_TRUTH_FILE)
    METADATA_FILE = 'sed2013_task2_dataset_train.csv' 
    TAG_FILE = 'sed2013_task2_dataset_train_tags.csv'
    # Load the metadata
    metadataPath = os.path.join(pathDirDatasets, METADATA_FILE)
    tagsPath = os.path.join(pathDirDatasets, TAG_FILE)
    print "he acabat els path"
    # --------------------------------------------------------------------------
    # Build the textual vocabulary saving the most frequent terms
    textVocabulary = TextVocabulary( ) #assignar classe buida textVocabulary
    print "estic treienet els nonevent"
    #llamar a gt y a metadata para quitar los non_event
    #groundTruth = GroundTruth(gtPath)
    #metadata = Metadata(metadataPath,tagsPath)
    #listOfTags = []
    #for event in groundTruth.get_eventIDs():
    #    if event != 'non_event':
    #        for img in groundTruth.get_photos_in_event(event):
    #            if metadata.get_tags_by_id(img)!=None:# si la imagen no tiene tags peta
    #                for tag in metadata.get_tags_by_id(img):
    #                    listOfTags.append(tag)
    
        
    pathFileDataset = os.path.join( pathDirDatasets, 'train.txt')
    listOfTags = textVocabulary.processTxtFile(pathFileDataset,metadataPath,tagsPath) #millora!  
    textVocabulary.buildFromTags2(listOfTags, (len(listOfTags)/2)) 
    
    pathFileVocabulary = os.path.join( pathWork, '3_vocabulary', 'text_23_12.p')
    textVocabulary.saveToDisk(pathFileVocabulary)
    
    # --------------------------------------------------------------------------
    # Init the TF/IDF extractor
    tfidfExtractor = TfidfExtractor(pathFileMetadata, 
                                    pathFileTags, 
                                    pathFileVocabulary,
                                    flagVerbose=False)

    # Process the train dataset
    processLabel(tfidfExtractor, pathDirTfidfs, 'train')
    
    # Process the test dataset
    #processLabel(tfidfExtractor, pathDirTfidfs, 'test')
    
    print "Extracting TF-IDF... done."
