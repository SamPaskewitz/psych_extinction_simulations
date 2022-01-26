from statsrat import exemplar

null = exemplar.model(name = 'null',
                      sim = exemplar.sim.Gaussian,
                      rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                      atn_update = exemplar.atn_update.null,
                      y_ex_update = exemplar.y_ex_update.ex_mean)
                       
grad = exemplar.model(name = 'grad',
                      sim = exemplar.sim.Gaussian,
                      rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                      atn_update = exemplar.atn_update.gradient_ngsec,
                      y_ex_update = exemplar.y_ex_update.ex_mean)
    
grad_common = exemplar.model(name = 'grad_common',
                             sim = exemplar.sim.Gaussian,
                             rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                             atn_update = exemplar.atn_update.gradient_ngsec_common,
                             y_ex_update = exemplar.y_ex_update.ex_mean)

# Come to think of it, with x values of 0 and 1 this won't work any differently from grad_common (with Gaussian similarity).
grad_cityblock_common = exemplar.model(name = 'grad_cityblock_common',
                                       sim = exemplar.sim.city_block,
                                       rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                                       atn_update = exemplar.atn_update.gradient_norm_cityblock_common,
                                       y_ex_update = exemplar.y_ex_update.ex_mean)

grad_both = exemplar.model(name = 'grad_both',
                           sim = exemplar.sim.Gaussian,
                           rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                           atn_update = exemplar.atn_update.gradient_ngsec_both,
                           y_ex_update = exemplar.y_ex_update.ex_mean)

heuristic = exemplar.model(name = 'heuristic',
                           sim = exemplar.sim.Gaussian,
                           rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                           atn_update = exemplar.atn_update.heuristic,
                           y_ex_update = exemplar.y_ex_update.ex_mean)