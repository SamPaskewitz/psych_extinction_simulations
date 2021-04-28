"""
Context dependence of reinstatement.

Based loosely on Bouton and Bolles 1979, Experiment 1.

However, I'm omitting the second CS, i.e. the US is unsignaled.
I'm also omitting the backwards conditioning control group.
"""

from statsrat import expr

iti = 5
n_rep_train = 5
n_rep_extn = 5
n_rep_test = 2

### DEFINE STAGES ###

# conditioning
training = expr.stage(x_pn = [['cs']],
                      x_bg = ['ctx_a'],
                      u = [['us']],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = iti,
                      n_rep = n_rep_train)

# extinction
extn = expr.stage(x_pn = [['cs']],
                  x_bg = ['ctx_b'],
                  u_psb = ['us'],
                  order_fixed = True,
                  iti = iti,
                  n_rep = n_rep_extn)

# extra shocks (for reinstatement); CTX A
shocks_ctx_a = expr.stage(x_pn = [[]],
                          x_bg = ['ctx_a'],
                          u = [['us']],
                          u_psb = ['us'],
                          order_fixed = True,
                          iti = iti,
                          n_rep = 2)

# extra shocks (for reinstatement); CTX B
shocks_ctx_b = expr.stage(x_pn = [[]],
                          x_bg = ['ctx_b'],
                          u = [['us']],
                          u_psb = ['us'],
                          order_fixed = True,
                          iti = iti,
                          n_rep = 2)

# test
test = expr.stage(x_pn = [['cs']],
                  x_bg = ['ctx_b'],
                  u_psb = ['us'],
                  order_fixed = True,
                  iti = iti,
                  n_rep = n_rep_test)

### DEFINE SCHEDULES ###

# extra shocks in test context, i.e. CTX B
same = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': extn, 'extra_us': shocks_ctx_b, 'test': test})

# extra shocks in conditioning context, i.e. CTX A
different = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': extn, 'extra_us': shocks_ctx_a, 'test': test})

### DEFINE BEHAVIORAL SCORE AND OAT ###

# behavioral score
cs_score = expr.behav_score(stage = 'test',
                            trial_pos = ['cs -> nothing'],
                            resp_pos = ['us'])

# OAT
context_effect = expr.oat(schedule_pos = ['same'],
                          schedule_neg = ['different'],
                          behav_score_pos = cs_score,
                          behav_score_neg = cs_score)

### DEFINE EXPERIMENT ###

reinstatement = expr.experiment(schedules = {'same': same, 'different': different},
                                oats = {'context_effect': context_effect})