# You will need separate scenarios HERE for full and fast. DON'T CHANGE THE ORDER, only
# append new keys. Otherwise the numbering for the runTheMatrix tests will change.
upgradeKeys=['2017',
             '2019',
             'BE5D',
             '2017dev',
             'Extended2023Muondev',
             'BE5DPixel10DLHCCCooling',
             '2019WithGEM',
             'BE5DPixel10D',
             '2017Aging',
             '2019WithGEMAging',
             'Extended2023',
             'Extended2023HGCalMuon',
             'Extended2023SHCal',
             'Extended2023SHCal4Eta',
             'Extended2023TTI',
             'Extended2023Muon',
             'Extended2023HGCalV6Muon',
             'Extended2023SHCalNoTaperNoExtPix',
             'Extended2023Pixel',
             'Extended2023SHCalNoTaper',
             'Extended2023SHCalNoTaper4Eta',
             'Extended2023HGCal',
             'Extended2023HGCalMuon4Eta',
             'BE5DPixel10DLHCC',
             'Extended2023HGCalV4',
             'Extended2023HGCalMuonPU',
             'Extended2023SHCalNoTaperPU',
             '2019WithGEMAgingPU',
             'Extended2023HGCalMuonPandora',
             'Extended2023HGCalMuonPandoraPU'
         ]


upgradeGeoms={ '2017' : 'Extended2017',
               '2019' : 'Extended2019',
               '2019WithGEM' : 'Extended2019',
               '2017Aging' : 'Extended2017',
               '2019WithGEMAging' : 'Extended2019',
               'BE5D' : 'ExtendedPhase2TkBE5D',
               'BE5DPixel10D' : 'ExtendedPhase2TkBE5DPixel10D',
               '2017dev' : 'Extended2017dev,Extended2017devReco',
               'Extended2023Muondev' : 'Extended2023Muondev,Extended2023MuondevReco',
               'BE5DPixel10DLHCCCooling' : 'ExtendedPhase2TkBE5DPixel10DLHCC',
               'Extended2023' : 'Extended2023,Extended2023Reco',
               'Extended2023HGCalMuon' : 'Extended2023HGCalMuon,Extended2023HGCalMuonReco',
               'Extended2023SHCal' : 'Extended2023SHCal,Extended2023SHCalReco',
               'Extended2023SHCal4Eta' : 'Extended2023SHCal4Eta,Extended2023SHCal4EtaReco',
               'Extended2023TTI' : 'Extended2023TTI,Extended2023TTIReco',
               'Extended2023Muon' : 'Extended2023Muon,Extended2023MuonReco',
               'BE5DPixel10DLHCC' : 'ExtendedPhase2TkBE5DPixel10DLHCC',
               'Extended2023HGCalV6Muon' : 'Extended2023HGCalV6Muon,Extended2023HGCalV6MuonReco',
               'Extended2023SHCalNoTaperNoExtPix' : 'Extended2023SHCalNoTaperNoExtPix',
               'Extended2023Pixel' : 'Extended2023Pixel,Extended2023PixelReco',
               'Extended2023SHCalNoTaper' : 'Extended2023SHCalNoTaper,Extended2023SHCalNoTaperReco',
               'Extended2023SHCalNoTaper4Eta' : 'Extended2023SHCalNoTaper4Eta,Extended2023SHCalNoTaper4EtaReco',
               'Extended2023HGCal' : 'Extended2023HGCal,Extended2023HGCalReco',
               'Extended2023HGCalMuon4Eta' : 'Extended2023HGCalMuon4Eta,Extended2023HGCalMuon4EtaReco',
               'Extended2023HGCalV4' : 'Extended2023HGCalV4Muon,Extended2023HGCalV4MuonReco',
               'Extended2023HGCalMuonPandora' : 'Extended2023HGCalMuon,Extended2023HGCalMuonReco'
               }
