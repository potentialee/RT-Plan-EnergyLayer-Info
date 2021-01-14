# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:41:19 2021

@author: Chanil
"""

import pydicom
import os
        
nominalEnergyList_beam1 = []
nominalEnergyList_beam2 = []
nominalEnergyList_beam3 = []

MUlist_beam1 = []
MUlist_beam2 = []
MUlist_beam3 = []

# Get RT plan file
for files in os.listdir(os.getcwd()) :
    if (files.startswith('RP') and files.endswith('.dcm')) :
        rtplanDataset = pydicom.dcmread(files)
        
# Get nominal energy and each layer's MU value
for beam in rtplanDataset.IonBeamSequence :
    beamNumber = beam.BeamNumber
    if (beamNumber == 1):
        for i in range(0 , len(beam.IonControlPointSequence)-1) :
            # First, get cumulative meterset weight and subtract last one
            if(i < 1) :
                nominalEnergyList_beam1.append(float(beam.IonControlPointSequence[i].NominalBeamEnergy))
                MUlist_beam1.append(float(beam.IonControlPointSequence[i].CumulativeMetersetWeight))
            elif(i >= 1) :
                if (float(beam.IonControlPointSequence[i].NominalBeamEnergy) != float(beam.IonControlPointSequence[i-1].NominalBeamEnergy)) :
                    nominalEnergyList_beam1.append(float(beam.IonControlPointSequence[i].NominalBeamEnergy))
                MUlist_beam1.append(float(beam.IonControlPointSequence[i].CumulativeMetersetWeight) - float(beam.IonControlPointSequence[i-1].CumulativeMetersetWeight))
        # zero value delete in MU list
        for item in MUlist_beam1 :
            if item == 0:
                MUlist_beam1.remove(0)
        
        print("## FIELD 1 NOMINAL ENERGY ##")
        print(nominalEnergyList_beam1)
        print("")
                
        print("## FIELD 1 MU LIST PER ENERGY ##")
        print(MUlist_beam1)
        print("")
                
    if (beamNumber == 2):
        for i in range(0 , len(beam.IonControlPointSequence)-1) :
            if(i < 1) :
                nominalEnergyList_beam2.append(float(beam.IonControlPointSequence[i].NominalBeamEnergy))
                MUlist_beam2.append(float(beam.IonControlPointSequence[i].CumulativeMetersetWeight))
            elif(i >= 1) :
                if (float(beam.IonControlPointSequence[i].NominalBeamEnergy) != float(beam.IonControlPointSequence[i-1].NominalBeamEnergy)) :
                    nominalEnergyList_beam2.append(float(beam.IonControlPointSequence[i].NominalBeamEnergy))
                MUlist_beam2.append(float(beam.IonControlPointSequence[i].CumulativeMetersetWeight) - float(beam.IonControlPointSequence[i-1].CumulativeMetersetWeight))
        for item in MUlist_beam2 :
            if item == 0:
                MUlist_beam2.remove(0)
        
        print("## FIELD 2 NOMINAL ENERGY ##")
        print(nominalEnergyList_beam2)
        print("")
                
        print("## FIELD 2 MU LIST PER ENERGY ##")
        print(MUlist_beam2)
        print("")
            
    if (beamNumber == 3):
        for i in range(0 , len(beam.IonControlPointSequence)-1) :
            if(i < 1) :
                nominalEnergyList_beam3.append(float(beam.IonControlPointSequence[i].NominalBeamEnergy))
                MUlist_beam3.append(float(beam.IonControlPointSequence[i].CumulativeMetersetWeight))
            elif(i >= 1) :
                if (float(beam.IonControlPointSequence[i].NominalBeamEnergy) != float(beam.IonControlPointSequence[i-1].NominalBeamEnergy)) :
                    nominalEnergyList_beam3.append(float(beam.IonControlPointSequence[i].NominalBeamEnergy))
                MUlist_beam3.append(float(beam.IonControlPointSequence[i].CumulativeMetersetWeight) - float(beam.IonControlPointSequence[i-1].CumulativeMetersetWeight))
        for item in MUlist_beam3 :
            if item == 0:
                MUlist_beam3.remove(0)
        
        print("## FIELD 3 NOMINAL ENERGY ##")
        print(nominalEnergyList_beam3)
        print("")
        
        print("## FIELD 3 MU LIST PER ENERGY ##")
        print(MUlist_beam3)
        print("")
    