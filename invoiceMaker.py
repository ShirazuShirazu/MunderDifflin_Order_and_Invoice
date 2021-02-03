import openpyxl as oxl, datetime, os

invoice_count = 0


def createInvoice(newOrder):

    # Creates an invoice from the invoice info given in the dictionary, newOrder.
    # uses openpyxl.

    invoicewb = oxl.load_workbook('Munder Difflin.xlsx')

    newInvoice = invoicewb.active

    newInvoice['B10'] = newOrder['First Name'] + ' ' + newOrder['Last Name']
    newInvoice['D10'] = newOrder['Address']
    newInvoice['F9'] = newOrder['Invoice ID']
    newInvoice['F10'] = newOrder['Invoice Date']
    newInvoice['F11'] = newOrder['Invoice Due']
    newInvoice['B16'] = newOrder['Item Description']
    newInvoice['E16'] = newOrder['Total Cost']
    newInvoice['F17'] = newOrder['Total Cost']

    invoiceName = str(newOrder['Invoice ID']) + '.xlsx'
    # invoiceName will be what the invoice file will be saved as.

    cwd = os.getcwd()
    newpath = cwd + '/Invoices/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    filepath = os.path.join(newpath, invoiceName)
    invoicewb.save(filepath)


if __name__ == '__main__':
    columns = ['Client ID', 'First Name', 'Last Name', 'Address', 'Invoice ID', 'Invoice Date', 'Invoice Due',
               'Item Description', 'Total Cost']
    values = [12310123, 'Shiraz', 'Mohamed', 'Dubai', 696969, datetime.datetime.now().date(),
              datetime.datetime.now().date(),
              'thingamajig', '420']
    colval = zip(columns, values)
    colval = dict(colval)

    createInvoice(colval)
    print('\n test done')
