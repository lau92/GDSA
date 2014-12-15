import os
import sys

from modules.features.VisualVocabulary import VisualVocabulary

def usage():
    print "This script will generate a visual vocabulary."


def main(argv):
    
    # Define the default values for the options
    # Paths
    pathHome = os.path.abspath('/Users/Tania')
    pathWork = os.path.join( pathHome, 'workspace', 'pyxel','tools','socialevent','mediaeval2013','classification')   
    
    pathDirImages = os.path.join( pathWork, '1_images', 'train' )
    pathFileDatasetTrain = os.path.join(pathWork, '2_datasets', 'train.txt')
    pathVocabulary = os.path.join(pathWork, '3_vocabulary', 'vocabulary.p')

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
    
def run(argv):
    main()
