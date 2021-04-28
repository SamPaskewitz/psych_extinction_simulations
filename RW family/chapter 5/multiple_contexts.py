"""
Renewal after extinction in multiple contexts.

Based loosely on Gunther et al 1998, Experiment 1.

Gunther et al 1998, Experiment 1
--------------------------------
lick supression

162 total extinction trials

I'm leaving out the no extinction group.

equal exposure to all contexts according to some complicated
schedule that I'm not going to replicate
"""

from statsrat import expr

iti = 5
n_rep_train = 5
n_rep_extn = 9
n_rep_test = 5

### DEFINE STAGES ###

# conditioning
training = expr.stage(x_pn = [['cs']],
                      x_bg = ['ctx_a'],
                      u = [['us']],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = iti,
                      n_rep = n_rep_train)

# extinction (all in one context)
extn = expr.stage(x_pn = [['cs']],
                  x_bg = ['ctx_b'],
                  u_psb = ['us'],
                  order_fixed = True,
                  iti = iti,
                  n_rep = n_rep_extn)

# extinction (1/3 length, in context B)
extn_b = expr.stage(x_pn = [['cs']],
                    x_bg = ['ctx_b'],
                    u_psb = ['us'],
                    order_fixed = True,
                    iti = iti,
                    n_rep = int(n_rep_extn/3))

# extinction (1/3 length, in context C)
extn_c = expr.stage(x_pn = [['cs']],
                    x_bg = ['ctx_c'],
                    u_psb = ['us'],
                    order_fixed = True,
                    iti = iti,
                    n_rep = int(n_rep_extn/3))

# extinction (1/3 length, in context D)
extn_d = expr.stage(x_pn = [['cs']],
                    x_bg = ['ctx_d'],
                    u_psb = ['us'],
                    order_fixed = True,
                    iti = iti,
                    n_rep = int(n_rep_extn/3))

# test (in context E)
test = expr.stage(x_pn = [['cs']],
                  x_bg = ['ctx_e'],
                  u_psb = ['us'],
                  order_fixed = True,
                  iti = iti,
                  n_rep = n_rep_test)

### DEFINE SCHEDULES ###

# extinction in one context
one_context = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': extn, 'test': test})

# extinction in three contexts
three_contexts = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'ex_b': extn_b, 'ex_c': extn_c, 'ex_d': extn_d, 'test': test})

### DEFINE BEHAVIORAL SCORE AND OAT ###

# behavioral score
cs_score = expr.behav_score(stage = 'test',
                            trial_pos = ['cs -> nothing'],
                            resp_pos = ['us'])

# OAT
one_vs_three = expr.oat(schedule_pos = ['one_context'],
                        schedule_neg = ['three_contexts'],
                        behav_score_pos = cs_score,
                        behav_score_neg = cs_score)

### DEFINE EXPERIMENT ###

renewal = expr.experiment(schedules = {'one_context': one_context, 'three_contexts': three_contexts},
                          oats = {'one_vs_three': one_vs_three})