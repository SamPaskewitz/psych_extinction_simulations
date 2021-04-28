from statsrat import expr

'''
Experiment object for simulating spontaneous recovery.
In this case, delays between extinction and test are explicitly included in the simulation.

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

# I won't use this, as it complicates the design and doesn't seem to make much difference.
prexp_stage = expr.stage(x_pn = [['cs']],
                         x_bg = ['ctx'],
                         u_psb = ['us'],
                         order_fixed = True,
                         iti = iti,
                         n_rep = n_rep_prexp)

train_stage = expr.stage(x_pn = [['cs']],
                         x_bg = ['ctx'],
                         u = [['us']],
                         u_psb = ['us'],
                         order_fixed = True, 
                         iti = iti,
                         n_rep = n_rep_train)

extn_stage = expr.stage(x_pn = [['cs']],
                        x_bg = ['ctx'],
                        u_psb = ['us'],
                        order_fixed = True,
                        iti = iti,
                        n_rep = n_rep_extn)

pre_extn_test_stage = expr.stage(x_pn = [['cs']],
                                 x_bg = ['ctx'],
                                 u_psb = ['us'],
                                 order_fixed = True,
                                 iti = iti,
                                 n_rep = n_rep_test)

post_extn_test_stage = expr.stage(x_pn = [['cs']],
                                  x_bg = ['ctx'],
                                  u_psb = ['us'],
                                  order_fixed = True,
                                  iti = iti,
                                  n_rep = n_rep_test)

spont_rec_test_stage = expr.stage(x_pn = [['cs']],
                                  x_bg = ['ctx'],
                                  u_psb = ['us'],
                                  order_fixed = True,
                                  iti = iti,
                                  n_rep = n_rep_test)

delay50_stage = expr.stage(x_pn = [[]],
                           x_bg = ['home_cage'],
                           u_psb = ['us'],
                           order_fixed = True,
                           iti = 0,
                           n_rep = 50)

delay100_stage = expr.stage(x_pn = [[]],
                            x_bg = ['home_cage'],
                            u_psb = ['us'],
                            order_fixed = True,
                            iti = 0,
                            n_rep = 100)

delay200_stage = expr.stage(x_pn = [[]],
                            x_bg = ['home_cage'],
                            u_psb = ['us'],
                            order_fixed = True,
                            iti = 0,
                            n_rep = 200)

delay400_stage = expr.stage(x_pn = [[]],
                            x_bg = ['home_cage'],
                            u_psb = ['us'],
                            order_fixed = True,
                            iti = 0,
                            n_rep = 400)

##### DEFINE SCHEDULES #####

# extinction
extn_delay0 = expr.schedule(resp_type = 'exct',
                            stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'test': spont_rec_test_stage})

# extinction with a delay of 50 time units
extn_delay50 = expr.schedule(resp_type = 'exct',
                             stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'delay': delay50_stage, 'test': spont_rec_test_stage})

# extinction with a delay of 100 time units
extn_delay100 = expr.schedule(resp_type = 'exct',
                              stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'delay': delay100_stage, 'test': spont_rec_test_stage})

# extinction with a delay of 200 time units
extn_delay200 = expr.schedule(resp_type = 'exct',
                              stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'delay': delay200_stage, 'test': spont_rec_test_stage})

# extinction with a delay of 400 time units
extn_delay400 = expr.schedule(resp_type = 'exct',
                              stages = {'cond': train_stage, 'pre_ex_test': pre_extn_test_stage, 'extinction': extn_stage, 'post_ex_test': post_extn_test_stage, 'delay': delay400_stage, 'test': spont_rec_test_stage})

##### DEFINE BEHAVIORAL SCORES #####

cs_score = expr.behav_score(stage = 'spont rec test',
                            trial_pos = ['cs -> nothing'],
                            resp_pos = 2*['us'])

##### DEFINE OATS AND EXPERIMENTS #####

# spontaneous recovery
spont_rec = expr.experiment(schedules = {'delay0': extn_delay0, 'delay50': extn_delay50, 'delay100': extn_delay100, 'delay200': extn_delay200, 'delay400': extn_delay400},
                            oats = {'spontaneous_recovery': expr.oat(schedule_pos = ['delay400'],
                                                                     schedule_neg = ['delay0'],
                                                                     behav_score_pos = cs_score,
                                                                     behav_score_neg = cs_score)
})