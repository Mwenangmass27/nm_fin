import random
import sys
from threading import Thread
import time

class Calculator(Thread):


    def __init__(self,"pricer_type"):
        Thread.__init__(self)
        self.list_pricers = ["pricer_type"]

    def run(self):
        for l in self.list_pricers:
            if (l["pricer_type"]=="montecarlo"):
                mc_values=[[[[[0 for i in range(nb_exp)] for j in range(nb_exp)] for k in range(nb_exp)] for l in range(nb_exp)] for m in range(nb_exp)]
                for i in range(nb_exp):
                    for j in range(nb_exp):
                        for k in range(nb_exp):
                            for l in range(nb_exp):
                                for m in range(nb_exp):
                                    mc_call=mlo.Montecarlo(mu=data_mc["mu"][i],maturity=data_mc["maturity"][j],sigma=data_mc["sigma"][k],s_on_k=data_mc["s_on_k"][l],nmc=data_mc["nmc"][m])
                                    (mc_values[i][j][k][l]).append(mc_call.pricer_call())
            if (l["pricer_type"]=="montecarlo is"):
                mc_is_values=[[[[[0 for i in range(nb_exp)] for j in range(nb_exp)] for k in range(nb_exp)] for l in range(nb_exp)] for m in range(nb_exp)]
                for i in range(nb_exp):
                    for j in range(nb_exp):
                        for k in range(nb_exp):
                            for l in range(nb_exp):
                                for m in range(nb_exp):
                                    mc_is_call=mloi.Montecarlo_is(mu=data_mc_is["mu"][i],maturity=data_mc_is["maturity"][j],sigma=data_mc_is["sigma"][k],s_on_k=data_mc_is["s_on_k"][l],nmc=data_mc_is["nmc"][m])
                                    (mc_is_values[i][j][k][l]).append(mc_is_call.pricer_call())
            if (l["pricer_type"]=="montecarlo antithetic"):
                mc_ant_values=[[[[[0 for i in range(nb_exp)] for j in range(nb_exp)] for k in range(nb_exp)] for l in range(nb_exp)] for m in range(nb_exp)]
                for i in range(nb_exp):
                    for j in range(nb_exp):
                        for k in range(nb_exp):
                            for l in range(nb_exp):
                                for m in range(nb_exp):
                                    mc_ant=mant.Montecarlo_antithetic(mu=data_mc_antithetic["mu"][i],maturity=data_mc_antithetic["maturity"][j],sigma=data_mc_antithetic["sigma"][k],s_on_k=data_mc_antithetic["s_on_k"][l],nmc=data_mc_antithetic["nmc"][m])
                                    (mc_ant_values[i][j][k][l]).append(mc_ant.pricer_call())
            if(l["pricer_type"]=="euler explicite"):
                fd_eexp_values=[[[[[[[0 for i in range(nb_exp)] for j in range(nb_exp)] for k in range(nb_exp)] for l in range(nb_exp)] for m in range(nb_exp)]for n in range(nb_exp)] for p in range(nb_exp)]
                for i in range(nb_exp):
                    for j in range(nb_exp):
                        for k in range(nb_exp):
                            for l in range(nb_exp):
                                for m in range(nb_exp):
                                    for n in range(nb_exp):
                                        for p in range(nb_exp):
                                            fd_call=fdx.fd_eulerexp(mu=data_fd_eexp["mu"][i],maturity=data_fd_eexp["maturity"][j],sigma=data_fd_eexp["sigma"][k],s_on_k=data_fd_eexp["s_on_k"][l],nt=data_fd_eexp["nt"][m],nx=data_fd_eexp["nx"][n])
                                            (fd_eexp_values[i][j][k][l][m][n]).append(fd_call.pricer_call())
            if(l["pricer_type"]=="euler implicite"):
                fd_eimp_values=[[[[[[[0 for i in range(nb_exp)] for j in range(nb_exp)] for k in range(nb_exp)] for l in range(nb_exp)] for m in range(nb_exp)]for n in range(nb_exp)] for p in range(nb_exp)]
                for i in range(nb_exp):
                    for j in range(nb_exp):
                        for k in range(nb_exp):
                            for l in range(nb_exp):
                                for m in range(nb_exp):
                                    for n in range(nb_exp):
                                        for p in range(nb_exp):
                                            fd_call=fdi.fd_eulerimp(mu=data_fd_eimp["mu"][i],maturity=data_fd_eimp["maturity"][j],sigma=data_fd_eimp["sigma"][k],s_on_k=data_fd_eimp["s_on_k"][l],nt=data_fd_eimp["nt"][m],nx=data_fd_eimp["nx"][n])
                                            (fd_eimp_values[i][j][k][l][m][n]).append(fd_call.pricer_call())