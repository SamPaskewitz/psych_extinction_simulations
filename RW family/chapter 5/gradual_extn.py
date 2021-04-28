"""
Effect of gradual extinction on spontaneous recovery and reinstatement.
This is based roughly on Gershman et al 2017.

Notes on Gershman et al 2017, Experiment 1
------------------------------------------
10 minute habituation to box before conditioning

3 conditioning trials

24 extinction trials

gradual condition: shocks on extinction trials 1, 3, 6, 10, and 15 (5/24 reinforced)

gradual reverse condition: shocks on extinction trials 1, 6, 10, 13,
and 15 (5/24 reinforced)

first test 24 hours after extinction; second test after 30 day delay

4 trials per test

CS duration: 20 seconds

ITI duration: 120 seconds (6 x CS duration)

Notes on Gershman et al 2017, Experiment 2
------------------------------------------
similar to Experiment 1, but with 2 trials of reinstatement instead of the delay

all stages 24 hours apart

no second, novel CS used in the reinstatement stage (i.e. shocks were unsignaled)

greater fear to both the tone and context in the standard and gradual reverse groups than in the gradual group
"""
import numpy as np
from statsrat import expr

iti = 5
n_rep_train = 5
n_rep_extn = 24
n_rep_test = 4
delay_length = 200

### DEFINE STAGES ###

# conditioning
training = expr.stage(x_pn = [['cs']],
                      x_bg = ['ctx'],
                      u = [['us']],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = iti,
                      n_rep = n_rep_train)

# delay
delay = expr.stage(x_pn = [[]],
                   x_bg = ['home_cage'],
                   u_psb = ['us'],
                   order_fixed = True,
                   iti = 0,
                   n_rep = delay_length)

# standard extinction
std_extn = expr.stage(x_pn = [['cs']],
                      x_bg = ['ctx'],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = iti,
                      n_rep = n_rep_extn)

# gradual extinction
grd_us_trials = [0, 2, 5, 9, 14]
grd_order = np.zeros(n_rep_extn, dtype = 'int')
grd_order[grd_us_trials] = 1
grd_extn = expr.stage(x_pn = [['cs'], ['cs']],
                      u = [[], ['us']],
                      x_bg = ['ctx'],
                      u_psb = ['us'],
                      order = list(grd_order),
                      iti = iti,
                      n_rep = 1)

# reversed gradual extinction
rev_us_trials = [0, 5, 9, 12, 14]
rev_order = np.zeros(n_rep_extn, dtype = 'int')
rev_order[rev_us_trials] = 1
rev_extn = expr.stage(x_pn = [['cs'], ['cs']],
                      u = [[], ['us']],
                      x_bg = ['ctx'],
                      u_psb = ['us'],
                      order = list(rev_order),
                      iti = iti,
                      n_rep = 1)

# extra, unsignaled shocks (for reinstatement)
shocks = expr.stage(x_pn = [[]],
                    x_bg = ['ctx'],
                    u = [['us']],
                    u_psb = ['us'],
                    order_fixed = True,
                    iti = iti,
                    n_rep = 2)

# test
test = expr.stage(x_pn = [['cs']],
                  x_bg = ['ctx'],
                  u_psb = ['us'],
                  order_fixed = True,
                  iti = iti,
                  n_rep = n_rep_test)

### DEFINE SCHEDULES FOR SPONTANEOUS RECOVERY ###

# standard extinction
standard_sr = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': std_extn, 'delay': delay, 'test': test})

# gradual extinction
gradual_sr = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': grd_extn, 'delay': delay, 'test': test})

# reverse of gradual extinction
gradual_reverse_sr = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': rev_extn, 'delay': delay, 'test': test})

### DEFINE SCHEDULES FOR REINSTATEMENT ###

# standard extinction
standard_re = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': std_extn, 'extra_us': shocks, 'test': test})

# gradual extinction
gradual_re = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': grd_extn, 'extra_us': shocks, 'test': test})

# reverse of gradual extinction
gradual_reverse_re = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': rev_extn, 'extra_us': shocks, 'test': test})

### DEFINE BEHAVIORAL SCORE AND OATS ###

# behavioral score
cs_score = expr.behav_score(stage = 'test',
                            trial_pos = ['cs -> nothing'],
                            resp_pos = ['us'])

# OAT: gradual vs. standard
grd_vs_std = expr.oat(schedule_pos = ['standard'],
                      schedule_neg = ['gradual'],
                      behav_score_pos = cs_score,
                      behav_score_neg = cs_score)

# OAT: gradual vs. gradual reverse
grd_vs_rev = expr.oat(schedule_pos = ['gradual_reverse'],
                      schedule_neg = ['gradual'],
                      behav_score_pos = cs_score,
                      behav_score_neg = cs_score)

### DEFINE EXPERIMENTS ###

# spontaneous recovery
spont_rec = expr.experiment(schedules = {'standard': standard_sr, 'gradual': gradual_sr, 'gradual_reverse': gradual_reverse_sr},
                            oats = {'grd_vs_std': grd_vs_std, 'grd_vs_rev': grd_vs_rev})

# reinstatement
reinstatement = expr.experiment(schedules = {'standard': standard_re, 'gradual': gradual_re, 'gradual_reverse': gradual_reverse_re},
                                oats = {'grd_vs_std': grd_vs_std, 'grd_vs_rev': grd_vs_rev})