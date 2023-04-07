
import config
import connection
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def write_values(range_name, value_input_option,
                 values, sheet=None,
                 spreadsheet_id=config.SAMPLE_SPREADSHEET_ID):
    if sheet is None:
        sheet = connection.connect()
    try:

        body = {
            'values': values
        }
        result = sheet.values().update(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption=value_input_option, body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def read_values(sheet=None,
                spreadsheet_id=config.SAMPLE_SPREADSHEET_ID, range_name=config.SAMPLE_RANGE_NAME):
    if sheet is None:
        sheet = connection.connect()
    try:
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range_name).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
