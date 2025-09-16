import test_environment
import unittest
import os
from unittest.mock import MagicMock
from manager import copy_file, remove_file, remove_folder, analyze

#unittest.main()
#Это встроенный метод фреймворка unittest, который:
#Автоматически находит все тестовые методы в классе (начинающиеся с test_).
#Запускает их последовательно.
#Выводит результаты (OK/FAIL).

class TestCopyFiles(unittest.TestCase):
	def test_copy_file_success(self):
		"""
			check for successful copying
		"""
		test_environment.create_environment()
		args = MagicMock()
		#args.origin = "test\\test.txt"
		args.origin = os.path.join(os.getcwd(), "test", "test.txt")
		######
		print(args.origin)
		#args.target = "test\\test.txt"
		args.target = os.path.join(os.getcwd(), "test", "test.txt")
		#new_file_name = "test\\test.txt.copy(1)"
		new_file_name = os.path.join(os.getcwd(), "test", "test.txt.copy(1)")
		self.assertFalse(os.path.exists(new_file_name)) 	# there is no file <new_file_name>     
		self.assertEqual(copy_file(args), 0)  				# copying completed successfully (return 0)
		self.assertTrue(os.path.exists(new_file_name))  	# new file exists
		test_environment.remove_environment()

	def test_copy_file_fail(self):
		"""
			trying to copy non-existent file
		"""
		test_environment.create_environment()
		args = MagicMock()
		#args.origin = "test\\testt.txt"
		args.origin = os.path.join(os.getcwd(), "test", "testt.txt")
		#args.target = "test\\testtt.txt"
		args.target = os.path.join(os.getcwd(), "test", "testtt.txt")
		#new_file_name = "test\\testtt.txt"
		new_file_name = os.path.join(os.getcwd(), "test", "testtt.txt")
		self.assertFalse(os.path.exists(new_file_name))		# there is no file <new_file_name>    
		self.assertEqual(copy_file(args), -1)  				# copying failed (return -1)
		self.assertFalse(os.path.exists(new_file_name)) 	# there is no file <new_file_name>
		test_environment.remove_environment()

class TestDeleteFiles(unittest.TestCase):
	def test_delete_file_success(self):
		"""
			check for successful deleting
		"""
		test_environment.create_environment()
		args = MagicMock()
		#file_to_remove = "test\\test.txt"
		file_to_remove = os.path.join(os.getcwd(), "test", "test.txt")
		args.origin = file_to_remove

		self.assertTrue(os.path.exists(file_to_remove)) 	# file <file_to_remove> exists    
		self.assertEqual(remove_file(args), 0)  			# deleting completed successfully (return 0)
		self.assertFalse(os.path.exists(file_to_remove)) 	# there is no file <file_to_remove>
		test_environment.remove_environment()

	def test_delete_file_fail(self):
		"""
			trying to delete non-existent file
		"""
		test_environment.create_environment()
		args = MagicMock()
		#file_to_remove = "testtt\\test.txt.copy"
		file_to_remove = os.path.join(os.getcwd(), "test", "test.txt.copy")
		args.origin = file_to_remove

		self.assertFalse(os.path.exists(file_to_remove))	# there is no file <file_to_remove>    
		self.assertEqual(remove_file(args), -1)  			# deleting failed (return -1)
		self.assertFalse(os.path.exists(file_to_remove)) 	# there is no file <new_file_name>
		test_environment.remove_environment()

class TestDeleteFolders(unittest.TestCase):
	def test_delete_folder_success(self):
		"""
			check for successful deleting
		"""
		test_environment.create_environment()
		args = MagicMock()
		#folder_to_remove = "test\\test1"
		folder_to_remove = os.path.join(os.getcwd(), "test", "test1")
		args.origin = folder_to_remove

		self.assertTrue(os.path.exists(folder_to_remove)) 	# file <file_to_remove> exists    
		self.assertEqual(remove_folder(args), 0)  			# deleting completed successfully (return 0)
		self.assertFalse(os.path.exists(folder_to_remove)) 	# there is no file <file_to_remove>
		test_environment.remove_environment()

	def test_delete_folder_fail(self):
		"""
			trying to delete non-existent folder
		"""
		test_environment.create_environment()
		args = MagicMock()
		#folder_to_remove = "testtt\\testtt"
		folder_to_remove = os.path.join(os.getcwd(), "test", "testtt")
		args.origin = folder_to_remove

		self.assertFalse(os.path.exists(folder_to_remove))	# there is no file <file_to_remove>    
		self.assertEqual(remove_file(args), -1)  			# deleting failed (return -1)
		self.assertFalse(os.path.exists(folder_to_remove)) 	# there is no file <new_file_name>
		test_environment.remove_environment() 

class TestAnalyze(unittest.TestCase):
	def test_analyze_success(self):
		"""
			check for successful analysis
		"""
		test_environment.create_environment()
		args = MagicMock()
		#folder_to_analize = "test\\test1"
		folder_to_analyze = os.path.join(os.getcwd(), "test", "test1")
		args.origin = folder_to_analyze
		self.assertEqual(analyze(args), 0)  			# deleting completed successfully (return 0)
		test_environment.remove_environment()
		
	def test_analyze_fail(self):
		"""
			trying to analyze non-existent folder
		"""
		test_environment.create_environment()
		args = MagicMock()
		#folder_to_analize = "testtt\\testtt"
		folder_to_analyze = os.path.join(os.getcwd(), "test", "testtt")
		args.origin = folder_to_analyze
		self.assertEqual(remove_file(args), -1)  			# deleting failed (return -1)
		test_environment.remove_environment()		


if __name__ == "__main__":
	unittest.main()	