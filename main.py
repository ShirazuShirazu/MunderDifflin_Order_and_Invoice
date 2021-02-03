import clientDeets, orderLogger, invoiceMaker
import datetime, os

# creates a log object to access the client data store.

log = clientDeets.log()

# Starting a menu, giving instructions and waiting for user response.

while True:
    print('\n' + '=' * 25)
    print("Enter what you would like to do (1-4):\n")
    print('1) Create a new invoice')
    print('2) Check client contacts')
    print('3) Check previous orders')

    print('\n')
    choice = int(input('Enter your choice: '))

    if choice == 1:

        newOrder = {}
        print("Creating new invoice. Enter the appropriate details:\n")
        newOrder['First Name'] = input("Client's firstname: ")

        # log.checkExisting searches if a client with the same first name is present in the client info
        # database.

        contact = log.checkExisting(newOrder['First Name'])
        newOrder.update(contact)

        # Inputting additional info of the order.

        newOrder['Item Description'] = input("Item description: ")
        newOrder['Total Cost'] = input("Total cost: ")

        newOrder['Invoice ID'] = ''.join([x for x in str(datetime.datetime.now()) if x.isnumeric()])[:-6]

        newOrder['Invoice Date'] = datetime.datetime.now().date()
        newOrder['Invoice Due'] = newOrder['Invoice Date'] + datetime.timedelta(days=7)

        orderLogger.addNewOrder(newOrder)
        invoiceMaker.createInvoice(newOrder)

    elif choice == 2:

        # Displays all saved client info.

        log.displayContacts()

    elif choice == 3:

        # Opens the invoice excel log
        os.startfile('C:/Users/LENOVO/Documents/Projects/MunderDifflin/orderLog.xlsx')

    elif choice == 4:

        print('Closing program')
        break

# Program End
