import os
from bullet import Password

item = {'Name' : [], 'Details' : []}
account = ''

class Home:
  def __init__(self,op):
    global account
    if op == 1:
      os.system('clear')
      print('\033[93m'+'Login Form'+'\033[0m')
      admin_user = input('Username : ')
      cli = Password(prompt = 'Password : ',hidden = '•')
      password = cli.launch()

      if admin_user == 'smglobalshop' and password == 'admin_sm127':
        account = 'Admin'
        input('login success.')
      else:
        raise TypeError

    elif op == 2:
      os.system('clear')
      account = 'User'

class Admin:
  def __init__(self):
    # private
    self.__name = 'Item Name'
    self.__price = 0
    self.__discount = 0

    # all item name
    if os.path.exists('admin/item list.txt'):
      file = open('admin/item list.txt','r')
      item['Name'] = file.readlines()
      file.close()
    else:
      file = open('admin/item list.txt','x')
    
    # details
    for name in item['Name']:
      f = open('admin/'+name[:-1]+'.txt','r')
      item['Details'].append(f.readlines())
      f.close()

  @property
  def setName(self):
    pass
  
  @setName.setter
  def setName(self,name):
    self.__name = name
  
  @property
  def getName(self):
    pass
  
  @getName.getter
  def getName(self):
    return self.__name
  
  @property
  def setPrice(self):
    pass
  
  @setPrice.setter
  def setPrice(self,price):
    self.__price = price + (price*0.1)
  
  @property
  def getPrice(self):
    pass
  
  @getPrice.getter
  def getPrice(self):
    return self.__price
  
  @property
  def setDiscount(self):
    pass
  
  @setDiscount.setter
  def setDiscount(self,discount):
    self.__discount = discount
  
  @property
  def getDiscount(self):
    pass

  @getDiscount.getter
  def getDiscount(self):
    return self.__discount
  
  @property
  def setEditPrice(self):
    pass

  @setEditPrice.setter
  def setEditPrice(self,price):
    self.__price = price

  @property
  def getPriceDiscount(self):
    pass

  @getPriceDiscount.getter
  def getPriceDiscount(self):
    self.__price -= self.__price*(self.__discount/100)
    return self.__price 
  
  def inputFile(self,name,price,discount,dis_price):
    f = open('admin/'+name+'.txt','w')
    f.write(name+'\n'+str(price)+'\n'+str(discount)+'\n'+str(dis_price)+'\n')
    f.close()

    f = open('admin/item list.txt','a')
    f.write(name+'\n')
    f.close()
  
  def showAll(self):
    os.system('clear')
    print('\033[95m'+'SM Entertainment Global Shop'+'\033[0m')

    print('{:<5}{:<25}{:<15}{:<15}{:<15}'.format('No.','Name','Normal Price','Discount','Discounted Price'))

    for i in range(len(item['Name'])):
      print('{:<5}{:<25}{:<15}{:<15}{:<15}'.format(i+1,item['Details'][i][0][:-1],item['Details'][i][1][:-1],item['Details'][i][2][:-1]+'%',item['Details'][i][3][:-1]))
  
  def editItem(self,editNumber,editProperty):
    item['Details'][editNumber-1][editProperty-1] = input('New Value : ').title()+'\n'

    ask = input('Are you sure? (Y/N) ').upper()
    if ask == 'Y':
      a.setEditPrice = round(float(item['Details'][editNumber-1][1][:-1]))
      a.setDiscount = round(float(item['Details'][editNumber-1][2][:-1]))
      item['Details'][editNumber-1][3] = str(a.getPriceDiscount)+'\n'

      os.remove('admin/'+item['Name'][editNumber-1][:-1]+'.txt')
      item['Name'][editNumber-1] = item['Details'][editNumber-1][0]

      f = open('admin/'+item['Details'][editNumber-1][0][:-1]+'.txt','w')
      for details in item['Details'][editNumber-1]:
        f.write(details)
      f.close()

      f = open('admin/item list.txt','w')
      for name in item['Name']:
        f.write(name)
      f.close()

      input('\n\nThe data has been edited.')
  
  def delete(self):
    delOption = input("Which item do you want to delete? *fill with item number/type 'all' to delete all item\n").lower()
    delOption2 = input('Are you sure? (Y/N) ').upper()
    if delOption == 'all' and delOption2 == 'Y':
      for name in item['Name']:
        os.remove('admin/'+name[:-1]+'.txt')
      item['Name'].clear()
      input('\n\nAll item have been deleted.')
    elif delOption.isdigit() and delOption2 == 'Y':
      os.remove('admin/'+item['Name'][int(delOption)-1][:-1]+'.txt')
      item['Name'].pop(int(delOption)-1)
      input('\n\nThe item has been deleted.')
    
    f = open('admin/item list.txt','w')
    for name in item['Name']:
      f.write(name)
    f.close()

