import argparse

import sys
import os
# Get the current working directory
cwd = os.getcwd()
# Add the src directory to sys.path
sys.path.append(os.path.join(cwd, 'src'))

from src._lnlpcli import LNLPCLI

def main():
    """
    Entry point of the BERTopic CLI.

    Parses command line arguments, initializes the LNLPCLI object, and runs the CLI.
    """

    parser = argparse.ArgumentParser(description="BERTopic CLI")

    parser.add_argument(
        "--save_dir", type=str, help="Path to save the model"
    )

    parser.add_argument(
        "--data", type=str, help="Path to the global data file"
    )
    parser.add_argument(
        "--num_samples", type=int, help="Number of samples to generate"
    )

    parser.add_argument(
        "--sequence", type=str, help="Sequence of commands to process"
    )

    parser.add_argument(
        "--tmconfig", type=str, help="Path to the global topic model config file"
    )
    parser.add_argument(
        "--optconfig", type=str, help="Path to the global optimization config file"
    )
    parser.add_argument(
        "--ftconfig", type=str, help="Path to the global fine tuning config file"
    )
    args = parser.parse_args()

    num_samples = args.num_samples if args.num_samples else 0

    sequence = args.sequence if args.sequence else ''

    cli = LNLPCLI(save_dir=args.save_dir, global_data_path=args.data, global_tm_config_path=args.tmconfig, global_ft_config_path=args.ftconfig, sequence=sequence, global_optmization_path=args.optconfig, num_samples=num_samples)

    cli.run()

if __name__ == "__main__":

    main()

