#!/usr/bin/python3
import sys


def print_statistics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403':
                    0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            if len(data) > 2:
                try:
                    status_code = data[-2]
                    file_size = int(data[-1])
                    total_size += file_size
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)


    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
