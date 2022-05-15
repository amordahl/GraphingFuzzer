import os.path

import matplotlib.pyplot as plt
import pandas
import csv
import typing
import tqdm

import argparse
p = argparse.ArgumentParser()
p.add_argument("input", help="input csv")
p.add_argument("--no-header", help="By default, we treat the first row of the CSV as a header. Enabling this option "
                                   "will cause us to assume that the CSV has no header.")
args = p.parse_args()

def main(args: argparse.Namespace):

    plt.close("all")
    print("Reading in dataframe.")
    data = pandas.read_csv(args.input, low_memory=False)
    fig, ax = plt.subplots()

    for key, grp in data.groupby(['power_schedule']):
        ax = grp.plot(ax=ax, kind='scatter', x='seed_id', y='coverage', label=key)

    #data.plot(x='seed_id', y='coverage')
    plt.show()
    pass



if __name__ == "__main__":
    main(args)