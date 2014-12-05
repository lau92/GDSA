#4_tfidf
import os
from modules.features.TfidfExtractor import TfidfExtractor
from modules.features.TextVocabulary import TextVocabulary


def processLabel(TfidfExtractor, pathDirTfidfs, datasetLabel):
    
    # Directory where the images are located
    pathDirImages = os.path.join( pathDirImagesBase, datasetLabel ) 
    if not os.path.exists(pathDirImages):
        print 'ERROR: Directory not found ' + pathDirImages
        return
     
    # File containing the image IDs   
    pathFileDataset = os.path.join( pathDirDatasets, datasetLabel + '.txt' )
    if not os.path.exists(pathFileDataset):
        print 'ERROR: File not found ' + pathFileDataset
        return    
        
    print 'Extracting Tfidf from ' + pathFileDataset + "..."

    # Directory for Tfidfs
    pathDirTfidfLabel = os.path.join( pathDirTfidfs, datasetLabel )    
    if not os.path.exists(pathDirTfidfLabel):
        os.makedirs(pathDirTfidfLabel)
        
    TfidfExtractor.processTxtFile( pathFileDataset, pathDirTfidfLabel)
    
    
# Main
def main():
    if __name__ == "__main__":
        
        pathHome = os.path.expanduser('~')
        
        pathWork = os.path.join( pathHome, 'work', 'mediaeval','2013-sed','classification' )
        pathDirImagesBase = os.path.join(pathWork, '1_images')
        pathDirDatasets = os.path.join(pathWork, '2_datasets')
        #pathFileVocabulary = os.path.join( pathWork, '3_vocabulary','vocabulary.p' )
        pathDirTfidfs = os.path.join(pathWork, '4_tfidf')
        
        pathFileMetadata = os.path.join(pathDirDatasets,'sed2013_task2_dataset_train.csv')
        #    pathFileDatasetTrain = os.path.join(pathWork, '2_datasets/train.txt')
        pathFileTags = os.path.join(pathDirDatasets,'sed2013_task2_dataset_train_tags.csv')
        
        # Build the textual vocabulary saving the most frequent terms
        textVocabulary = TextVocabulary( )
        textVocabulary.buildFromTags(pathFileTags, 5000)
        pathFileVocabulary =os.path.join( pathWork, '3_vocabulary', 'text.p')
        textVocabulary.saveToDisk(pathFileVocabulary)
        
        # Init the TF/IDF extractor
        tfidfExtractor = TfidfExtractor(pathFileMetadata, 
                                        pathFileTags, 
                                        pathFileVocabulary,
                                        flagVerbose=False)
        
        # Process the train dataset
        processLabel(tfidfExtractor, pathDirTfidfs, 'train'+'_19_7')
        
        # Process the test dataset
        processLabel(tfidfExtractor, pathDirTfidfs, 'test'+'_19_7')
        
        print "Extracting TF-IDF... done."
        
def run():
    main()