upgradeGTs={ '2017' : 'auto:upgrade2017',
             '2019' : 'auto:upgrade2019',
             '2019WithGEM' : 'auto:upgrade2019',
             '2017Aging' : 'W17_300_62E2::All',
             '2019WithGEMAging' : 'PH1_1K_FB_V3::All',#EB aged at 1000fb-1
             'BE5D' : 'auto:upgradePLS3',
             'BE5DPixel10D' : 'auto:upgradePLS3',
             '2017dev' : 'auto:upgrade2017',
             'Extended2023Muondev' : 'auto:upgradePLS3',
             'BE5DPixel10DLHCCCooling' : 'auto:upgradePLS3',
             'Extended2023' : 'auto:upgradePLS3',
             'Extended2023HGCalMuon' : 'PH2_1K_FB_V6::All', #EB aged at 1000fb-1
             'Extended2023SHCal' : 'auto:upgradePLS3',
             'Extended2023SHCal4Eta' : 'auto:upgradePLS3',
             'Extended2023TTI' : 'auto:upgradePLS3',
             'Extended2023Muon' : 'auto:upgradePLS3',
             'BE5DPixel10DLHCC' : 'auto:upgradePLS3',
             'Extended2023HGCalV6Muon' : 'PH2_1K_FB_V6::All', #EB aged at 1000fb-1
             'Extended2023SHCalNoTaperNoExtPix' : 'auto:upgradePLS3',
             'Extended2023Pixel' : 'auto:upgradePLS3',
             'Extended2023SHCalNoTaper' : 'PH2_1K_FB_V6::All',#EB aged at 1000fb-1
             'Extended2023SHCalNoTaper4Eta' : 'auto:upgradePLS3',
             'Extended2023HGCal' : 'auto:upgradePLS3',
             'Extended2023HGCalMuon4Eta' : 'auto:upgradePLS3',
             'Extended2023HGCalV4' : 'auto:upgradePLS3',
             'Extended2023HGCalMuonPandora' : 'PH2_1K_FB_V6::All' #EB aged at 1000fb-1
             }
upgradeCustoms={ '2017' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2017',
                 '2019' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2019',
                 '2019WithGEM' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2019WithGem',
                 '2017Aging' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2017,SLHCUpgradeSimulations/Configuration/aging.customise_aging_300',
                 '2019WithGEMAging' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2019WithGem,SLHCUpgradeSimulations/Configuration/aging.customise_aging_newpixel_1000',
                 'BE5D' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_phase2_BE5D',
                 'BE5DPixel10D' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_phase2_BE5DPixel10D',
                 '2017dev' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2017dev',
                 'Extended2023Muondev' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023Muondev',
                 'BE5DPixel10DLHCCCooling' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_phase2_BE5DPixel10DLHCCCooling',
                 'Extended2023' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023',
                 'Extended2023HGCalMuon' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023HGCalMuon',
                 'Extended2023SHCal' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023SHCal',
                 'Extended2023SHCal4Eta' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023SHCal',
                 'Extended2023TTI' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023TTI',
                 'Extended2023Muon' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023Muon',
                 'BE5DPixel10DLHCC' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_phase2_BE5DPixel10DLHCC',
                 'Extended2023HGCalV6Muon' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023HGCalV6Muon',
                 'Extended2023SHCalNoTaperNoExtPix' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023SHCalNoExtPix',
                 'Extended2023Pixel' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023Pixel',
                 'Extended2023SHCalNoTaper' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023SHCal',
                 'Extended2023SHCalNoTaper4Eta' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023SHCal',
                 'Extended2023HGCal' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023HGCal',
                 'Extended2023HGCalMuon4Eta' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023HGCalMuon',
                 'Extended2023HGCalV4' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023HGCalMuon',
                 'Extended2023HGCalMuonPandora' : 'RecoParticleFlow/PandoraTranslator/customizeHGCalPandora_cff.cust_2023HGCalPandoraMuon'
                 }

