from statsrat import expr

iti = 5
n_rep_train = 5
n_rep_extn = 10
n_rep_test = 2
delay_length = 200
space_length = 100

### DEFINE STAGES ###

# conditioning
training = expr.stage(x_pn = [['cs']],
                      x_bg = ['ctx'],
                      u = [['us']],
                      u_psb = ['us'],
                      order_fixed = True,
                      iti = iti,
                      n_rep = n_rep_train)

# extinction (represents a single session)
extinction = expr.stage(x_pn = [['cs']],
                        x_bg = ['ctx'],
                        u_psb = ['us'],
                        order_fixed = True,
                        iti = iti,
                        n_rep = int(n_rep_extn/2))

# space
space = expr.stage(x_pn = [[]],
                   x_bg = ['home_cage'],
                   u_psb = ['us'],
                   order_fixed = True,
                   iti = 0,
                   n_rep = space_length)

# delay
delay = expr.stage(x_pn = [[]],
                   x_bg = ['home_cage'],
                   u_psb = ['us'],
                   order_fixed = True,
                   iti = 0,
                   n_rep = delay_length)

# test
test = expr.stage(x_pn = [['cs']],
                   x_bg = ['ctx'],
                   u_psb = ['us'],
                   order_fixed = True,
                   iti = iti,
                   n_rep = n_rep_test)


### DEFINE SCHEDULES ###

spaced_immediate = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'ex1': extinction, 'space': space, 'ex2': extinction, 'test': test})

spaced_delay = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'ex1': extinction, 'space': space, 'ex2': extinction, 'delay': delay, 'test': test})

control_immediate = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'ex1': extinction, 'ex2': extinction, 'test': test})

control_delay = expr.schedule(resp_type = 'exct', stages = {'cond': training, 'ex1': extinction, 'ex2': extinction, 'delay': delay, 'test': test})

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

### DEFINE EXPERIMENT ###

spont_rec = expr.experiment(schedules = {'spaced_immediate': spaced_immediate, 'spaced_delay': spaced_delay, 'control_immediate': control_immediate, 'control_delay': control_delay},
                            oats = {'spont_rec': spont_rec})