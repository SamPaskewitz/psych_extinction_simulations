from statsrat import expr
import pandas as pd

'''
Experiment object for simulating spontaneous recovery.
In this case, the delay is represented by a continuous time cue (for the exemplar model).

Based on Quirk, 2002.

Notes on Quirk, 2002
--------------------
suppression of bar pressing, measured as freezing (with video camera)

5 'habituation' (pre-exposure to the CS) trials prior to conditioning (I'll omit these)

7 trials conditioning

20 extinction trials (1 hour later, with time between spent in home cage)

15 test/re-extinction trials

entire delay spent in home cage

data reported from last 2 trials of conditioning (pre-extinction), last 2 trials of extinction (post-extinction), and first 2 trials of test (spontaneous recovery)
'''
iti = 5
n_rep_prexp = 5
n_rep_train = 7
n_rep_extn = 16
n_rep_test = 2

##### DEFINE STAGES #####

train_stage = expr.stage(x_pn = [['cs']],
                         x_bg = ['ctx', 'time'],
                         x_value = pd.Series({'cs': 1.0, 'ctx': 1.0, 'time': 0.0}),
                         u = [['us']],
                         u_psb = ['us'],
                         order_fixed = True, 
                         iti = iti,
                         n_rep = n_rep_train)

extn_stage = expr.stage(x_pn = [['cs']],
                        x_bg = ['ctx', 'time'],
                        x_value = pd.Series({'cs': 1.0, 'ctx': 1.0, 'time': 1.0}),
                        u_psb = ['us'],
                        order_fixed = True,
                        iti = iti,
                        n_rep = n_rep_extn)

pre_extn_test_stage = expr.stage(x_pn = [['cs']],
                                 x_bg = ['ctx', 'time'],
                                 x_value = pd.Series({'cs': 1.0, 'ctx': 1.0, 'time': 0.0}),
                                 u_psb = ['us'],
                                 order_fixed = True,
                                 iti = iti,
                                 n_rep = n_rep_test)

post_extn_test_stage = expr.stage(x_pn = [['cs']],
                                  x_bg = ['ctx', 'time'],
                                  x_value = pd.Series({'cs': 1.0, 'ctx': 1.0, 'time': 1.0}),
                                  u_psb = ['us'],
                                  order_fixed = True,
                                  iti = iti,
                                  n_rep = n_rep_test)

test_stage_delay0 = expr.stage(x_pn = [['cs']],
                               x_bg = ['ctx', 'time'],
                               x_value = pd.Series({'cs': 1.0, 'ctx': 1.0, 'time': 1.0}),
                               u_psb = ['us'],
                               order_fixed = True,
                               iti = iti,
                               n_rep = n_rep_test)

test_stage_delayhalf = expr.stage(x_pn = [['cs']],
                                  x_bg = ['ctx', 'time'],
                                  x_value = pd.Series({'cs': 1.0, 'ctx': 1.0, 'time': 1.5}),
                                  u_psb = ['us'],
                                  order_fixed = True,
                                  iti = iti,
                                  n_rep = n_rep_test)

test_stage_delay1 = expr.stage(x_pn = [['cs']],
                               x_bg = ['ctx', 'time'],
                               x_value = pd.Series({'cs': 1.0, 'ctx': 1.0, 'time': 2.0}),
                               u_psb = ['us'],
                               order_fixed = True,
                               iti = iti,
                               n_rep = n_rep_test)

test_stage_delay2 = expr.stage(x_pn = [['cs']],
                               x_bg = ['ctx', 'time'],
                               x_value = pd.Series({'cs': 1.0, 'ctx': 1.0, 'time': 3.0}),
                               u_psb = ['us'],
                               order_fixed = True,
                               iti = iti,
                               n_rep = n_rep_test)

test_stage_delay4 = expr.stage(x_pn = [['cs']],
                               x_bg = ['ctx', 'time'],
                               x_value = pd.Series({'cs': 1.0, 'ctx': 1.0, 'time': 5.0}),
                               u_psb = ['us'],
                               order_fixed = True,
                               iti = iti,
                               n_rep = n_rep_test)

##### DEFINE SCHEDULES #####

# extinction
extn_delay0 = expr.schedule(resp_type = 'exct',
                            stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'test': test_stage_delay0})

# extinction with a delay of 0.5
extn_delayhalf = expr.schedule(resp_type = 'exct',
                               stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'test': test_stage_delayhalf})

# extinction with a delay of 1
extn_delay1 = expr.schedule(resp_type = 'exct',
                            stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'test': test_stage_delay1})

# extinction with a delay of 2
extn_delay2 = expr.schedule(resp_type = 'exct',
                            stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'test': test_stage_delay2})

# extinction with a delay of 4
extn_delay4 = expr.schedule(resp_type = 'exct',
                            stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'test': test_stage_delay4})

##### DEFINE BEHAVIORAL SCORES #####

cs_score = expr.behav_score(stage = 'spont rec test',
                            trial_pos = ['cs -> nothing'],
                            resp_pos = 2*['us'])

##### DEFINE OATS AND EXPERIMENTS #####

# spontaneous recovery
spont_rec = expr.experiment(schedules = {'delay0': extn_delay0, 'delayhalf': extn_delayhalf, 'delay1': extn_delay1, 'delay2': extn_delay2, 'delay4': extn_delay4},
                            oats = {'spontaneous_recovery': expr.oat(schedule_pos = ['delay4'],
                                                                     schedule_neg = ['delay0'],
                                                                     behav_score_pos = cs_score,
                                                                     behav_score_neg = cs_score)
})