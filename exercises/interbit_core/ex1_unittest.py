import glob
import unittest, os, tempfile, shutil

class TestGlob(unittest.TestCase):
	fnames=['foo.txt', 'bar.txt', 'baz.py']
	def setUp(self):
		"""Create some files in a temp dir."""
		self.dir=tempfile.mkdtemp()
		for fname in self.fnames:
			open(self.absolute(fname), 'w').close()
	def absolute(self, fname):
		return os.path.join(self.dir, fname)
	def tearDown(self):
		"""Delete the temp dir."""
		shutil.rmtree(self.dir)
	def assertGlob(self, pattern, fnames):
		self.assertEqual(sorted(glob.glob(pattern)),sorted(fnames))
	def testCurrentDirGlob(self):
		"""Test globbing in current dir."""
		os.chdir(self.dir)
		self.assertGlob('ba?.*',['bar.txt', 'baz.py'])
	def testAbsoluteGlob(self):
		"""Test globbing with full path."""
		self.assertGlob(self.absolute('*xt'), map(self.absolute, ['foo.txt', 'bar.txt']))
if __name__=='__main__':
	unittest.main()
