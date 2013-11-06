header= 'Header'
footer= 'Footer'
empty = ""
title = 'Title 1'
title2 = 'Title 2'
paragraph = "Esimene loik tuleb mingi hull pikk lalalalalala "
coun = sum(c.isalpha() for c in paragraph) 


print header.center(60, "=")
print empty.center(60, " ")
print title.center(60, " ")
print empty.center(60, " ")
print paragraph.rjust(50, " ")
	

print empty.center(60, " ")
print title2.center(60, " ")
print empty.center(60, " ")
print paragraph.rjust(50, " ")
print empty.center(60, " ")
print footer.center(60, "=")