upgradeFragments=['FourMuPt_1_200_cfi','SingleElectronPt10_cfi',
                  'SingleElectronPt35_cfi','SingleElectronPt1000_cfi',
                  'SingleGammaPt10_cfi','SingleGammaPt35_cfi','SingleMuPt1_cfi','SingleMuPt10_cfi',
                  'SingleMuPt100_cfi','SingleMuPt1000_cfi','TTbarLepton_Tauola_8TeV_cfi','Wjet_Pt_80_120_8TeV_cfi',
                  'Wjet_Pt_3000_3500_8TeV_cfi','LM1_sfts_8TeV_cfi','QCD_Pt_3000_3500_8TeV_cfi','QCD_Pt_600_800_8TeV_cfi',
                  'QCD_Pt_80_120_8TeV_cfi','H200ChargedTaus_Tauola_8TeV_cfi','JpsiMM_8TeV_cfi','TTbar_Tauola_8TeV_cfi',
                  'WE_8TeV_cfi','ZEE_8TeV_cfi','ZTT_Tauola_All_hadronic_8TeV_cfi','H130GGgluonfusion_8TeV_cfi',
                  'PhotonJet_Pt_10_8TeV_cfi','QQH1352T_Tauola_8TeV_cfi','MinBias_TuneZ2star_8TeV_pythia6_cff','WM_8TeV_cfi',
                  'ZMM_8TeV_cfi','ADDMonoJet_8TeV_d3MD3_cfi','ZpMM_8TeV_cfi','WpM_8TeV_cfi',
                  'Wjet_Pt_80_120_14TeV_cfi','Wjet_Pt_3000_3500_14TeV_cfi','LM1_sfts_14TeV_cfi','QCD_Pt_3000_3500_14TeV_cfi',
                  'QCD_Pt_80_120_14TeV_cfi','H200ChargedTaus_Tauola_14TeV_cfi','JpsiMM_14TeV_cfi','TTbar_Tauola_14TeV_cfi',
                  'WE_14TeV_cfi','ZEE_14TeV_cfi','ZTT_Tauola_All_hadronic_14TeV_cfi','H130GGgluonfusion_14TeV_cfi',
                  'PhotonJet_Pt_10_14TeV_cfi','QQH1352T_Tauola_14TeV_cfi',
                  'MinBias_TuneZ2star_14TeV_pythia6_cff','WM_14TeV_cfi','ZMM_14TeV_cfi',
                  'FourMuExtendedPt_1_200_cfi',
                  'TenMuExtendedE_0_200_cfi',
                  'SingleElectronPt10Extended_cfi',
                  'SingleElectronPt35Extended_cfi',
                  'SingleElectronPt1000Extended_cfi',
                  'SingleGammaPt10Extended_cfi',
                  'SingleGammaPt35Extended_cfi',
                  'SingleMuPt1Extended_cfi',
                  'SingleMuPt10Extended_cfi',
                  'SingleMuPt100Extended_cfi',
                  'SingleMuPt1000Extended_cfi',
                  'TenMuE_0_200_cfi',
                  'SinglePiE50HCAL_cfi',
                  'QCDForPF_14TeV_cfi',
                  'DYToLL_M_50_TuneZ2star_14TeV_pythia6_tauola_cff',
                  'DYtoTauTau_M_50_TuneD6T_14TeV_pythia6_tauola_cff'          ]



### remember that you need to add a new step for phase 2 to include the track trigger
### remember that you need to add fastsim

# step1 is normal gen-sim
# step2 is digi
# step3 is reco
# step4 is harvest
# step5 is digi+l1tracktrigger
# step6 is fastsim
# step7 is fastsim harvesting
upgradeSteps=['GenSimFull','GenSimHLBeamSpotFull','DigiFull','RecoFull','RecoFullHGCAL','HARVESTFull','DigiTrkTrigFull','FastSim','HARVESTFast','DigiFullPU','RecoFullPU','RecoFullPUHGCAL','HARVESTFullPU','DigiFullTrigger']

