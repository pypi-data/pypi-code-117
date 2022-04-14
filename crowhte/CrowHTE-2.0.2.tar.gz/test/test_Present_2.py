import unittest
from unittest.mock import patch

from crow.utils.crow_globals import crow_globals
from crow.uitabs.Present import Present


class TestPresent2(unittest.TestCase):
    """
    Test the various functionalities of Crow.
    """

    def test_Present_6(self):
        """
        Methods of the Present class.
        """
        # test all layouts with error
        cg = crow_globals()
        cg.datafiles = ["test/data/processed_96-well_data_with_errors.csv"]
        pres = Present("test present", cg)
        pres.colorscheme.set(1)
        pres.write_to_file.set(False)
        for layout in range(1, 7):
            pres.layout.set(layout)
            with patch("crow.uitabs.Present.messagebox.showwarning") as test_warning:
                with patch("crow.uitabs.Present.mylog") as test_logger:
                    with patch("crow.uitabs.Present.plot.show") as test_plot:
                        pres.presentbutton.invoke()
                        self.assertTrue(test_plot.called)
                        self.assertTrue(test_warning.called)
                        self.assertTrue(test_logger.called)

    def test_Present_7(self):
        """
        Methods of the Present class.
        """
        # test all layouts with zeros
        cg = crow_globals()
        cg.datafiles = ["test/data/processed_96-well_data_with_zeros.csv"]
        pres = Present("test present", cg)
        pres.colorscheme.set(1)
        pres.write_to_file.set(False)
        for layout in range(1, 7):
            pres.layout.set(layout)
            with patch("crow.uitabs.Present.messagebox.showwarning") as test_warning:
                with patch("crow.uitabs.Present.mylog") as test_logger:
                    with patch("crow.uitabs.Present.plot.show") as test_plot:
                        pres.presentbutton.invoke()
                        self.assertTrue(test_plot.called)
                        self.assertTrue(test_warning.called)
                        self.assertTrue(test_logger.called)

    def test_Present_8(self):
        """
        Methods of the Present class.
        """
        # wrong data type
        cg = crow_globals()
        cg.datafiles = ["test/data/raw_data_1.xml"]
        pres = Present("test present", cg)
        pres.write_to_file.set(False)
        pres.layout.set(1)
        pres.colorscheme.set(1)
        with patch("crow.uitabs.Present.messagebox.showerror") as test_error:
            pres.presentbutton.invoke()
            self.assertTrue(test_error.called)

    def test_Present_9(self):
        """
        Methods of the Present class.
        """
        # no data selected
        cg = crow_globals()
        cg.datafiles = []
        pres = Present("test present", cg)
        pres.write_to_file.set(False)
        pres.layout.set(1)
        pres.colorscheme.set(1)
        with patch("crow.uitabs.Present.messagebox.showerror") as test_error:
            pres.presentbutton.invoke()
            self.assertTrue(test_error.called)

        # too many input files
        cg = crow_globals()
        cg.datafiles = [
            "test/data/processed_96-well_data_with_errors.csv",
            "test/data/processed_96-well_data.csv",
        ]
        pres = Present("test present", cg)
        pres.write_to_file.set(False)
        pres.layout.set(1)
        pres.colorscheme.set(1)
        with patch("crow.uitabs.Present.messagebox.showerror") as test_error:
            pres.presentbutton.invoke()
            self.assertTrue(test_error.called)

        # input file too big
        cg = crow_globals()
        cg.datafiles = [
            "test/data/processed_too_big.csv"
        ]
        pres = Present("test present", cg)
        pres.write_to_file.set(False)
        pres.layout.set(1)
        pres.colorscheme.set(1)
        with patch("crow.uitabs.Present.messagebox.showerror") as test_error:
            pres.presentbutton.invoke()
            self.assertTrue(test_error.called)
