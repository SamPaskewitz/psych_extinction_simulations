"""
This represents a research design that would allow one to test the hypothesis that spontaneous recovery is context
dependent.  To my knowledge, no one has so far carried out an experiment like this.
"""

from statsrat import expr

iti = 5
n_rep_train = 5
n_rep_extn = 10
n_rep_test = 2
delay_length = 200

### DEFINE STAGES ###

# conditioning (CTX A)
training = expr.stage(x_pn = [['cs']],
                      x_bg = ['ctx_a'],
                      u = [['us']],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = iti,
                      n_rep = n_rep_train)

# extinction (CTX A)
extinction = expr.stage(x_pn = [['cs']],
                        x_bg = ['ctx_a'],
                        u_psb = ['us'],
                        order_fixed = True,
                        iti = iti,
                        n_rep = n_rep_extn)

# delay
delay = expr.stage(x_pn = [[]],
                   x_bg = ['home_cage'],
                   u_psb = ['us'],
                   order_fixed = True,
                   iti = 0,
                   n_rep = delay_length)

# test (CTX A)
test_a = expr.stage(x_pn = [['cs']],
                   x_bg = ['ctx_a'],
                   u_psb = ['us'],
                   order_fixed = True,
                   iti = iti,
                   n_rep = n_rep_test)

# test (CTX B)
test_b = expr.stage(x_pn = [['cs']],
                   x_bg = ['ctx_b'],
                   u_psb = ['us'],
                   order_fixed = True,
                   iti = iti,
                   n_rep = n_rep_test)

### DEFINE SCHEDULES ###

# different test context (CTX B), immediate test
diff_immediate = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': extinction, 'test': test_b})

# different test context (CTX B), delay before test
diff_delay = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': extinction, 'delay': delay, 'test': test_b})

# same test context (CTX A), immediate test
same_immediate = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': extinction, 'test': test_a})

# same test context (CTX A), delay before test
same_delay = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'extinction': extinction, 'delay': delay, 'test': test_a})

### DEFINE BEHAVIORAL SCORE AND OATS ###

# behavioral score
cs_score = expr.behav_score(stage = 'test',
                            trial_pos = ['cs -> nothing'],
                            resp_pos = ['us'])

# OAT: spontaneous recovery
spont_rec = expr.oat(schedule_pos = ['delay'],
                     schedule_neg = ['immediate'],
                     behav_score_pos = cs_score,
                     behav_score_neg = cs_score)

# OAT: context dependence of spontaneous recovery (this amounts to the same thing - up to a constant factor - as subtracting spontaneous recovery in the Diff groups from spontaneous recovery in the Same groups)
context_dep = expr.oat(schedule_pos = ['same_delay', 'diff_immediate'],
                       schedule_neg = ['same_immediate', 'diff_delay'],
                       behav_score_pos = cs_score,
                       behav_score_neg = cs_score)

### DEFINE EXPERIMENT ###

spont_rec = expr.experiment(schedules = {'diff_immediate': diff_immediate, 'diff_delay': diff_delay, 'same_immediate': same_immediate, 'same_delay': same_delay},
                            oats = {'spont_rec': spont_rec, 'context_dep': context_dep})