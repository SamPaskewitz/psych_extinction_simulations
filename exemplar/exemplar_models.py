from statsrat import exemplar

null = exemplar.model(name = 'null',
                      sim = exemplar.sim.Gaussian,
                      rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                      atn_update = exemplar.atn_update.null,
                      u_ex_update = exemplar.u_ex_update.ex_mean)
                       
grad = exemplar.model(name = 'grad',
                      sim = exemplar.sim.Gaussian,
                      rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                      atn_update = exemplar.atn_update.gradient_ngsec,
                      u_ex_update = exemplar.u_ex_update.ex_mean)
    
grad_common = exemplar.model(name = 'grad_common',
                             sim = exemplar.sim.Gaussian,
                             rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                             atn_update = exemplar.atn_update.gradient_ngsec_common,
                             u_ex_update = exemplar.u_ex_update.ex_mean)

grad_both = exemplar.model(name = 'grad_both',
                           sim = exemplar.sim.Gaussian,
                           rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                           atn_update = exemplar.atn_update.gradient_ngsec_both,
                           u_ex_update = exemplar.u_ex_update.ex_mean)

heuristic = exemplar.model(name = 'heuristic',
                           sim = exemplar.sim.Gaussian,
                           rtrv = exemplar.rtrv.normalized_sim_ex_counts,
                           atn_update = exemplar.atn_update.heuristic,
                           u_ex_update = exemplar.u_ex_update.ex_mean)