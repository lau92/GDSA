import os
from modules.features.BofExtractor import BofExtractor

def processLabel(pathDirImagesBase, pathDirDatasets, bofExtractor, pathDirBofs, datasetLabel):
    
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
        
    print 'Extracting BoF from ' + pathFileDataset + "..."

    # Directory for BoFs
    pathDirBofLabel = os.path.join( pathDirBofs, datasetLabel )    
    if not os.path.exists(pathDirBofLabel):
        os.makedirs(pathDirBofLabel)
        
    bofExtractor.processTxtFile( pathFileDataset, pathDirImages, 'jpg', pathDirBofLabel)
    
    
# Main
if __name__ == "__main__":
    
    pathHome = os.path.abspath('C:\Users\Adria\Documents\upc_temp\gdsa\Projecte\proves_proj\emohe-pyxel-deb01cc5202e')  
    pathWork = os.path.join(pathHome, 'tools','socialevent','mediaeval2013','classification' )
    pathDirImagesBase = os.path.join(pathWork, '1_images')
    pathDirDatasets = os.path.join(pathWork, '2_datasets')
    pathFileVocabulary = os.path.join( pathWork, '3_vocabulary','vocabulary12345.p' )
    #pathFileVocabulary = os.path.join( pathWork, '3_vocabulary','vocabulary.p' )
    pathDirBofs = os.path.join(pathWork, '4_bof')
    
    # Init the BoF extractor
    bofExtractor = BofExtractor(pathFileVocabulary, flagVerbose=False)
    
    # Process the train dataset
    #processLabel(pathDirImagesBase, pathDirDatasets, bofExtractor, pathDirBofs, 'train12345')
    #processLabel(pathDirImagesBase, pathDirDatasets, bofExtractor, pathDirBofs, 'train')
    
    # Process the test dataset
    processLabel(pathDirImagesBase, pathDirDatasets, bofExtractor, pathDirBofs, 'Images5')
    #processLabel(bofExtractor, pathDirBofs, 'test')
    
    print "Extracting BoF... done."