class User:
  wishlist = []

  def __init__(self):
    global wishlist
    if os.path.exists('user/wishlist.txt'):
      file = open('user/wishlist.txt','r')
      wishlist = file.readlines()
      file.close()
    else:
      file = open('user/wishlist.txt','x')
  
  def search(self,name):
    if name+'\n' in item['Name']:
      print('\nItem Found :')
      print('\033[3m'+'Item Name : '+item['Details'][item['Name'].index(name+'\n')][0][:-1])
      print('Discount Price : '+item['Details'][item['Name'].index(name+'\n')][3][:-1]+'\033[0m')
      input('\n\nENTER to continue.')
    else:
      raise TypeError

  def show(self):
    os.system('clear')
    print('\033[95m'+'SM Entertainment Global Shop'+'\033[0m')

    print('{:<5}{:<25}{:<15}'.format('No.','Name','Discounted Price'))

    for i in range(len(item['Name'])):
      print('{:<5}{:<25}{:<15}'.format(i+1,item['Details'][i][0][:-1],item['Details'][i][3][:-1]))
  
  def wishlist(self):
    print('\033[94m'+'\033[1m'+'My Wishlist'+'\033[0m')
    if len(wishlist) > 0:
      print('{:<25}{:<15}'.format('Name','Discounted Price'))

      for name in wishlist:
        print('{:<25}{:<15}'.format(item['Details'][item['Name'].index(name)][0][:-1],item['Details'][item['Name'].index(name)][3][:-1]))
    else:
      print('\033[1m'+'You have not added any wishlist!'+'\033[0m')

  def wishFunc(self,option):
    if option == '1':
      os.system('clear')
      print('{:<5}{:<25}{:<15}'.format('No.','Name','Discounted Price'))

      for i in range(len(item['Name'])):
        print('{:<5}{:<25}{:<15}'.format(i+1,item['Details'][i][0][:-1],item['Details'][i][3][:-1]))

      op_wish1 = int(input('\n\nWhich item do you want to add? : '))-1
      if item['Name'][op_wish1] not in wishlist:
        wishlist.append(item['Name'][op_wish1])
        input('\n\nitem added.')
      else:
        input('\n\nyou have added it before. please choose another one.')

    elif option == '2':
      op_wish2 = input('Which item do you want to delete? : ').title()+'\n'
      if op_wish2 in wishlist:
        ask = input('Are you sure? (Y/N) ').upper()
        if ask == 'Y':
          wishlist.remove(op_wish2)
          input('\n\nitem removed.')
      else:
        input('\n\nno such item found. please type correctly...')

    f = open('user/wishlist.txt','w')
    for name in wishlist:
      f.write(name)
    f.close()

  def ourStore(self):
    os.system('clear')
    print('\033[92m'+'\033[3m'+'About Us'+'\033[0m')
    print("""\nSM Global Shop, (D.B.A. Urban Coconut) is the official SM Entertainment fashion merchandise store. We carry fashion merchandise of sensational K-pop groups: EXO, Super Junior, Girls' Generation, Red Velvet, NCT, NCT127, SHINee, TVXQ!, f(x) and more.

Majority of our sales support SM Entertainment Artists so they can provide all of their fans with more music to enjoy! *All album sales from SM Global Shop officially count toward Billboard Charts (US orders ONLY) and Gaon Charts (Both International + US orders)

We are proud to have partnered with Korean Wave #1 leader SM Entertainment to provide you with K-Pop apparel and accessories to spread Korean culture and artists globally. Our mission is to make it easier for SM Entertainment fans all around the world to purchase authentic beloved artists goods!""")
    
      
if __name__ == "__main__":
  while account == '':
    try:
      print('\033[92m'+'SM Entertainment Global Shop'+'\033[0m')
      op = int(input('1. Admin\n2. User\nNumber : '))
      h = Home(op)
    except TypeError:
      input('username/password did not match! please try again...')
    os.system('clear')

  while account == 'Admin' :
    try:
      a = Admin()
      os.system('clear')
      print('\033[92m'+'SM Entertainment Global Shop\nWelcome Admin!'+'\033[0m')
      op1 = int(input('1. Input\n2. Show\n3. Edit\n4. Delete\n5. Log Out\nNumber : '))
      if op1 == 1:
        print('\033[94m'+'\n\nInput Form'+'\033[0m')
        a.setName = input('Name : ').title()
        a.setPrice = int(input('Price : '))
        a.setDiscount = int(input('Discount : '))
        a.inputFile(a.getName,a.getPrice,a.getDiscount,a.getPriceDiscount)
        input('\n\nItem added.')
      elif op1 == 5 :
        account = 'user'
        break
      else:
        if len(item['Name']) > 0 :
          if op1 == 2 :
            c = Admin()
            c.showAll()
            input('\n\nENTER to continue.')
          elif op1 == 3 :
            a.showAll()
            print()
            a.editItem(int(input('Which item do you what to edit? *fill with item number : ')),int(input('\nEdit Form\n1. Name\n2. Normal Price\n3. Discount\nNumber : ')))
          elif op1 == 4 :
            a.showAll()
            a.delete()
          elif op1 == 5 :
            account = ''
          else:
            raise ValueError
        else:
          raise IndexError
    except ValueError:
      input('\n\nPlease choose between 1-5...')
    except IndexError:
      input('\n\nNo item found...')
  
  while account == 'User':
    try:
      os.system('clear')
      print('\033[92m'+'SM Entertainment Global Shop\nWelcome User!'+'\033[0m')
      user = User()
      data = Admin()
      if len(item['Name']) > 0:
        op = int(input('1. Search\n2. Show All Item\n3. Wishlist\n4. About Us\n5. Log Out\nNumber : '))
        if op == 1:
          search = input('\nSearch : ').title()
          user.search(search)
        elif op == 2:
          user.show()
          input('\n\nENTER to continue.')
        elif op == 3:
          os.system('clear')
          user.wishlist()
          wish = input('\n\npress 1 to add wishlist, press 2 to delete wishlist or ENTER to continue ')
          user.wishFunc(wish)
        elif op == 4:
          user.ourStore()
          input('\n\nENTER to continue.')
        elif op == 5:
          account = ''
        else:
          raise ValueError
      else:
        print()
        input('Dear User,\nSM Global Shop is currently cleaning all of the item. Once the item is added, you will be able to access all of the feature. Thank you for your understanding!\n\nSM Entertainment')
        account = ''
    except ValueError:
      input('\n\nPlease choose between 1-5...')
    except TypeError:
      input('\n\nNo such item found...')


