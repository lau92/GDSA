# tool to generate an Annotation and Ontology
import os
import pandas as pd
import pickle
#from modules.socialevent.classification.GroundTruth import GroundTruth
from modules.classification.Annotation import Annotation
from modules.classification.Ontology import Ontology
from modules.classification.LabelType import LabelType

def main():
    # Paths
    pathHome = os.path.abspath('/Users/Tania')
    datasetsPath = os.path.join( pathHome, 'workspace', 'pyxel','tools','socialevent','mediaeval2013','classification', '2_datasets')   
    
    # Arxiu csv que conte veritat terreny
    groundTruthFile = 'sed2013_task2_dataset_train_gs.csv'
    
    # Creacio arxius que contindra anotacio i ontologia
    annotationFile = 'annotation.p'
    ontologyFile = 'ontology.p'
    
    annotationSavePathFile = os.path.join(datasetsPath, annotationFile)
    groundTruthPathFile = os.path.join(datasetsPath, groundTruthFile)
    ontologyPathFile = os.path.join(datasetsPath, ontologyFile)
    
    # Lectura de l'arxiu de ground truth
    dataframe_csv = pd.read_csv('%s' % (groundTruthPathFile), sep='\t')
    
    # For each class of event
    gtGroupedByEvent = dataframe_csv.groupby('event_type')
    
    ontology = Ontology()
    
    for semanticClass in gtGroupedByEvent.groups.keys():
        ontology.addSemanticClass(semanticClass) 
            
    # Create a new Annotation
    annotation = Annotation(ontology)
            
    # Iterate row by row thorugh the Pandas Dataframe            
    for index, row in dataframe_csv.iterrows():
        #print row['gt'], row['document_id']
        annotation.addInstance( str(row['event_type']), LabelType.POSITIVE, str(row['document_id']) )
        # This for add only the positive annotation
    
    # to generate the neutral and negative annotation
    annotation.completetheAnnotation()
    
    pickle.dump( annotation , open( annotationSavePathFile ,'wb'))
    pickle.dump( ontology , open( ontologyPathFile ,'wb'))
    
    print "S'han creat correctament els arxius annotation i ontology, ja no cal fer-ho més"

# Perque funcioni correctament s'ha de posar la seguent ordre en comptes de la que havia
main()
    
