from time import sleep

from tqdm import tqdm


def main():
    some_list = [x for x in range(50)]
    for x in tqdm(some_list):
        sleep(0.1)


if __name__ == "__main__":
    main()