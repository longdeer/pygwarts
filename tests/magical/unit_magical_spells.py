import	unittest
from	math					import inf
from	pygwarts.magical.spells	import flagrate
from	pygwarts.tests.magical	import MagicalTestCase








class SpellsCases(MagicalTestCase):
	def test_flagrate_singular(self):

		self.assertEqual(flagrate(1),"")
		self.assertEqual(flagrate(-1),"")
		self.assertEqual(flagrate("1"),"")
		self.assertEqual(flagrate("-1"),"")
		self.assertEqual(flagrate(""),"")
		self.assertEqual(flagrate("True"),"")
		self.assertEqual(flagrate("False"),"")
		self.assertEqual(flagrate("None"),"")
		self.assertEqual(flagrate(True),"")
		self.assertEqual(flagrate(None),"")
		self.assertEqual(flagrate([ 42 ]),"")
		self.assertEqual(flagrate(( 42, )),"")
		self.assertEqual(flagrate({ 42, }),"")
		self.assertEqual(flagrate({ 42: 42, }),"")
		self.assertEqual(flagrate(print),"")
		self.assertEqual(flagrate(...),"")
		self.assertEqual(flagrate(self),"")
		self.assertEqual(flagrate(ValueError),"")

	def test_flagrate_plural(self):

		self.assertEqual(flagrate(False),"s")
		self.assertEqual(flagrate(0),"s")
		self.assertEqual(flagrate(0.),"s")
		self.assertEqual(flagrate(.0),"s")
		self.assertEqual(flagrate(-0),"s")
		self.assertEqual(flagrate(-0.),"s")
		self.assertEqual(flagrate(-.0),"s")
		self.assertEqual(flagrate("0"),"s")
		self.assertEqual(flagrate("0."),"s")
		self.assertEqual(flagrate(".0"),"s")
		self.assertEqual(flagrate("-0"),"s")
		self.assertEqual(flagrate("-0."),"s")
		self.assertEqual(flagrate("-.0"),"s")
		self.assertEqual(flagrate(1.),"s")
		self.assertEqual(flagrate(-1.),"s")
		self.assertEqual(flagrate("1."),"s")
		self.assertEqual(flagrate("-1."),"s")
		self.assertEqual(flagrate(2),"s")
		self.assertEqual(flagrate(2.),"s")
		self.assertEqual(flagrate(10),"s")
		self.assertEqual(flagrate(10.1),"s")
		self.assertEqual(flagrate(100500),"s")
		self.assertEqual(flagrate(-2),"s")
		self.assertEqual(flagrate(-2.),"s")
		self.assertEqual(flagrate(-10),"s")
		self.assertEqual(flagrate(-10.1),"s")
		self.assertEqual(flagrate(-100500),"s")
		self.assertEqual(flagrate("2"),"s")
		self.assertEqual(flagrate("2."),"s")
		self.assertEqual(flagrate("10"),"s")
		self.assertEqual(flagrate("10.1"),"s")
		self.assertEqual(flagrate("100500"),"s")
		self.assertEqual(flagrate("-2"),"s")
		self.assertEqual(flagrate("-2."),"s")
		self.assertEqual(flagrate("-10"),"s")
		self.assertEqual(flagrate("-10.1"),"s")
		self.assertEqual(flagrate("-100500"),"s")
		self.assertEqual(flagrate(1E1),"s")
		self.assertEqual(flagrate(2E200),"s")
		self.assertEqual(flagrate(-1E1),"s")
		self.assertEqual(flagrate(-2E200),"s")
		self.assertEqual(flagrate("1E1"),"s")
		self.assertEqual(flagrate("2E200"),"s")
		self.assertEqual(flagrate("-1E1"),"s")
		self.assertEqual(flagrate("-2E200"),"s")
		self.assertEqual(flagrate(inf),"s")
		self.assertEqual(flagrate(-inf),"s")
		self.assertEqual(flagrate("inf"),"s")
		self.assertEqual(flagrate("-inf"),"s")








if __name__ == "__main__" : unittest.main(verbosity=2)







