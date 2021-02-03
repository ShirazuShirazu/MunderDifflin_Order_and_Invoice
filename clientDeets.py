import json, random, pprint, os

# d = {'Shiraz' : 'Witcher'}
# db = json.dumps(d)
# json.dump(d,open('clientlog.json','w'))
#
# db2 = json.load(open('clientlog.json','r'))
# d2 = json.loads(db)
# print(d2)

pp = pprint.PrettyPrinter(width=50, indent=2)


class log:

    def __init__(self):
        self.filepath = os.path.join(os.getcwd(), 'clientlog.json')

        try:

            fp = open(self.filepath, 'r')
            self.db = json.load(fp)
            self.db = json.loads(self.db)
            fp.close()

        except:
            print('Creating new contact log as "clientlog.json"')
            self.db = {}

    def createNew(self, fname=None):

        # Create a new client's contact

        if not fname:
            fname = input("First name: ")
        lname = input("Last name: ")
        address = input("Client's address: ")

        clientId = random.randint(10000, 99999)

        self.db[clientId] = {'First Name': fname, 'Last Name': lname, 'Address': address, 'Client ID': clientId}
        dbserial = json.dumps(self.db)
        json.dump(dbserial, open(self.filepath, 'w'))
        print('Client added.')
        return self.db[clientId]

    def displayContacts(self):

        pp.pprint(self.db)

        inp = input('\n Type any key to continue: ')
        del inp

    def clearContacts(self):

        choice = input('Are you sure you want to clear all contacts? (y/n): ')
        if choice in ['y', 'Y']:
            self.db = {}
            fp = open(self.filepath, 'w')
            print('cleared')
            fp.close()

        else:
            print("All your database are belong to us.")

    def displayContact(self, clientId):

        details = self.db[clientId]
        # print('Client ID:',clientId)
        pp.pprint(details)

    def checkExisting(self, firstname):

        firstnamesdb = {}
        for clientid, details in self.db.items():
            firstnamesdb.setdefault(details['First Name'], set()).add(clientid)

        if firstname in firstnamesdb.keys():

            if len(firstnamesdb[firstname]) > 1:
                print('Matching Contacts:\n')

                for i, clientId in enumerate(firstnamesdb[firstname]):
                    print('---- Contact', i + 1, '----')
                    self.displayContact(clientId)

                choice = int(input("Enter the contact number of the matching client or type '0': "))

                if 0 < choice < len(firstnamesdb[firstname]):
                    print('---- Contact', i + 1, '----')
                    self.displayContact(clientId)

                    print('\n')
                    choice = int(input('Type 1 to select above contact or 2 to create a new contact.'))
                    if choice == 1:
                        desiredClientId = list(firstnamesdb[firstname])[choice - 1]
                        return self.db[desiredClientId]
                    else:
                        return self.createNew(firstname)

                elif choice == 0:
                    return self.createNew(firstname)

            elif len(firstnamesdb[firstname]) == 1:
                desiredclientid = firstnamesdb[firstname]

                print("1 contact found with first name:", firstname)
                self.displayContact(list(desiredclientid)[0])

                choice2 = input("Enter '1' to use this contact or '0 to create a new contact: ")
                if choice2 == 1:
                    return self.db[list(desiredclientid)[0]]
                else:
                    return self.createNew(firstname)

        else:
            return self.createNew(firstname)

    def getLastDate(self):

        return self.db['Invoice Date'][-1].date()
