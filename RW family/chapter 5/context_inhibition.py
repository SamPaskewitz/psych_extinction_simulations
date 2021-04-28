"""
Detection of inhibition by the extinction context using a summation test,
and the effect of extinction ITI on inhibition by context.

Based on Polack et al (2012, Experiment 1).  For the sake of simplicity
the retardation test following the summation test is omitted.
"""
from statsrat import expr

### DEFINE STAGES ###

# conditioning of cs2
training_cs2 = expr.stage(x_pn = [['cs2']],
                          x_bg = ['ctx_a'],
                          u = [['us']],
                          u_psb = ['us'],
                          order_fixed = True,
                          iti = 5,
                          n_rep = 4)

# conditioning of cs1
training_cs1 = expr.stage(x_pn = [['cs1']],
                          x_bg = ['ctx_d'],
                          u = [['us']],
                          u_psb = ['us'],
                          order_fixed = True,
                          iti = 5,
                          n_rep = 24)

# extinction (massed)
msd_extn = expr.stage(x_pn = [['cs1']],
                      x_bg = ['ctx_b'],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = 1,
                      n_rep = 40)

# extinction (spaced)
spc_extn = expr.stage(x_pn = [['cs1']],
                      x_bg = ['ctx_b'],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = 50,
                      n_rep = 40)

# summation test (in extinction context)
test_sum = expr.stage(x_pn = [['cs2']],
                      x_bg = ['ctx_b'],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = 0,
                      n_rep = 1)

# summation test (control)
test_ctl = expr.stage(x_pn = [['cs2']],
                      x_bg = ['ctx_c'],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = 0,
                      n_rep = 1)

### DEFINE SCHEDULES ###

sum_msd = expr.schedule(resp_type = 'exct', stages = {'cond_cs2': training_cs2, 'cond_cs1': training_cs1, 'extinction': msd_extn, 'test': test_sum})

ctl_msd = expr.schedule(resp_type = 'exct', stages = {'cond_cs2': training_cs2, 'cond_cs1': training_cs1, 'extinction': msd_extn, 'test': test_ctl})

sum_spc = expr.schedule(resp_type = 'exct', stages = {'cond_cs2': training_cs2, 'cond_cs1': training_cs1, 'extinction': spc_extn, 'test': test_sum})

ctl_spc = expr.schedule(resp_type = 'exct', stages = {'cond_cs2': training_cs2, 'cond_cs1': training_cs1, 'extinction': spc_extn, 'test': test_ctl})

### DEFINE BEHAVIORAL SCORE AND OATS ###

# behavioral score
cs2_score = expr.behav_score(stage = 'test',
                             trial_pos = ['cs2 -> nothing'],
                             resp_pos = ['us'])

# OAT: summation vs. control, massed
massed = expr.oat(schedule_pos = ['control_massed'],
                  schedule_neg = ['summation_massed'],
                  behav_score_pos = cs2_score,
                  behav_score_neg = cs2_score)

# OAT: summation vs. control, spaced
spaced = expr.oat(schedule_pos = ['control_spaced'],
                  schedule_neg = ['summation_spaced'],
                  behav_score_pos = cs2_score,
                  behav_score_neg = cs2_score)

### DEFINE EXPERIMENT ###
context_inhibition = expr.experiment(schedules = {'summation_massed': sum_msd, 'control_massed': ctl_msd, 'summation_spaced': sum_spc, 'control_spaced': ctl_spc},
                                     oats = {'massed': massed, 'spaced': spaced})
