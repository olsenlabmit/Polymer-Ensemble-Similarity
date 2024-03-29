# -*- coding: utf-8 -*-

# import necessary libraries
import numpy as np
import json


# function for json save
def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()


# print function
def dict_print_function(dict_x):
    dict_x_keys = list(dict_x.keys())
    for i in range(0, len(dict_x_keys)):
        print(
            "sequence: ", dict_x_keys[i], ", its weight: ", dict_x[dict_x_keys[i]], "\n"
        )


# first-order markov copolymer ensemble generation
def generate_sequence_equal_composition(
    lambda_value=0.0,
    chain_length=10,
    chain_amount=1000,
    ensemble_dict_filename="ensemble_dict.json",
    ensemble_weight_dict_filename="ensemble_weight_dict.json",
    print_details=False,
):
    f_R1_value = 0.5  # we fix the concentration of R0 and R1

    # the transition variables t00, t01, t10, t11 are only determined by lambda

    t00 = (1 + lambda_value) / 2

    t01 = (1 - lambda_value) / 2

    t10 = (1 - lambda_value) / 2

    t11 = (1 + lambda_value) / 2

    print("First Order Markov Process Parameters:")
    print("f_R1 : ", f_R1_value, "\n")
    print("lambda : ", lambda_value, "\n")
    print("t00 : ", t00, "\n")
    print("t01 : ", t01, "\n")
    print("t10 : ", t10, "\n")
    print("t11 : ", t11, "\n")

    ensemble_weight_dict = {}

    for i in range(chain_amount):
        seq = ""

        # sample
        x0 = np.random.rand()
        if x0 <= f_R1_value:
            seq = seq + "1"
        else:
            seq = seq + "0"

        for j in range(1, chain_length):
            if seq[-1] == "0":
                t = np.random.rand()
                if t <= t00:
                    seq = seq + "0"
                else:
                    seq = seq + "1"

            elif seq[-1] == "1":
                t = np.random.rand()
                if t <= t11:
                    seq = seq + "1"
                else:
                    seq = seq + "0"
            else:
                print("error")

        if (seq in ensemble_weight_dict) == False:
            ensemble_weight_dict[seq] = 1

        else:
            ensemble_weight_dict[seq] = ensemble_weight_dict[seq] + 1

    if print_details == True:
        print(
            "With ",
            chain_amount,
            "samplings, the First-Order Markov Copolymer Ensemble is:\n",
        )

        dict_print_function(ensemble_weight_dict)

    # save the sequences that are sampled
    with open(ensemble_dict_filename, "w") as fp:
        json.dump(list(ensemble_weight_dict.keys()), fp)

    # save the weights
    with open(ensemble_weight_dict_filename, "w") as fp:
        fp.write(json.dumps(ensemble_weight_dict, default=np_encoder))


# test at lambda = 0.0
generate_sequence_equal_composition(
    lambda_value=0.0, chain_length=10, chain_amount=100, print_details=True
)
