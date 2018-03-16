import FWCore.ParameterSet.Config as cms
process = cms.Process("ProcessOne")
process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.CondDBCommon.connect = 'sqlite_file:lhcinfo_pop_test.db'
process.CondDBCommon.DBParameters.authenticationPath = '.'
process.CondDBCommon.DBParameters.messageLevel=cms.untracked.int32(1)

process.MessageLogger = cms.Service("MessageLogger",
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('INFO')),
                                    destinations = cms.untracked.vstring('cout')
                                    )

process.source = cms.Source("EmptyIOVSource",
                            lastValue = cms.uint64(1),
                            timetype = cms.string('runnumber'),
                            firstValue = cms.uint64(1),
                            interval = cms.uint64(1)
                            )

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDBCommon,
                                          logconnect = cms.untracked.string('sqlite_file:loglhcinfo_pop_test.db'),
                                          timetype = cms.untracked.string('timestamp'),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('LHCInfoRcd'),
                                                                     tag = cms.string('lhcinfo_test')
                                                                     )
                                                            )
                                          )

process.Test1 = cms.EDAnalyzer("LHCInfoPopConAnalyzer",
                               SinceAppendMode = cms.bool(True),
                               record = cms.string('LHCInfoRcd'),
                               name = cms.untracked.string('LHCInfo'),
                               Source = cms.PSet(fill = cms.untracked.uint32(6303),
                                   firstFill = cms.untracked.uint32( 6309 ),
                                   lastFill = cms.untracked.uint32( 6310 ),
                                   connectionString = cms.untracked.string("oracle://cms_orcon_adg/CMS_RUNTIME_LOGGER"),
                                   DIPSchema = cms.untracked.string("CMS_BEAM_COND"),
                                   authenticationPath =  cms.untracked.string("/afs/cern.ch/user/a/anoolkar/private"),
                                   debug=cms.untracked.bool(False)
                                                 ),
                               loggingOn = cms.untracked.bool(True),
                               IsDestDbCheckedInQueryLog = cms.untracked.bool(False)
                               )

process.p = cms.Path(process.Test1)
