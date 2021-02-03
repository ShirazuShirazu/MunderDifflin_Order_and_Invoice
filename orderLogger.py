import pandas as pd
import openpyxl as oxl, datetime


# addNewOrder takes the newOrder in the form of a dictionary. It makes newOrder a df and then appends said df to old
# df of orders, taken from the excel sheet 'orderLog,xlsx'. It then saves the new df to the excel sheet. Issue with
# this method is the full excel sheet is copied, created into df, appended with the new order and is then rewritten
# back into excel. I'm fully aware this is time and resource consuming. Hopefully I find the time to come back to
# redesign this.

# TODO: Find the time to redesign this.

def addNewOrder(newOrder):
    global prevOrders

    newOrder = pd.DataFrame(data = newOrder, index=[0])

    prevOrders = prevOrders.append(newOrder, ignore_index=True)

    prevOrders.to_excel('orderLog.xlsx', sheet_name='All Orders')


columns = ['Client ID', 'First Name', 'Last Name', 'Address', 'Invoice ID', 'Invoice Date', 'Invoice Due',
           'Item Description', 'Total Cost']

try:

    prevOrders = pd.read_excel('orderLog.xlsx', engine='openpyxl', index_col=0)
    print('try')

    # checks if the excel sheet already has the columns in place
    if list(prevOrders.columns):
        print('this')
        pass

    else:
        print('that')
        prevOrders = pd.DataFrame(columns=columns)

except:

    # fp = open('orderLog.xlsx', 'w')
    # fp.close()

    temp = pd.DataFrame(columns=columns)
    temp.to_excel('orderLog.xlsx', sheet_name='All Orders')

    # xl = oxl.load_workbook('orderLog.xlsx')
    # xl.save('orderLog.xlsx')

    # prevOrders = pd.read_excel('orderLog.xlsx', engine='openpyxl', index_col=0)
    prevOrders = pd.DataFrame(columns=columns)
    print('made new')

if __name__ == '__main__':
    columns = ['Client ID', 'First Name', 'Last Name', 'Address', 'Invoice ID', 'Invoice Date', 'Invoice Due',
               'Item Description', 'Total Cost']
    values = [12310123, 'Shiraz', 'Mohamed', 'Dubai', 696969, datetime.datetime.now().date(),
              datetime.datetime.now().date(),
              'thingamajig', '420']
    colval = zip(columns, values)
    colval = dict(colval)

    addNewOrder(colval)
    addNewOrder(colval)
    print('\n test done')
