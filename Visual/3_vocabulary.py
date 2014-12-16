import os
import sys

from modules.features.VisualVocabulary import VisualVocabulary

def usage():
    print "This script will generate a visual vocabulary."


def main(argv):
    
    # Define the default values for the options
    pathHome = os.path.abspath('C:\Users\Adria\Documents\upc_temp\gdsa\Projecte\proves_proj\emohe-pyxel-deb01cc5202e')
    pathWork = os.path.join(pathHome, 'tools','socialevent','mediaeval2013','classification' )    
    pathDirImages = os.path.join( pathWork, '1_images', 'train' )
    pathFileDatasetTrain = os.path.join(pathWork, '2_datasets', 'train.txt')
    #pathDirImages = os.path.join( pathWork, '1_images', 'train' )
    #pathFileDatasetTrain = os.path.join(pathWork, '2_datasets', 'train.txt')
    pathVocabulary = os.path.join(pathWork, '3_vocabulary', 'vocabulary_prova2.p')

    _flagVerbose=False
    
    vocabularySize=256                  # Amount of visual words
    maxNumImages=10                     # Maximum amount of images to consider

    # Init the Visual Vocabulary
    visualVocabulary = VisualVocabulary(flagVerbose=_flagVerbose)
    
    
    visualVocabulary.buildFromImageCollection( pathFileDatasetTrain, 
                                              pathDirImages, 
                                              'jpg', 
                                              vocabularySize, 
                                              maxNumImages )
    
    visualVocabulary.saveToDisk( pathVocabulary )


if __name__ == "__main__":
    main(sys.argv[1:])
    

