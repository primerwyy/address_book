__author__ = 'WangYuanYuan'
# Date 2014-3-17
''' This is a address book. Include name, tel, mail'''

import sys
import cPickle as p


class AddressBook:
    ''' Class of Address book'''

    def __init__(self, name, tel, mail):
        self.name = name
        self.tel = tel
        self.mail = mail


address_dirc = {}
address_file = 'address.data'


def WriteData(filename, data):
    '''Write data to the file'''

    f = file(filename, 'w')
    p.dump(data, f)
    f.close()


def ReadData():
    '''Read data from the file'''

    f = file(address_file)
    try:
        return p.load(f)
    except:
        return {}


def Add():
    '''Add object to the address book '''

    name = raw_input('Name: ')
    if len(name) == 0:
        print 'Name can\'t be empty!'
        sys.exit()

    tel = raw_input('Tel: ')
    mail = raw_input('Mail: ')

    if isInAddress(name):
        s = AddressBook(name, tel, mail)
        address_dirc = ReadData()
        address_dirc[s.name] = [s.tel, s.mail]
        WriteData(address_file, address_dirc)
    else:
        print '{0} already existed!'.format(name)


def Search(name):
    address_dirc = ReadData()
    for item in address_dirc:
        if item == name:
            return 'Name: {0}\nTel: {1}\nMail: {2}'\
                .format(item, address_dirc[item][0], address_dirc[item][1])
    return  '{0} not in the address '.format(name)


def Del(name):
    address_dirc = ReadData()
    for item in address_dirc:
        if item == name:
            del address_dirc[item]
        else:
            print 'del pearson ont exist'

    WriteData(address_file, address_dirc)


def Help():
    print '''
        Address Book    version_1.0    Author: WYY
        Option include:
        -A             add person to the address book
        -H             help information
        -S [option]    search person in address book
        -D [option]    delete person
        '''
    ReadData()

def isInAddress(name):
    address = ReadData()
    if name in address:
        return False
    return True


def AddressNumbers():
    '''Count the numbers of address book '''
    address_dirc = ReadData()
    return len(address_dirc)


if len(sys.argv) < 2:
    print 'No action specified'
    sys.exit()

if sys.argv[1].startswith('-'):
    option = sys.argv

    if option[1][1:] == 'A':
        Add()
    elif option[1][1:] == 'D':
        Del(option[2])
    elif option[1][1:] == 'S':
        print Search(option[2])
    elif option[1][1:] == 'H':
        Help()
    else:
        print 'address book no this action !'
if sys.argv[1] == 'quit':
    sys.exit()
