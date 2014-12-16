# Evaluation paquet
import os
import pickle  
import getopt
import sys
from sklearn import metrics
from modules.classification.LabelType import LabelType
from modules.classification.Annotation import Annotation

class Evaluator:
    """ This class provides some utils to evaluate the predicted results from Detector class,
        geting two Annotations, GroundTruth and the prectited from Detector"""
    
    def __init__(self, pathGroundTruthAnnotation, 
                        pathPredictedAnnotation,
                        pathOntology,
                        flagSaveInMemory=False, 
                        flagVerbose=False,
                        flagRunOnServer=False):
        
        # Load the created ontology 
        self.ontology = pickle.load( open( pathOntology, "rb" ))
        
        # Init Annotation, both, GroundTruth and Predicted
        self.groundTruthAnnotation = Annotation(self.ontology)
        self.predictedAnnotation = Annotation(self.ontology)
        

        gtFile = open ( pathGroundTruthAnnotation, 'rb')
        resultsFile=open(pathPredictedAnnotation,'rb')
        
        # load annotation objects
        self.groundTruthAnnotation=pickle.load(gtFile)
        self.predictedAnnotation  =pickle.load(resultsFile)
        
        self.listGt=[]
        self.listResults=[]
        
        self.flagSaveInMemory = flagSaveInMemory
        self.flagVerbose = flagVerbose
        self.flagRunOnServer = flagRunOnServer
        


    
    def buildDataList(self, pathTxtFile):
        
        if self.flagVerbose:
            print 'Reading images from ' + pathTxtFile + "..."
        
        # Read the file containing the image IDs
        fileDataset = open( pathTxtFile, 'r')
        
        # Read lines from the text file, stripping the end of line character
        imageIds = [line.strip() for line in fileDataset ]
        
        # Close file
        fileDataset.close()
        
        # build a each list of classNames belongs imageId in paralel to obtain the same list position for eash imageId
        for docId in imageIds:
            
            # Process the collection of image IDs
            self.listGt.append( self.groundTruthAnnotation.getAnnotatedClasses( LabelType.POSITIVE, docId))
            self.listResults.append(self.predictedAnnotation.getAnnotatedClasses( LabelType.POSITIVE, docId))
        print self.groundTruthAnnotation.getAnnotatedClasses( LabelType.POSITIVE, docId)

    def accuracyScore( self ):
        return metrics.accuracy_score( self.listGt, self.listResults )
        
    def precisionScore( self ):
        return metrics.precision_score( self.listGt, self.listResults,average='weighted' )
    
    def recallScore( self ):
        return metrics.recall_score( self.listGt, self.listResults )
        
    def F1Score( self ):
        return metrics.f1_score( self.listGt, self.listResults )
    
    def classificationReport(self):
        target_names = self.groundTruthAnnotation.getSemanticClassNames()
        return metrics.classification_report( self.listGt, self.listResults, target_names = target_names)
        
    def getListResults(self):
        return self.listResults
 
    def getListGt(self):
        return self.listGt   
        
# Script usage        
def usage():
    print "This script provides some evaluation tools"
