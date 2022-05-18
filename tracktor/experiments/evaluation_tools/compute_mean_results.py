import argparse
import json
import os
from typing import List

import numpy as np
import tensorboard as tb
import tensorflow as tf


def smooth(scalars: List[float], weight: float) -> List[float]:
    """ Weight between 0 and 1 """

    # First value in the plot (first timestep)
    last = scalars[0]
    smoothed = []
    for point in scalars:
        # Calculate smoothed value
        smoothed_val = last * weight + (1 - weight) * point
        smoothed.append(smoothed_val)

        # Anchor the last smoothed value
        last = smoothed_val

    return smoothed


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--result_dirs_start_with', required=True)
    parser.add_argument('--result_dirs_end_with', required=False, default='')
    parser.add_argument('--result_dirs_without', required=False, default='')
    parser.add_argument('--ignore_with', required=False, default='')
    parser.add_argument('--metric', required=True)
    parser.add_argument('--metric_base', action='store_true')

    args = parser.parse_args()

    base_dir = os.path.dirname(args.result_dirs_start_with)

    # metrics = ['mota/val', 'idf1/val', 'num_switches/val']

    results = {}
    for result_dir in os.listdir(base_dir):
        if (not (result_dir.startswith(os.path.basename(args.result_dirs_start_with))
            and result_dir.endswith(os.path.basename(args.result_dirs_end_with)))
            or (args.result_dirs_without and args.result_dirs_without in result_dir)
            or (args.ignore_with and args.ignore_with in result_dir)):
            continue

        event_files = [s for s in os.listdir(os.path.join(base_dir, result_dir)) if s.startswith('events.out')]
        assert len(event_files) == 1, f'More or less than one event file in {result_dir}.'
        event_file = event_files[0]

        results_per_exp = {}
        for e in tf.compat.v1.train.summary_iterator(os.path.join(base_dir, result_dir, event_file)):
            for v in e.summary.value:

                tag = v.tag

                if args.metric_base:
                    tag = os.path.basename(v.tag)

                if args.metric != tag:
                    continue

                if tag not in results_per_exp:
                    results_per_exp[tag] = []
                results_per_exp[tag].append(v.simple_value)

                num_entries = len(results_per_exp[tag])

        print(result_dir, f"{num_entries} ENTRIES")

        results[result_dir] = results_per_exp

    res_m = [res[args.metric] for res in results.values()]
    min_length_in_res_m = min([len(r) for r in res_m])
    res_m = np.array([r[:min_length_in_res_m] for r in res_m])
    res_m = np.mean(res_m, axis=0)

    print()
    for i, r in enumerate(res_m):
        print(f"MEAN {args.metric} {r:.3f} ENTRY {i}")

    print(f"\nBEST MEAN {args.metric} {res_m.max():.3f} ENTRY {res_m.argmax()}")
