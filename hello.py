print("hello")
number = 3
"i eat {0} apples".format(number)
'i eat 3 apples'

number = 10
day = "three"
"i ate {0} apples. so i was sick for {1} days. ".format(number, day)
'i ate apples. so i was sick for three days'

"i ate {number} apples. so i was sick for {day} days.".format(number=10,day=3)
'i ate 10 apples.so i was sick for 3 days'

"i ate {0} apples. so i was sick for {day} days.".format(10, day=3)
'i ate 10 apples. so i was sick for 3 days'

"[0:<10}".format("hi")

"{0:>10}".format("hi")

"{0:<10}".format("hi")

"{0:^10}".format("hi")

"{0:=^10}".format("hi")

"{0:!<10}".format("hi")



y = 3.41234123
"{0:10.3f}".format(y)

