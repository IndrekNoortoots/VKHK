# coding: latin-1
print '{:^75}'.format('Arve')
print
head = '{:<30} {:<20} {:<20} {:>10}'
head_2 = '{:<30} {:<21} {:<21} {:>10}'
head_3 = '{:<29} {:<10}'
body = '{:<19}{:>15}{:>15}{:>15}'
price = '{:>49}{:>15}'
prce = '{:>50}{:>15}'

footer = '{:<19}{:<15}'
print head.format('Arve väljastaja', 'Arve saaja','Arve number:','0001')
print head_2.format('Villu Pomm', 'Peeter Pesupäev','Kuupäev:','07.11.2013')
print head_3.format('Oksa 1','Männi 2')
for x in xrange(1,5):
    print
    pass
print body.format('Kaup','Hind','Kogus','Kokku')
print body.format('Hapukapsas','5 KG','1','5')
print body.format('Kartul','5','1 KG','5')
print 
print price.format('Vahesumma', '10')
print prce.format('Käibemaks 20%', '10,6')
print price.format('Kokku', '20,60')
for x in xrange(1,2):
    print
    pass
print footer.format('Kontaktid','Arveldus')
print footer.format('villu@gmail.com','Swedbank')
print footer.format('telefon:1135135 ','IBN 14535135135135')