upgradeScenToRun={ '2017':['GenSimFull','DigiFull','RecoFull','HARVESTFull'],
                   '2019':['GenSimFull','DigiFull','RecoFull','HARVESTFull'],
                   '2019WithGEM':['GenSimFull','DigiFull','RecoFull','HARVESTFull'],
                   '2017Aging':['GenSimFull','DigiFull','RecoFull','HARVESTFull'],
                   '2019WithGEMAging':['GenSimFull','DigiFull','RecoFull','HARVESTFull'],
                   'BE5D':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'BE5DPixel10D':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   '2017dev':['GenSimFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023Muondev':['GenSimHLBeamSpotFull','DigiFullTrigger','RecoFull','HARVESTFull'],
                   'BE5DPixel10DLHCCCooling':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023HGCalMuon':['GenSimHLBeamSpotFull','DigiFull','RecoFullHGCAL'],
                   'Extended2023SHCal':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023SHCal4Eta':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023TTI':['GenSimHLBeamSpotFull','DigiTrkTrigFull'], ##no need to go beyond local reco
                   'Extended2023Muon':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'BE5DPixel10DLHCC':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023HGCalV6Muon':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023SHCalNoTaperNoExtPix':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023Pixel':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023SHCalNoTaper':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023SHCalNoTaper4Eta':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023HGCal':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023HGCalMuon4Eta':['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023HGCalV4' : ['GenSimHLBeamSpotFull','DigiFull','RecoFull','HARVESTFull'],
                   'Extended2023HGCalMuonPU' : ['GenSimHLBeamSpotFull','DigiFullPU','RecoFullPUHGCAL'],
                   'Extended2023SHCalNoTaperPU' : ['GenSimHLBeamSpotFull','DigiFullPU','RecoFullPU','HARVESTFullPU'],
                   '2019WithGEMAgingPU':['GenSimFull','DigiFullPU','RecoFullPU','HARVESTFullPU'],
                   'Extended2023HGCalMuonPandora':['GenSimHLBeamSpotFull','DigiFull','RecoFullHGCAL'],
                   'Extended2023HGCalMuonPandoraPU' : ['GenSimHLBeamSpotFull','DigiFullPU','RecoFullPUHGCAL']
                   }

from  Configuration.PyReleaseValidation.relval_steps import Kby

howMuches={'FourMuPt_1_200_cfi':Kby(10,100),
           'TenMuE_0_200_cfi':Kby(10,100),
           'FourMuExtendedPt_1_200_cfi':Kby(10,100),
           'TenMuExtendedE_0_200_cfi':Kby(10,100),
           'SingleElectronPt10_cfi':Kby(9,100),
           'SingleElectronPt35_cfi':Kby(9,100),
           'SingleElectronPt1000_cfi':Kby(9,50),
           'SingleGammaPt10_cfi':Kby(9,100),
           'SingleGammaPt35_cfi':Kby(9,50),
           'SingleMuPt1_cfi':Kby(25,100),
           'SingleMuPt10_cfi':Kby(25,100),
           'SingleMuPt100_cfi':Kby(9,100),
           'SingleMuPt1000_cfi':Kby(9,100),
           'SingleElectronPt10Extended_cfi':Kby(9,100),
           'SingleElectronPt35Extended_cfi':Kby(9,100),
           'SingleElectronPt1000Extended_cfi':Kby(9,50),
           'SingleGammaPt10Extended_cfi':Kby(9,100),
           'SingleGammaPt35Extended_cfi':Kby(9,50),
           'SingleMuPt1Extended_cfi':Kby(25,100),
           'SingleMuPt10Extended_cfi':Kby(25,100),
           'SingleMuPt100Extended_cfi':Kby(9,100),
           'SingleMuPt1000Extended_cfi':Kby(9,100),
           'SinglePiE50HCAL_cfi':Kby(10,100),
           'TTbarLepton_Tauola_8TeV_cfi':Kby(9,100),
           'Wjet_Pt_80_120_8TeV_cfi':Kby(9,100),
           'Wjet_Pt_3000_3500_8TeV_cfi':Kby(9,50),
           'LM1_sfts_8TeV_cfi':Kby(9,100),
           'QCD_Pt_3000_3500_8TeV_cfi':Kby(9,50),
           'QCD_Pt_600_800_8TeV_cfi':Kby(9,50),
           'QCD_Pt_80_120_8TeV_cfi':Kby(9,100),
           'H200ChargedTaus_Tauola_8TeV_cfi':Kby(9,100),
           'JpsiMM_8TeV_cfi':Kby(66,100),
           'TTbar_Tauola_8TeV_cfi':Kby(9,100),
           'WE_8TeV_cfi':Kby(9,100),
           'ZEE_8TeV_cfi':Kby(9,100),
           'ZTT_Tauola_All_hadronic_8TeV_cfi':Kby(9,100),
           'H130GGgluonfusion_8TeV_cfi':Kby(9,100),
           'PhotonJet_Pt_10_8TeV_cfi':Kby(9,100),
           'QQH1352T_Tauola_8TeV_cfi':Kby(9,100),
           'MinBias_TuneZ2star_8TeV_pythia6_cff':Kby(9,30),
           'WM_8TeV_cfi':Kby(9,100),
           'ZMM_8TeV_cfi':Kby(18,100),
           'ADDMonoJet_8TeV_d3MD3_cfi':Kby(9,100),
           'ZpMM_8TeV_cfi':Kby(9,100),
           'WpM_8TeV_cfi':Kby(9,100),
           'Wjet_Pt_80_120_14TeV_cfi':Kby(9,100),
           'Wjet_Pt_3000_3500_14TeV_cfi':Kby(9,50),
           'LM1_sfts_14TeV_cfi':Kby(9,100),
           'QCD_Pt_3000_3500_14TeV_cfi':Kby(9,50),
           'QCD_Pt_80_120_14TeV_cfi':Kby(9,100),
           'H200ChargedTaus_Tauola_14TeV_cfi':Kby(9,100),
           'JpsiMM_14TeV_cfi':Kby(66,100),
           'TTbar_Tauola_14TeV_cfi':Kby(9,100),
           'WE_14TeV_cfi':Kby(9,100),
           'ZEE_14TeV_cfi':Kby(9,100),
           'ZTT_Tauola_All_hadronic_14TeV_cfi':Kby(9,100),
           'H130GGgluonfusion_14TeV_cfi':Kby(9,100),
           'PhotonJet_Pt_10_14TeV_cfi':Kby(9,100),
           'QQH1352T_Tauola_14TeV_cfi':Kby(9,100),
           'MinBias_TuneZ2star_14TeV_pythia6_cff':Kby(9,100),
           'WM_14TeV_cfi':Kby(9,100),
           'ZMM_14TeV_cfi':Kby(18,100),
            'QCDForPF_14TeV_cfi':Kby(9,50),
            'DYToLL_M_50_TuneZ2star_14TeV_pythia6_tauola_cff':Kby(9,100),
            'DYtoTauTau_M_50_TuneD6T_14TeV_pythia6_tauola_cff':Kby(9,100)
           }

upgradeDatasetFromFragment={'FourMuPt_1_200_cfi': 'FourMuPt1_200',
                            'FourMuExtendedPt_1_200_cfi': 'FourMuExtendedPt1_200',
                            'TenMuE_0_200_cfi': 'TenMuE_0_200',
                            'TenMuExtendedE_0_200_cfi': 'TenMuExtendedE_0_200',
                            'SingleElectronPt10_cfi' : 'SingleElectronPt10',
                            'SingleElectronPt35_cfi' : 'SingleElectronPt35',
                            'SingleElectronPt1000_cfi' : 'SingleElectronPt1000',
                            'SingleGammaPt10_cfi' : 'SingleGammaPt10',
                            'SingleGammaPt35_cfi' : 'SingleGammaPt35',
                            'SingleMuPt1_cfi' : 'SingleMuPt1',
                            'SingleMuPt10_cfi' : 'SingleMuPt10',
                            'SingleMuPt100_cfi' : 'SingleMuPt100',
                            'SingleMuPt1000_cfi' : 'SingleMuPt1000',
                            'SingleElectronPt10Extended_cfi' : 'SingleElectronPt10Extended',
                            'SingleElectronPt35Extended_cfi' : 'SingleElectronPt35Extended',
                            'SingleElectronPt1000Extended_cfi' : 'SingleElectronPt1000Extended',
                            'SingleGammaPt10Extended_cfi' : 'SingleGammaPt10Extended',
                            'SingleGammaPt35Extended_cfi' : 'SingleGammaPt35Extended',
                            'SingleMuPt1Extended_cfi' : 'SingleMuPt1Extended',
                            'SingleMuPt10Extended_cfi' : 'SingleMuPt10Extended',
                            'SingleMuPt100Extended_cfi' : 'SingleMuPt100Extended',
                            'SingleMuPt1000Extended_cfi' : 'SingleMuPt1000Extended',
                            'SinglePiE50HCAL_cfi' : 'SinglePiE50HCAL',
                            'TTbarLepton_Tauola_8TeV_cfi' : 'TTbarLepton_8TeV',
                            'Wjet_Pt_80_120_8TeV_cfi' : 'Wjet_Pt_80_120_8TeV',
                            'Wjet_Pt_3000_3500_8TeV_cfi' : 'Wjet_Pt_3000_3500_8TeV',
                            'LM1_sfts_8TeV_cfi' : 'LM1_sfts_8TeV',
                            'QCD_Pt_3000_3500_8TeV_cfi' : 'QCD_Pt_3000_3500_8TeV',
                            'QCD_Pt_600_800_8TeV_cfi' : 'QCD_Pt_600_800_8TeV',
                            'QCD_Pt_80_120_8TeV_cfi' : 'QCD_Pt_80_120_8TeV',
                            'H200ChargedTaus_Tauola_8TeV_cfi' : 'Higgs200ChargedTaus_8TeV',
                            'JpsiMM_8TeV_cfi' : 'JpsiMM_8TeV',
                            'TTbar_Tauola_8TeV_cfi' : 'TTbar_8TeV',
                            'WE_8TeV_cfi' : 'WE_8TeV',
                            'ZEE_8TeV_cfi' : 'ZEE_8TeV',
                            'ZTT_Tauola_All_hadronic_8TeV_cfi' : 'ZTT_8TeV',
                            'H130GGgluonfusion_8TeV_cfi' : 'H130GGgluonfusion_8TeV',
                            'PhotonJet_Pt_10_8TeV_cfi' : 'PhotonJets_Pt_10_8TeV',
                            'QQH1352T_Tauola_8TeV_cfi' : 'QQH1352T_Tauola_8TeV',
                            'MinBias_TuneZ2star_8TeV_pythia6_cff': 'MinBias_TuneZ2star_8TeV',
                            'WM_8TeV_cfi' : 'WM_8TeV',
                            'ZMM_8TeV_cfi' : 'ZMM_8TeV',
                            'ADDMonoJet_8TeV_d3MD3_cfi' : 'ADDMonoJet_d3MD3_8TeV',
                            'ZpMM_8TeV_cfi' : 'ZpMM_8TeV',
                            'WpM_8TeV_cfi' : 'WpM_8TeV',
                            'Wjet_Pt_80_120_14TeV_cfi' : 'Wjet_Pt_80_120_14TeV',
                            'Wjet_Pt_3000_3500_14TeV_cfi' : 'Wjet_Pt_3000_3500_14TeV',
                            'LM1_sfts_14TeV_cfi' : 'LM1_sfts_14TeV',
                            'QCD_Pt_3000_3500_14TeV_cfi' : 'QCD_Pt_3000_3500_14TeV',
                            'QCD_Pt_80_120_14TeV_cfi' : 'QCD_Pt_80_120_14TeV',
                            'H200ChargedTaus_Tauola_14TeV_cfi' : 'Higgs200ChargedTaus_14TeV',
                            'JpsiMM_14TeV_cfi' : 'JpsiMM_14TeV',
                            'TTbar_Tauola_14TeV_cfi' : 'TTbar_14TeV',
                            'WE_14TeV_cfi' : 'WE_14TeV',
                            'ZEE_14TeV_cfi' : 'ZEE_14TeV',
                            'ZTT_Tauola_All_hadronic_14TeV_cfi' : 'ZTT_14TeV',
                            'H130GGgluonfusion_14TeV_cfi' : 'H130GGgluonfusion_14TeV',
                            'PhotonJet_Pt_10_14TeV_cfi' : 'PhotonJets_Pt_10_14TeV',
                            'QQH1352T_Tauola_14TeV_cfi' : 'QQH1352T_Tauola_14TeV',
                            'MinBias_TuneZ2star_14TeV_pythia6_cff' : 'MinBias_TuneZ2star_14TeV',
                            'WM_14TeV_cfi' : 'WM_14TeV',
                            'ZMM_14TeV_cfi' : 'ZMM_14TeV',
                            'QCDForPF_14TeV_cfi' : 'QCDForPF_14TeV',
                            'DYToLL_M_50_TuneZ2star_14TeV_pythia6_tauola_cff' : 'DYToLL_M_50_TuneZ2star_14TeV',
                            'DYtoTauTau_M_50_TuneD6T_14TeV_pythia6_tauola_cff' : 'DYtoTauTau_M_50_TuneD6T_14TeV'
                            }



#just do everything...
