"""
Extinction with or without representation of context.
"""

from statsrat import expr

iti = 5
n_rep_train = 5
n_rep_extn = 10
n_rep_test = 5

nc_training_stage = expr.stage(x_pn = [['cs']],
                               x_bg = [],
                               u = [['us']],
                               u_psb = ['us'],
                               order_fixed = True,
                               iti = iti,
                               n_rep = n_rep_train)

nc_extn_stage = expr.stage(x_pn = [['cs']],
                        x_bg = [],
                        u_psb = ['us'],
                        order_fixed = True,
                        iti = iti,
                        n_rep = n_rep_extn)

nc_test_stage = expr.stage(x_pn = [['cs']],
                        x_bg = [],
                        u_psb = ['us'],
                        order_fixed = True,
                        iti = iti,
                        n_rep = n_rep_test)

ctx_training_stage = expr.stage(x_pn = [['cs']],
                            x_bg = ['ctx'],
                            u = [['us']],
                            u_psb = ['us'],
                            order_fixed = True,
                            iti = iti,
                            n_rep = n_rep_train)

ctx_extn_stage = expr.stage(x_pn = [['cs']],
                        x_bg = ['ctx'],
                        u_psb = ['us'],
                        order_fixed = True,
                        iti = iti,
                        n_rep = n_rep_extn)

ctx_test_stage = expr.stage(x_pn = [['cs']],
                        x_bg = ['ctx'],
                        u_psb = ['us'],
                        order_fixed = True,
                        iti = iti,
                        n_rep = n_rep_test)

# extinction (no context)
nc_extn_schedule = expr.schedule(resp_type = 'exct', stages = {'cond': nc_training_stage, 'extinction': nc_extn_stage, 'test':  nc_test_stage})
nc_extn = expr.experiment(schedules = {'extinction': nc_extn_schedule})

# extinction (context)
ctx_extn_schedule = expr.schedule(resp_type = 'exct', stages = {'cond': ctx_training_stage, 'extinction': ctx_extn_stage, 'test': ctx_test_stage})
ctx_extn = expr.experiment(schedules = {'extinction': ctx_extn_schedule})