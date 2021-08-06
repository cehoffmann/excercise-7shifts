import unittest
import StringCalculator

class TestCalculator(unittest.TestCase):
    # Test block for strings of valid integers
    def test_Add_ValidNumbers(self):
        # Tests simple strings of valid numbers
        self.assertEqual(StringCalculator.Add("1,2,3,4,5,6"), 21)
        self.assertEqual(StringCalculator.Add("35,2,124,578,622,412,1000"), 2773)
        self.assertEqual(StringCalculator.Add("21,24,23,24,18,365,1,45,2,854,36,27,58,69,24,74,85"), 1750)
    
    # Tests block for strings with numbers over 1000 which will be ignored
    def test_Add_IgnoresHighNumbers(self):        
        self.assertEqual(StringCalculator.Add("1,2,3,4,5,6,1024,10,2754,96854,2,3,4,1001"), 40)
        self.assertEqual(StringCalculator.Add("1,1024,3,5427,1000,5,1247"), 1009)
        self.assertEqual(StringCalculator.Add("25,4485,87252,2"), 27)

    #Test Block for string containing line feeds
    def test_Add_LineFeed(self):
        self.assertEqual(StringCalculator.Add("7,\n5,2"), 14)
        self.assertEqual(StringCalculator.Add("8\n,14,587"), 609)
        self.assertEqual(StringCalculator.Add("654,13,865\n,\n578"), 2110)
    
    # Tests block for strings with custom delimiters
    def test_Add_CustomDelimiters(self):
        self.assertEqual(StringCalculator.Add("//#\n54#8#765#54#224"), 1105)
        self.assertEqual(StringCalculator.Add("//#,@\n1#2@3#5@8"), 19)
        self.assertEqual(StringCalculator.Add("//#,%,^,@\n6#54@354@12^435%47"), 908)

    # Tests block for strings with custom delimiters, and line feeds
    def test_Add_CustomDelimiterLineFeed(self):
        self.assertEqual(StringCalculator.Add("//@\n3@25@4\n@120"), 152)
        self.assertEqual(StringCalculator.Add("//#,!,$\n#88\n!24$34!756\n45$65"), 1012)
        self.assertEqual(StringCalculator.Add("//@,$,%,^,&\n@6$3\n%547^\n35\n&74"), 665)

    # Tests block for strings with custom delimiters, and line feeds, and negative numbers
    def test_Add_CustomDelimiterLineFeedNegatives(self):
        with self.assertRaises(ValueError) as singleNeg:
            self.assertEqual(StringCalculator.Add("//$\n658$74$4$-55$41"), 832)
        self.assertEqual("Negative numbers are not allowed. -55", str(singleNeg.exception))

        with self.assertRaises(ValueError) as doubleNeg:
            self.assertEqual(StringCalculator.Add("//!,@,#\n9!\n-887@32\n#\n-427"), 152)
        self.assertEqual("Negative numbers are not allowed. -887, -427", str(doubleNeg.exception))

        with self.assertRaises(ValueError) as multipleNegs:
            self.assertEqual(StringCalculator.Add("//!@#$%^&\n-653!-43@547#-63$-546%-5^-8&-41"), 1012)
        self.assertEqual("Negative numbers are not allowed. -653, -43, -63, -546, -5, -8, -41", str(multipleNegs.exception))

    # Tests block to validate the existance of a number
    def test_Add_NoNumber(self):
        with self.assertRaises(ValueError) as null:
            StringCalculator.Add("")
        self.assertEqual("You haven't entered any valid numbers.", str(null.exception))

        with self.assertRaises(ValueError) as empty:
            StringCalculator.Add("       ")
        self.assertEqual("You haven't entered any valid numbers.", str(empty.exception))

        with self.assertRaises(ValueError) as noNumbers:
            StringCalculator.Add("^,%,&,,$$,!@,a,g,t%,  ,   , ")
        self.assertEqual("You haven't entered any valid numbers.", str(noNumbers.exception))
    
    # Tests with negative numbers, throws exception and list negative numbers
    def test_Add_NegativeNumbers(self):
        with self.assertRaises(ValueError) as negativeError:
            StringCalculator.Add("25,4,589,784,56,-21,54")
        self.assertEqual("Negative numbers are not allowed. -21", str(negativeError.exception))

        with self.assertRaises(ValueError) as negativeError:
            StringCalculator.Add("-6\n,-35,1,\n-3,-65,-74")
        self.assertEqual("Negative numbers are not allowed. -6, -35, -3, -65, -74", str(negativeError.exception))

        with self.assertRaises(ValueError) as negativeError:
            StringCalculator.Add("9,-8\n,76,\n-45")
        self.assertEqual("Negative numbers are not allowed. -8, -45", str(negativeError.exception))

if __name__ == "__main__":
    unittest.main()