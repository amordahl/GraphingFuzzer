import os.path

import matplotlib.pyplot as plt
import pandas
import csv
import typing
import tqdm

import argparse

from matplotlib.figure import Figure

p = argparse.ArgumentParser()
p.add_argument("input", help="input csv")
p.add_argument("--no-header", help="By default, we treat the first row of the CSV as a header. Enabling this option "
                                   "will cause us to assume that the CSV has no header.")
args = p.parse_args()

def main(args: argparse.Namespace):

    plt.close("all")
    print("Reading in dataframe.")
    data = pandas.read_csv(args.input, low_memory=False)
    print("Done!")

    # fig, axs = plt.subplots(nrows=len(data['power_schedule'].unique()), ncols=3)
    # fig: Figure
    # fig.set_size_inches((10,10))
    # fig.set_dpi(300)
    #
    # for i, ps in enumerate(data['power_schedule'].unique()):
    #     for j, ri in enumerate((data[data['power_schedule']== ps])['run_id'].unique()):
    #         subdata = data[data['power_schedule'] == ps]
    #         subdata = subdata[subdata['run_id'] == ri]
    #         ax = axs[i][j]
    #         ax.plot(subdata['time'], subdata['coverage'], linestyle='--', marker='o')

    fig, ax = plt.subplots()
    fig: Figure
    fig.set_size_inches((10,5))
    fig.set_dpi(300)

    for key, grp in data.groupby(['power_schedule']):
        ax = grp.plot(ax=ax, kind='line', marker='o', x='time', y='coverage', label=key)

    ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    # set aspect ratio to 1
    ratio = 0.5
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)

    plt.tight_layout()
    plt.show()
    pass



if __name__ == "__main__":
    main(args)