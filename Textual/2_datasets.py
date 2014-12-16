#ejecutar:
#runfile('C:/Users/Adria/Documents/upc_temp/gdsa/Projecte/emohe-pyxel-deb01cc5202e/tools/
#socialevent/mediaeval2013/classification/2_datasets.py', wdir=r'C:/Users/Adria/Documents
#/upc_temp/gdsa/Projecte/emohe-pyxel-deb01cc5202e')

import os

from modules.computation.Dataset import Dataset

def _main():
    
    print "S'han creat els arxius de test i train dins de la carpeta 2_datasets"
    
    pathHome = os.path.abspath('C:\Users\Adria\Documents\upc_temp\gdsa\Projecte\proves_proj\emohe-pyxel-deb01cc5202e')
    
    pathWork = os.path.join(pathHome, 'tools','socialevent','mediaeval2013','classification' )
    pathImages = os.path.join(pathWork, '1_images')
    pathDatasets = os.path.join(pathWork, '2_datasets' )
    
    # For each data partition (train & test)
    for partition in os.listdir(pathImages):
        
        # If it is a directory 
        dirPartition = os.path.join( pathImages, partition )
        if os.path.isdir(dirPartition): 
        
            # Define the filename to contain the list of images to process
            filenameOut = os.path.join( pathDatasets, partition + '.txt')
            
            dataset = Dataset( filenameOut, 
                            flagSaveInMemory=False, 
                            flagVerbose=True)
    
            dataset.build( dirPartition, '.jpg' )

#def run():
_main()


