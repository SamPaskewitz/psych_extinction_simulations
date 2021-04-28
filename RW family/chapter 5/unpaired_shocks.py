"""
Renewal after extinction in multiple contexts.

Based loosely on Rauhut et al 2001, Experiment 2.
"""

from statsrat import expr

iti = 4
n_rep_train = 5
n_rep_extn = 5
n_rep_test = 2

### DEFINE STAGES ###

# **** FINISH UPDATING EVERYTHING. ****

# conditioning
training = expr.stage(x_pn = [['cs1']],
                      x_bg = ['ctx_a'],
                      u = [['us']],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = iti,
                      n_rep = n_rep_train)

# extinction (no unpaired shocks)
extn = expr.stage(x_pn = [['cs1'], []],
                  x_bg = ['ctx_b'],
                  u_psb = ['us'],
                  freq = [2, 1],
                  order_fixed = True,
                  iti = iti,
                  n_rep = n_rep_extn)

# extinction (with unpaired shocks)
extn_shocks = expr.stage(x_pn = [['cs1'], []],
                         x_bg = ['ctx_b'],
                         u = [[], ['us']],
                         u_psb = ['us'],
                         freq = [2, 1],
                         order_fixed = True,
                         iti = iti,
                         n_rep = n_rep_extn)

# test
test = expr.stage(x_pn = [['cs1']],
                  x_bg = ['ctx_a'],
                  u_psb = ['us'],
                  order_fixed = True,
                  iti = iti,
                  n_rep = n_rep_test)

# reacquisition/novel acquisition
training2 = expr.stage(x_pn = [['cs1'], ['cs2']],
                       x_bg = ['ctx_a'],
                       u = 2*[['us']],
                       u_psb = ['us'],
                       order_fixed = True,
                       iti = iti,
                       n_rep = n_rep_train)

### DEFINE SCHEDULES ###

# extinction without unpaired shocks (control)
control = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': extn, 'test': test, 'cond2': training2})

# extinction with unpaired shocks
shocks = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': extn_shocks, 'test': test, 'cond2': training2})

### DEFINE BEHAVIORAL SCORE AND OAT ###

# behavioral score
cs1_score = expr.behav_score(stage = 'test',
                            trial_pos = ['cs1 -> nothing'],
                            resp_pos = ['us'])

# OAT
shocks_vs_none = expr.oat(schedule_pos = ['control'],
                          schedule_neg = ['unpaired_shocks'],
                          behav_score_pos = cs1_score,
                          behav_score_neg = cs1_score)

### DEFINE EXPERIMENT ###

renewal = expr.experiment(schedules = {'control': control, 'unpaired_shocks': shocks},
                          oats = {'shocks_vs_none': shocks_vs_none})