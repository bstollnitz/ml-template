import argparse
import logging

def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("--my_arg", default=0)
    args = parser.parse_args()
    logging.info("input parameters: %s", vars(args))


if __name__ == "__main__":
    main()