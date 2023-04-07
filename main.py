
import config
import connection
import sheet_operations


def main():

    sheet_operations.write_values(config.SAMPLE_RANGE_NAME, "USER_ENTERED",
                                  [
                                      ['A', 'B'],
                                      ['C', 'D']
                                  ])
    sheet_operations.read_values()


if __name__ == '__main__':
    main()
