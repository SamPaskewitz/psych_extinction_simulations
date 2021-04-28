"""
Models for extinction project (dissertation) simulations.
All of these use the rectified prediction function.
"""
from statsrat import rw

elem = rw.model(name = 'elem',
                pred = rw.pred.rectified,
                fbase = rw.fbase.elem,
                fweight = rw.fweight.none,
                lrate = rw.lrate.cnst,
                drate = rw.drate.zero,
                aux = rw.aux.basic)

power = rw.model(name = 'power',
                pred = rw.pred.rectified,
                fbase = rw.fbase.elem,
                fweight = rw.fweight.none,
                lrate = rw.lrate.power,
                drate = rw.drate.zero,
                aux = rw.aux.basic)

tdrva = rw.model(name = 'tdrva',
                pred = rw.pred.rectified,
                fbase = rw.fbase.elem,
                fweight = rw.fweight.none,
                lrate = rw.lrate.from_aux_feature_simple,
                drate = rw.drate.zero,
                aux = rw.aux.tdrva)

tdrva_cfg2 = rw.model(name = 'tdrva_cfg2',
                      pred = rw.pred.rectified,
                      fbase = rw.fbase.cfg2,
                      fweight = rw.fweight.none,
                      lrate = rw.lrate.from_aux_feature_simple,
                      drate = rw.drate.zero,
                      aux = rw.aux.tdrva)

tdrva_decay = rw.model(name = 'tdrva_decay',
                       pred = rw.pred.rectified,
                       fbase = rw.fbase.elem,
                       fweight = rw.fweight.none,
                       lrate = rw.lrate.from_aux_feature_simple,
                       drate = rw.drate.only_neg,
                       aux = rw.aux.tdrva)

tdrva_decay_cfg2 = rw.model(name = 'tdrva_decay_cfg2',
                            pred = rw.pred.rectified,
                            fbase = rw.fbase.cfg2,
                            fweight = rw.fweight.none,
                            lrate = rw.lrate.from_aux_feature_simple,
                            drate = rw.drate.only_neg,
                            aux = rw.aux.tdrva)

decay = rw.model(name = 'decay',
                pred = rw.pred.rectified,
                fbase = rw.fbase.elem,
                fweight = rw.fweight.none,
                lrate = rw.lrate.cnst,
                drate = rw.drate.only_neg,
                aux = rw.aux.basic)

power_decay = rw.model(name = 'power_decay',
                       pred = rw.pred.rectified,
                       fbase = rw.fbase.elem,
                       fweight = rw.fweight.none,
                       lrate = rw.lrate.power,
                       drate = rw.drate.only_neg,
                       aux = rw.aux.basic)

cfg2 = rw.model(name = 'cfg2',
                 pred = rw.pred.rectified,
                 fbase = rw.fbase.cfg2,
                 fweight = rw.fweight.none,
                 lrate = rw.lrate.cnst,
                 drate = rw.drate.zero,
                 aux = rw.aux.basic)

refined = rw.model(name = 'refined', # Combines decay, power and cfg2.
                   pred = rw.pred.rectified,
                   fbase = rw.fbase.cfg2,
                   fweight = rw.fweight.none,
                   lrate = rw.lrate.power,
                   drate = rw.drate.only_neg,
                   aux = rw.aux.basic)

CompAct_decay = rw.model(name = 'CompAct_decay',
                         pred = rw.pred.rectified,
                         fbase = rw.fbase.elem,
                         fweight = rw.fweight.from_aux_norm,
                         lrate = rw.lrate.from_aux_norm,
                         drate = rw.drate.only_neg,
                         aux = rw.aux.gradcomp)

CompAct_decay_cfg2 = rw.model(name = 'CompAct_decay_cfg2',
                              pred = rw.pred.rectified,
                              fbase = rw.fbase.cfg2,
                              fweight = rw.fweight.from_aux_norm,
                              lrate = rw.lrate.from_aux_norm,
                              drate = rw.drate.only_neg,
                              aux = rw.aux.gradcomp)

revised_CompAct = rw.model(name = 'revised_CompAct', # combines CompAct, power law learning rates, decay and cfg2.
                           pred = rw.pred.rectified,
                           fbase = rw.fbase.cfg2,
                           fweight = rw.fweight.from_aux_norm,
                           lrate = rw.lrate.power_from_aux_norm,
                           drate = rw.drate.only_neg,
                           aux = rw.aux.gradcomp_feature_counts)