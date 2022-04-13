import os
import ast
import glob
import numpy as np
import pandas as pd
from astropy.io import ascii
import multiprocessing as mp
from astropy.stats import mad_std




# Package mode
from . import models
from . import SYDFILE, PYSYDFILE
from . import INFDIR, INPDIR, OUTDIR


class PySYDInputError(Exception):
    """Class for pySYD user input errors."""
    def __repr__(self):
        return "PySYDInputError"
    __str__ = __repr__

class PySYDProcessingError(Exception):
    """Class for pySYD processing exceptions."""
    def __repr__(self):
        return "PySYDProcessingError"
    __str__ = __repr__

class PySYDInputWarning(Warning):
    """Class for pySYD user input warnnings."""
    def __repr__(self):
        return "PySYDInputWarning"
    __str__ = __repr__


class Constants:
    """
    
    Container class for constants and known values -- which is
    primarily solar asteroseismic values for our purposes.
    
    """

    def __init__(self, defaults=['solar','conversions','constants']):
        """
        UNITS ARE IN THE SUPERIOR CGS 
        COME AT ME

        """
        self.constants = {}
        params = dict(
            m_sun = 1.9891e33,
            r_sun = 6.95508e10,
            rho_sun = 1.41,
            teff_sun = 5777.0,
            logg_sun = 4.4,
            teffred_sun = 8907.0,
            numax_sun = 3090.0,
            dnu_sun = 135.1,
            width_sun = 1300.0,
            tau_sun = [5.2e6,1.8e5,1.7e4,2.5e3,280.0,80.0],
            tau_sun_single = [3.8e6,2.5e5,1.5e5,1.0e5,230.,70.],
            G = 6.67428e-8,
            cm2au = 6.68459e-14,
            au2cm = 1.496e+13,
            rad2deg = 180./np.pi,
            deg2rad = np.pi/180.,
        )
        self.constants.update(params)

    def __repr__(self):
        return "<Constants>"


class Parameters(Constants):
    """

    Container class for ``pySYD``

    """

    def __init__(self, args=None, stars=None):
        """

        Calls super method to inherit all relevant constants and then
        stores the default values for all pysyd modules

        Methods

        """
        # makes sure to inherit constants
        super().__init__()
        self.get_defaults()
        if not self.is_interactive():
            self.add_cli(args)
        else:
            if stars is None:
                self.star_list()
            else:
                self.params['stars'] = stars
        self.assign_stars()

    def __repr__(self):
        return "<pysyd Parameters>"


    def is_interactive(self):
        import __main__ as main
        return not hasattr(main, '__file__')


    def get_defaults(self, params={}):
        """
        Loads default parameter information - completely analagous to the parsers available
        via command line (including how/when they are loaded in)
    
        Calls
            :mod:`pysyd.utils.Parameters.get_high`
            :mod:`pysyd.utils.Parameters.get_data`
            :mod:`pysyd.utils.Parameters.get_main`

        Attributes
            params : Dict[str[Dict[,]]]
                container class for ``pySYD`` parameters


        """
        self.params = {}
        # Initialize high level functionality
        self.get_high()
        # Get parameters related to data loading/saving
        self.get_data()
        # Initialize main 'params' dictionary
        self.get_main()
        # Get plotting info
        self.get_plotting()


    def get_high(self, inpdir='data', infdir='info', outdir='results', save=True, verbose=False, 
                 overwrite=False, cli=False, notebook=False,):
        """
   
        Get the parameters for higher-level functionality

        Parameters
            inpdir : str
                path to input data (default='data/')
            infdir : str
                path to star information (default='info/')
            outdir : str
                path to results (default='results/')
            save : bool, optional
                save all data products
            verbose : bool, optional
                turn on verbose output
            overwrite : bool, optional
                allow files to be overwritten by new ones
            cli : bool, optional
                this should not be touched - there is a function that determines this automatically
            notebook : bool, optional
                this should not be altered either - there is a function that determines this automatically

        Attributes
            params : Dict[str,Dict[,]]
                the updated parameters


        """
        high = dict(
            inpdir = os.path.join(os.path.abspath(os.getcwd()), INPDIR),
            infdir = os.path.join(os.path.abspath(os.getcwd()), INFDIR),
            outdir = os.path.join(os.path.abspath(os.getcwd()), OUTDIR),
            save = save,
            verbose = verbose,
            overwrite = overwrite,
            cli = cli,
            notebook = notebook,
        )
        self.params.update(high)


    def get_data(self, stars=None, todo='todo.txt', info='star_info.csv', mode='load',
                 gap=20, stitch=False, oversampling_factor=None, kep_corr=False, dnu=None, 
                 lower_ech=None, upper_ech=None, notching=False,):
        """
   
        Get the parameters related to data manipulation and initial loading

        Parameters
            stars : List[str], optional
                list of targets to process. If `None`, will read in from `info/todo.txt` (default).
            todo : str
                path to star list to process (default='info/todo.txt')
            info : str
                path to star csv info (default='info/star_info.csv')
            mode : str, optional
                which `pySYD` mode (default=`'load'`)
            gap : int, optional
                n times the number of cadences defines a "gap" (to correct for)
            stitch : bool, optional
                use the module that corrects for large gaps in data
            oversampling_factor : int, optional
                oversampling factor of input power spectrum
            kep_corr : bool, optional
                use the module that corrects for known kepler artefacts
            dnu : float, optional
                spacing to fold PS in order to "whiten" mixed modes (**Note:** requires all 3 args)
            lower_ech : float
                lower bound of folded PS (in muHz) to 'whiten' mixed modes (default = `None`)
            upper_ech : float
                upper bound of folded PS (in muHz) to 'whiten' mixed modes (default = `None`)
            notching : bool, optional
                option to use notching technique (vs. simulating white noise, default = `False`)

        Attributes
            params : Dict[str,Dict[,]]
                the updated parameters


        """
        data = dict(
            stars = stars,
            info = os.path.join(os.path.abspath(os.getcwd()), INFDIR, info),
            todo = os.path.join(os.path.abspath(os.getcwd()), INFDIR, todo),
            mode = mode,
            gap = gap,
            stitch = stitch,
            oversampling_factor = oversampling_factor,
            kep_corr = kep_corr,
            dnu = dnu,
            lower_ech = lower_ech,
            upper_ech = upper_ech,
            notching = notching,
        )
        self.params.update(data)


    def get_main(self, n_threads=0,):
        """
   
        Container class analagous to the `'main'` parser

        Parameters
            n_threads : int
                number of threads to use when running in parallel mode

        Calls
            :mod:`pysyd.utils.Parameters.get_estimate`
            :mod:`pysyd.utils.Parameters.get_background`
            :mod:`pysyd.utils.Parameters.get_global`
            :mod:`pysyd.utils.Parameters.get_sampling`

        Attributes
            params : Dict[str,Dict[,]]
                the updated parameters

        .. seealso::


        """
        # Initialize parameters for the find excess routine
        self.get_estimate()
        # Initialize parameters for the fit background routine
        self.get_background()
        # Initialize parameters relevant for estimating global parameters
        self.get_global()
        # Estimate parameters
        self.get_sampling()
        self.params.update({'n_threads':n_threads})


    def get_estimate(self, excess=True, smooth_width=10.0, binning=0.005, bin_mode='mean', 
                     step=0.25, n_trials=3, ask=False, lower_ex=1.0, upper_ex=8000.0,):
        """
    
        Get the parameters for the find excess routine.

        Parameters
            excess : bool, optional
                disable the module that estimates numax
            smooth_width: float, optional
                box filter width (in :math:`\rm \mu Hz`) to smooth power spectrum
            binning : float, optional
                logarithmic binning width. Default value is `0.005`.
            bin_mode : {'mean', 'median', 'gaussian'}
                mode to use when binning
            step : float, optional
                TODO: Write description. Default value is `0.25`.
            n_trials : int, optional
                the number of trials. Default value is `3`.
            ask : bool, optional
                If `True`, it will ask which trial to use as the estimate for numax.
            lower_ex : float, optional
                lower frequency limit of PS to use in the first module
            upper_ex : float, optional
                upper frequency limit of PS to use in the first module

        .. seealso:: methods :py:mod:`utils.Parameters.get_background`, :py:mod:`utils.Parameters.get_global`

        Attributes
            params : Dict[str,Dict[,]]
                the updated parameters

        """
        estimate = dict(
            excess = excess,
            smooth_width = smooth_width,
            binning = binning,
            bin_mode = bin_mode,
            step = step,
            n_trials = n_trials,
            ask = ask,
            lower_ex = lower_ex,
            upper_ex = upper_ex,
        )
        self.params.update(estimate)


    def get_background(self, background=True, ind_width=20.0, box_filter=1.0, n_rms=20, metric='bic', mc_iter=1, 
                       samples=False, n_laws=None, fix_wn=False, basis='tau_sigma', lower_bg=1.0, upper_bg=8000.0,):
        """
    
        Get defaults for the background-fitting routine

        Parameters
            background : bool, optional
                disable the background-fitting routine (not recommended)
            basis : str
                which basis to use for background fitting, e.g. {a,b} parametrization (default = `tau_sigma`)
            box_filter : float
                the size of the 1D box smoothing filter (default = `1.0` :math:`\\rm \\mu Hz`)
            ind_width : float
                the independent average smoothing width (default = `20.0` :math:`\\rm \\mu Hz`)
            n_rms : int
                number of data points to estimate red noise contributions (default = `20`)
            n_laws : int
                force number of Harvey-like components in background fit (default = `None`)
            fix_wn : bool
                fix the white noise level in the background fit (default = `False`)
            metric : str
                which metric to use (i.e. bic or aic) for model selection (default = `'bic'`)
            lower_bg : float, optional
                lower frequency limit of PS to use for the background fit
            upper_bg : float, optional
                upper frequency limit of PS to use for the background fit
            functions : Dict[int:pysyd.models]
                pointer function to different models for the background fit

        Attributes
            params : Dict[str,Dict[,]]
                the updated parameters


        """
        background = dict(
            background = background,
            basis = basis,
            box_filter = box_filter,
            ind_width = ind_width,
            n_rms = n_rms,
            n_laws = n_laws,
            fix_wn = fix_wn,
            metric = metric,
            lower_bg = lower_bg,
            upper_bg = upper_bg,
            functions = get_dict(type='functions'),
        )
        self.params.update(background)


    def get_global(self, globe=True, numax=None, lower_ps=None, upper_ps=None, ex_width=1.0, 
                   sm_par=None, smooth_ps=2.5, threshold=1.0, method='D', n_peaks=5,):
        """
    
        Get defaults for deriving global asteroseismic parameters :math:`\\rm \\nu_{max}` 
        and :math:`\\Delta\\nu`

        Parameters
            globe : bool, optional
                disable the module that fits the global parameters (also not recommended)
            numax : float, optional
                provide initial value for numax to bypass the first module
            lower_ps : float, optional
                lower bound of power excess to use for :term:`ACF` [in :math:`\\rm \mu Hz`]
            upper_ps : float
                upper bound of power excess to use for :term:`ACF` [in :math:`\\rm \mu Hz`]
            ex_width : float
                fractional width to use for power excess centered on :term:`numax`
            sm_par : float
                Gaussian filter width for determining smoothed numax (values are typically between 1-4)
            smooth_ps : float
                box filter to smooth PS smoothing before calculating the ACF (default = `1.5` :math:`\\rm \\mu Hz`)
            threshold : float
                fractional width of FWHM to use in ACF for later iterations (default = `1.0`) 
            method : str
                method to determine dnu, choices are ~['M','A','D'] (default is `'D'`)
            n_peaks : int
                the number of peaks to select (default = `10`)

        Attributes
            params : Dict[str,Dict[,]]
                the updated parameters


        """
        globe = dict(
            globe = globe,
            numax = numax,
            lower_ps = lower_ps,
            upper_ps = upper_ps,
            ex_width = ex_width,
            sm_par = sm_par,
            smooth_ps = smooth_ps,
            threshold = threshold,
            method = method,
            n_peaks = n_peaks,
        )
        self.params.update(globe)


    def get_sampling(self, mc_iter=1, samples=False,):
        """
    
        Get parameters relevant for estimating uncertainties

        Parameters
            mc_iter : int
                number of samples used to estimate uncertainty (default = `1`)
            samples : bool
                save samples from the monte carlo sampling (default = `False`)

        Attributes
            params : Dict[str,Dict[,]]
                the updated parameters


        """
        mcmc = dict(
            mc_iter = mc_iter,
            samples = samples,
        )
        self.params.update(mcmc)



    def get_plotting(self, showall=False, show=False, cmap='binary', clip_value=3.0, hey=False,
                     interp_ech=False, nox=None, noy='0+0', npb=10, smooth_ech=None,):
        """
    
        Get defaults for deriving global asteroseismic parameters :math:`\\rm \\nu_{max}` 
        and :math:`\\Delta\\nu`

        Parameters
            showall : bool, optional
                makes plot comparing all background models (default = `False`)
            show : bool
                show output figures (default = `True`) **note:** this is not recommended when running on many stars
            cmap : str, optional
                change colormap of echelle diagram (default = `'binary'`)
            clip_value : float
                the minimum frequency of the echelle plot. Default value is `3.0`.
            hey : bool
                plugin for Daniel Hey's echelle package (NOT CURRENTLY IMPLEMENTED YET)
            interp_ech : bool
                turns on the bilinear smoothing in echelle plot
            nox : int
                x-axis resolution on the echelle diagram - default uses spacing and resolution to calculate appropriate value
            noy : str
                how many radial orders to plot on the echelle diagram (default = `'5+0'` ) NEW: and how many orders to shift the ED by
            npb : int
                instead of specifying arbitrary value, provide how many frequencies should be in a given bin
            smooth_ech : float
                option to smooth the output of the echelle plot

        Attributes
            params : Dict[str,Dict[,]]
                the updated parameters


        """
        plot = dict(
            showall = showall,
            show = show,
            cmap = cmap,
            hey = hey,
            clip_value = clip_value,
            interp_ech = interp_ech,
            nox = nox,
            noy = noy,
            npb = npb,
            smooth_ech = smooth_ech,
        )
        self.params.update(plot)


    def add_stars(self, stars=None):
        if stars is not None:
            self.params['stars'] = stars
        else:
            raise PySYDInputError("ERROR: no star provided")
        self.assign_stars()


    def assign_stars(self,):
        """
        Add target stars

        This routine will load in target stars, sets up "groups" (relevant for parallel
        processing) and then load in the relevant information

        Parameters
            stars : List[str]
                list of stars to process
            todo : str, optional
                list of stars to process
            mode : str
                which pysyd mode to run

        """
        # Set file paths and make directories if they don't yet exist
        for star in self.params['stars']:
            self.params[star] = {}
            self.params[star]['path'] = os.path.join(self.params['outdir'], str(star))
            if self.params['save'] and not os.path.exists(self.params[star]['path']):
                os.makedirs(self.params[star]['path'])
        self.get_groups()
        self.add_info()


    def star_list(self,):
        """

        Add targets

        """
        # If no stars have been provided yet, read in from text file
        if not os.path.exists(os.path.join(self.params['infdir'], self.params['todo'])):
            raise PySYDInputError("ERROR: no stars or star list provided")
        else:
            with open(os.path.join(self.params['infdir'], self.params['todo']), "r") as f:
                self.params['stars'] = [line.strip().split()[0] for line in f.readlines()]


    def get_groups(self, n_threads=0,):
        """
        Get star groups
    
        Mostly relevant for parallel processing -- which sets up star groups to run 
        in parallel based on the number of threads


        """
        if hasattr(self, 'mode') and self.params['mode'] == 'parallel':
            todo = np.array(self.params['stars'])
            if self.params['n_threads'] == 0:
                self.params['n_threads'] = mp.cpu_count()
            if len(todo) < self.params['n_threads']:
                self.params['n_threads'] = len(todo)
            # divide stars into groups set by number of cpus/nthreads available
            digitized = np.digitize(np.arange(len(todo)) % self.params['n_threads'], np.arange(self.params['n_threads']))
            self.params['groups'] = np.array([todo[digitized == i] for i in range(1, self.params['n_threads']+1)], dtype=object)
        else:
            self.params['groups'] = np.array(self.params['stars'])


    def add_info(self):
        """
        Add info

        Checks and saves all default information for stars separately


        """
        self.get_info()
        for star in self.params['stars']:
            if self.params[star]['numax'] is not None:
                self.params[star]['excess'] = False
                if self.params[star]['dnu'] is not None:
                    self.params[star]['force'] = self.params[star]['dnu']
                self.params[star]['dnu'] = delta_nu(self.params[star]['numax'])
            else:
                if 'rs' in self.params[star] and self.params[star]['rs'] is not None and \
                  'logg' in self.params[star] and self.params[star]['logg'] is not None:
                    self.params[star]['ms'] = ((((self.params[star]['rs']*self.constants['r_sun'])**(2.0))*10**(self.params[star]['logg'])/self.constants['G'])/self.constants['m_sun'])
                    self.params[star]['numax'] = self.constants['numax_sun']*self.params[star]['ms']*(self.params[star]['rs']**(-2.0))*((self.params[star]['teff']/self.constants['teff_sun'])**(-0.5))
                    self.params[star]['dnu'] = self.constants['dnu_sun']*(self.params[star]['ms']**(0.5))*(self.params[star]['rs']**(-1.5))  
            if self.params[star]['lower_ech'] is not None and self.params[star]['upper_ech'] is not None:
                self.params[star]['ech_mask'] = [self.params[star]['lower_ech'], self.params[star]['upper_ech']]
            else:
                self.params[star]['ech_mask'] = None
            self.adjust_parameters(star)


    def get_info(self):
        """
        Load star info
    
        Reads in any star information provided in the csv -- columns MUST match the exact
        formats provided 

        .. todo:: if unsure, can (re)set up this file with a simple command


        """
        columns = get_dict(type='columns')
        # Create all keys first
        for star in self.params['stars']:
            for column in columns['all']:
                self.params[star][column] = None

        # Open csv file if it exists
        if os.path.exists(os.path.join(self.params['infdir'], self.params['info'])):
            df = pd.read_csv(os.path.join(self.params['infdir'], self.params['info']))
            stars = [str(each) for each in df.stars.values.tolist()]
            for star in self.params['stars']:
                if str(star) in stars:
                    idx = stars.index(str(star))
                    # Update information from columns
                    for column in df.columns.values.tolist():
                        if column in columns['int'] and not np.isnan(float(df.loc[idx,column])):
                            self.params[star][column] = int(df.loc[idx,column])
                        elif column in columns['float'] and not np.isnan(float(df.loc[idx,column])):
                            self.params[star][column] = float(df.loc[idx,column])
                        elif column in columns['bool']:
                            self.params[star][column] = df.loc[idx,column]
                        elif column in columns['str']:
                            self.params[star][column] = str(df.loc[idx,column])
                        else:
                            pass

        # Copy the rest of the defaults
        for star in self.params['stars']:
            for param in self.params:
                if param not in self.params[star]:
                    self.params[star][param] = self.params[param]
                elif param in self.params[star] and self.params[star][param] is None:
                    self.params[star][param] = self.params[param]
                else:
                    pass

        if not self.params['cli']:
            return
        # CLI will override anything from before
        for column in get_dict(type='columns')['override']:
            if self.override[column] is not None:
                for i, star in enumerate(self.params['stars']):
                    self.params[star][column] = self.override[column][i]


    def add_cli(self, args):
        """

        Save any non-default parameters provided via command line
        this skips over the "override" columns since those are star
        specific and we haven't saved any of the star information yet

        Parameters
            args : argparse.Namespace
                the command line arguments


        """
        if args.cli:
            self.check_cli(args)
            # CLI options overwrite defaults
            for key, value in args.__dict__.items():
                # Make sure it is not a variable with a >1 length
                if key not in self.override:
                    self.params[key] = value
            # were stars provided
            if self.params['stars'] is None:
                self.star_list()
        else:
            self.params['stars'] = args.stars


    def check_cli(self, args, max_laws=3):
        """ 
    
        Make sure that any command-line inputs are the proper lengths, types, etc.

        Parameters
            args : argparse.Namespace
                the command line arguments
            max_laws : int
                maximum number of resolvable Harvey components

        """
        self.override = {
            'numax': args.numax,
            'dnu': args.dnu,
            'lower_ex': args.lower_ex,
            'upper_ex': args.upper_ex,
            'lower_bg': args.lower_bg,
            'upper_bg': args.upper_bg,
            'lower_ps': args.lower_ps,
            'upper_ps': args.upper_ps,
            'lower_ech': args.lower_ech,
            'upper_ech': args.upper_ech,
        }
        for each in self.override:
            if self.override[each] is not None:
                assert len(args.stars) == len(self.override[each]), "The number of values provided for %s does not equal the number of stars"%each
        if args.oversampling_factor is not None:
            assert isinstance(args.oversampling_factor, int), "The oversampling factor for the input PS must be an integer"
        if args.n_laws is not None:
            assert args.n_laws <= max_laws, "We likely cannot resolve %d Harvey-like components for point sources. Please select a smaller number."%args.n_laws


    def adjust_parameters(self, star, adjust=True, defaults=None,):
        """ 
    
        Adjusts default parameters for low vs high numax configurations

        Parameters
            star : str
                individual star ID
            adjust : bool, optional
                maximum number of resolvable Harvey components
            defaults : str, optional
                option for when numax is not known but can differentiate between "low" vs. "high" frequencies

        """
        self.params[star]['boxes'] = np.logspace(np.log10(0.5), np.log10(500.), self.params['n_trials'])
        self.params[star]['smooth_width'], self.params[star]['ind_width'] = 10., 10.
        self.params[star]['lower_ex'], self.params[star]['lower_bg'] = 1., 1.
        self.params[star]['upper_ex'], self.params[star]['upper_bg'] = 8000., 8000.
        self.params[star]['smooth_ps'] = 1.5
        if self.params[star]['adjust'] and self.params[star]['numax'] is not None:
            if (self.params[star]['numax'] is not None and self.params[star]['numax'] < 500.) or \
              (self.params[star]['defaults'] is not None and self.params[star]['defaults'] == 'low'):
                self.params[star]['boxes'] = np.logspace(np.log10(0.5), np.log10(25.), self.params['n_trials'])
                self.params[star]['smooth_width'] = 5.
                self.params[star]['ind_width'] = 5.
                self.params[star]['smooth_ps'] = 1.0
                self.params[star]['lower_ex'], self.params[star]['lower_bg'] = 1., 1.
                self.params[star]['upper_ex'], self.params[star]['upper_bg'] = 1000., 1000.
            elif (self.params[star]['numax'] is not None and self.params[star]['numax'] >= 500.) or \
              (self.params[star]['defaults'] is not None and self.params[star]['defaults'] == 'high'):
                self.params[star]['boxes'] = np.logspace(np.log10(50.), np.log10(500.), self.params['n_trials'])
                self.params[star]['smooth_width'] = 20.
                self.params[star]['ind_width'] = 20.
                self.params[star]['smooth_ps'] = 2.5
                self.params[star]['lower_ex'], self.params[star]['lower_bg'] = 100., 100.
                self.params[star]['upper_ex'], self.params[star]['upper_bg'] = 8000., 8000.
            else:
                pass


def get_dict(type='params'):
    """
    Read dictionary
    
    Quick utility function to read in longer python dictionaries, which is primarily used in
    the utils script (i.e. verbose_output, scrape_output) and in the pipeline script 
    (i.e. setup)

    Parameters
        type : str
            which dictionary to read in - *MUST* match dict files - choices ~['params','columns','functions']

    Returns
        result : Dict[str,Dict[,]]
            the loaded, relevant dictionary

    .. important:: 
       `'functions'` must be saved within the script, since it points to modules loaded in from
       another file 

    """
    if type == 'functions':
        return {
                0: lambda white_noise : (lambda frequency : models._harvey_none(frequency, white_noise)),
                1: lambda frequency, white_noise : models._harvey_none(frequency, white_noise), 
                2: lambda white_noise : (lambda frequency, tau_1, sigma_1 : models._harvey_one(frequency, tau_1, sigma_1, white_noise)), 
                3: lambda frequency, tau_1, sigma_1, white_noise : models._harvey_one(frequency, tau_1, sigma_1, white_noise), 
                4: lambda white_noise : (lambda frequency, tau_1, sigma_1, tau_2, sigma_2 : models._harvey_two(frequency, tau_1, sigma_1, tau_2, sigma_2, white_noise)), 
                5: lambda frequency, tau_1, sigma_1, tau_2, sigma_2, white_noise : models._harvey_two(frequency, tau_1, sigma_1, tau_2, sigma_2, white_noise),
                6: lambda white_noise : (lambda frequency, tau_1, sigma_1, tau_2, sigma_2, tau_3, sigma_3 : models._harvey_three(frequency, tau_1, sigma_1, tau_2, sigma_2, tau_3, sigma_3, white_noise)),
                7: lambda frequency, tau_1, sigma_1, tau_2, sigma_2, tau_3, sigma_3, white_noise : models._harvey_three(frequency, tau_1, sigma_1, tau_2, sigma_2, tau_3, sigma_3, white_noise),
               }
    path = os.path.join(os.path.dirname(__file__), 'dicts', '%s.dict'%type)
    with open(path, 'r') as f:
        return ast.literal_eval(f.read())


def save_file(x, y, path, overwrite=False, formats=[">15.8f", ">18.10e"]):
    """
    Saves background-subtracted power spectrum
    
    After determining the best-fit stellar background model, this module
    saved the background-subtracted power spectrum

    Parameters
        x : numpy.ndarray
            the independent variable i.e. the time or frequency array 
        y : numpy.ndarray
            the dependent variable, in this case either the flux or power array
        path : str
            absolute path to save file to
        overwrite : bool, optional
            whether to overwrite existing files or not
        formats : List[str]
            2x1 list of formats to save arrays as


    """
    if os.path.exists(path) and not overwrite:
        path = get_next(path)
    with open(path, "w") as f:
        for xx, yy in zip(x, y):
            values = [xx, yy]
            text = '{:{}}'*len(values) + '\n'
            fmt = sum(zip(values, formats), ())
            f.write(text.format(*fmt))


def get_next(path, count=1):
    """
    Get next integer
    
    When the overwriting of files is disabled, this module determines what
    the last saved file was 

    Parameters
        path : str
            absolute path to file name that already exists
        count : int
            starting count, which is incremented by 1 until a new path is determined

    Returns
        new_path : str
            unused path name


    """
    path, fname = os.path.split(path)[0], os.path.split(path)[-1]
    new_fname = '%s_%d.%s'%(fname.split('.')[0], count, fname.split('.')[-1])
    new_path = os.path.join(path, new_fname)
    if os.path.exists(new_path):
        while os.path.exists(new_path):
            count += 1
            new_fname = '%s_%d.%s'%(fname.split('.')[0], count, fname.split('.')[-1])
            new_path = os.path.join(path, new_fname)
    return new_path


def save_estimates(star, variables=['star', 'numax', 'dnu', 'snr']):
    """
    
    Saves the parameter estimates (i.e. results from first module)

    Parameters
        star : pysyd.target.Target
            processed pipeline target
        variables : List[str]
            list of estimated variables to save (e.g., :math:`\\rm \\nu_{max}`, :math:`\\Delta\\nu`)

    Returns
        star : pysyd.target.Target
            updated pipeline target

    """
    if 'best' in star.params:
        best = star.params['best']
        results = [star.name, star.params['results']['estimates'][best]['numax'], star.params['results']['estimates'][best]['dnu'], star.params['results']['estimates'][best]['snr']]
        save_path = os.path.join(star.params['path'], 'estimates.csv')
        if not star.params['overwrite']:
            save_path = get_next(save_path)
        ascii.write(np.array(results), save_path, names=variables, delimiter=',', overwrite=True)
    star = save_plotting(star)
    return star


def save_plotting(star):
    """
    
    Saves all the relevant information for plotting (from the first iteration) so that it can 
    be done at the end now, as opposed to interrupting the workflow like it did before

    Parameters
        star : pysyd.target.Target
            processed pipeline target
        star.params['plotting'] : Dict[str,Dict[str,...]]
            constructs parameter plotting dictionary using the star instance
    Returns
        star : pysyd.target.Target
            updated pipeline target

    """

    if star.module == 'estimates':
        params = dict(
            time = np.copy(star.time),
            flux = np.copy(star.flux),
            freq = np.copy(star.freq),
            pow = np.copy(star.pow),
            bin_freq = np.copy(star.bin_freq),
            bin_pow = np.copy(star.bin_pow),
            interp_pow = np.copy(star.interp_pow),
            bgcorr_pow = np.copy(star.bgcorr_pow),
            )
    elif star.module == 'parameters':
        params = dict(
            time = np.copy(star.time),
            flux = np.copy(star.flux),
            frequency = np.copy(star.frequency),
            random_pow = np.copy(star.random_pow),
            smooth_pow = np.copy(star.smooth_pow),
            pssm = np.copy(star.pssm),
            bgcorr_smooth = np.copy(star.bgcorr_smooth),
            bin_freq = np.copy(star.bin_freq),
            bin_pow = np.copy(star.bin_pow),
            bin_err = np.copy(star.bin_err),
            region_freq = np.copy(star.region_freq),
            region_pow = np.copy(star.region_pow),
            lag = np.copy(star.lag),
            auto = np.copy(star.auto),
            zoom_lag = np.copy(star.zoom_lag),
            zoom_auto = np.copy(star.zoom_auto),
            peaks_l = np.copy(star.peaks_l),
            peaks_a = np.copy(star.peaks_a),
            best_lag = star.params['best_lag'],
            best_auto = star.params['best_auto'],
            obs_acf = max(star.params['plotting'][star.module]['dnu_fit']),
            z = np.copy(star.z),
            extent = np.copy(star.extent),
            xax = np.copy(star.xax),
            yax = np.copy(star.yax),
            a_orig = np.copy(star.params['a']),
            obs_numax = star.params['obs_numax'],
            exp_dnu = star.params['exp_dnu'],
            noise = star.params['noise'],
            pars = star.params['pars'],
            models = star.params['models'],
            paras = star.params['paras'],
            model = star.params['selected'],
            aic = star.params['aic'],
            bic = star.params['bic'],
            )
    else:
        pass
    star.params['plotting'][star.module].update(params)
    return star



def save_parameters(star, results={}, cols=['parameter', 'value', 'uncertainty']):
    """
    
    Saves the derived global parameters 

    Parameters
        star : pysyd.target.Target
            pipeline target with the results of the global fit
        results : Dict[str,float]
            parameter estimates from the pipeline
        cols : List[str]
            columns used to construct a pandas dataframe

    """
    results = star.params['results']['parameters']
    df = pd.DataFrame(results)
    star.df = df.copy()
    new_df = pd.DataFrame(columns=cols)
    for c, col in enumerate(df.columns.values.tolist()):
        new_df.loc[c, 'parameter'] = col
        new_df.loc[c, 'value'] = df.loc[0,col]
        if star.params['mc_iter'] > 1:
            new_df.loc[c, 'uncertainty'] = mad_std(df[col].values)
        else:
            new_df.loc[c, 'uncertainty'] = '--'
    save_path = os.path.join(star.params['path'], 'global.csv')
    if not star.params['overwrite']:
        save_path = get_next(save_path)
    new_df.to_csv(save_path, index=False)
    if star.params['samples']:
        save_path = os.path.join(star.params['path'], 'samples.csv')
        if not star.params['overwrite']:
            save_path = get_next(save_path)
        df.to_csv(save_path, index=False)
    if star.params['mc_iter'] > 1:
        star.params['plotting']['samples'] = {'df':star.df.copy()}


def verbose_output(star, note=''):
    """

    Prints verbose output from the global fit 


    """
    params = get_dict()
    if not star.params['overwrite']:
        list_of_files = glob.glob(os.path.join(star.params['path'], 'global*'))
        file = max(list_of_files, key=os.path.getctime)
    else:
        file = os.path.join(star.params['path'], 'global.csv')
    df = pd.read_csv(file)
    note += '-----------------------------------------------------------\nOutput parameters\n-----------------------------------------------------------'
    if star.params['mc_iter'] > 1:
        line = '\n%s: %.2f +/- %.2f %s'
        for idx in df.index.values.tolist():
            note += line%(df.loc[idx,'parameter'], df.loc[idx,'value'], df.loc[idx,'uncertainty'], params[df.loc[idx,'parameter']]['unit'])
    else:
        line = '\n%s: %.2f %s'
        for idx in df.index.values.tolist():
            note += line%(df.loc[idx,'parameter'], df.loc[idx,'value'], params[df.loc[idx,'parameter']]['unit'])
    note+='\n-----------------------------------------------------------'
    print(note)


def scrape_output(args):
    """
    Concatenate results
    
    Takes results for each processed target and concatenates the results into a single csv 
    for each submodule -- this is done automatically
    

    """
    # Estimate outputs
    if glob.glob(os.path.join(args.params['outdir'],'**','estimates*csv')):
        df = pd.DataFrame(columns=['star','numax','dnu','snr'])
        files_estimates = glob.glob(os.path.join(args.params['outdir'],'**','estimates*csv'))
        # get which stars have this output
        dirs = list(set([os.path.split(os.path.split(file)[0])[-1] for file in files_estimates]))
        # iterate through stars
        for dir in dirs:
            list_of_files = glob.glob(os.path.join(args.params['outdir'],dir,'estimates*csv'))
            file = max(list_of_files, key=os.path.getctime)
            df_new = pd.read_csv(file)
            df = pd.concat([df, df_new])
        df = sort_table(df)
        df.to_csv(os.path.join(args.params['outdir'],'estimates.csv'), index=False)

    # Parameter outputs
    if glob.glob(os.path.join(args.params['outdir'],'**','global*csv')):
        df = pd.DataFrame(columns=['star'])
        files_globals = glob.glob(os.path.join(args.params['outdir'],'**','global*csv'))
        dirs = list(set([os.path.split(os.path.split(file)[0])[-1] for file in files_globals]))
        for dir in dirs:
            list_of_files = glob.glob(os.path.join(args.params['outdir'],dir,'global*csv'))
            file = max(list_of_files, key=os.path.getctime)
            df_temp = pd.read_csv(file)
            columns = ['star'] + df_temp['parameter'].values.tolist()
            values = [dir] + df_temp['value'].values.tolist()
            if df_temp['uncertainty'].values.tolist()[0] != '--':
                columns += ['%s_err'%col for col in df_temp['parameter'].values.tolist()]
                values += df_temp['uncertainty'].values.tolist()
            # adjust format to be like the final csv
            df_new = pd.DataFrame(columns=columns)
            df_new.loc[0] = np.array(values)
            length = len(df)
            # makes sure all columns are in final csv
            for column in df_new.columns.values.tolist():
                if column not in df.columns.values.tolist():
                    df[column] = np.nan
                # copy value
                df.loc[length,column] = df_new.loc[0,column]
        df = sort_table(df)
        df.to_csv(os.path.join(args.params['outdir'],'global.csv'), index=False)


def sort_table(df, one=[], two=[],):
    df.set_index('star', inplace=True, drop=True)
    for star in df.index.values.tolist():
        alpha, numeric = 0, 0
        for char in str(star):
            if not char.isalpha():
                numeric += 1
            else:
                alpha += 1
        if alpha == 0:
            one.append(star)
        else:
            two.append(star)
    # sort integers
    one = [str(sort) for sort in sorted([int(each) for each in one])]
    final = one + sorted(two)
    df = df.reindex(final, copy=True)
    df.reset_index(drop=False, inplace=True)
    return df


def max_elements(x, y, npeaks, exp_dnu=None):
    """
    Return n max elements
    
    Module to obtain the x and y values for the n highest peaks in a power
    spectrum (or any 2D arrays really) 

    Parameters
        x : numpy.ndarray
            the x values of the data
        y : numpy.ndarray
            the y values of the data
        npeaks : int
            the first n peaks
        exp_dnu : float
            if not `None`, multiplies y array by Gaussian weighting centered on `exp_dnu`

    Returns
        peaks_x : numpy.ndarray
            the x coordinates of the first `npeaks`
        peaks_y : numpy.ndarray
            the y coordinates of the first `npeaks`


    """
    xc, yc = np.copy(x), np.copy(y)
    weights = np.ones_like(yc)
    if exp_dnu is not None:
        sig = 0.35*exp_dnu/2.35482 
        weights *= np.exp(-(xc-exp_dnu)**2./(2.*sig**2))*((sig*np.sqrt(2.*np.pi))**-1.)
    yc *= weights
    s = np.argsort(yc)
    peaks_y = y[s][-int(npeaks):][::-1]
    peaks_x = x[s][-int(npeaks):][::-1]

    return peaks_x, peaks_y


def return_max(x, y, exp_dnu=None, index=False, idx=None):
    """
    
    Return the either the value of peak or the index of the peak corresponding to the most likely dnu given a prior estimate,
    otherwise just the maximum value.

    Parameters
        x : numpy.ndarray
            the independent axis (i.e. time, frequency)
        y : numpy.ndarray
            the dependent axis
        index : bool
            if true will return the index of the peak instead otherwise it will return the value. Default value is `False`.
        dnu : bool
            if true will choose the peak closest to the expected dnu `exp_dnu`. Default value is `False`.
        exp_dnu : Required[float]
            the expected dnu. Default value is `None`.

    Returns
        result : Union[int, float]
            if `index` is `True`, result will be the index of the peak otherwise if `index` is `False` it will 
	        instead return the value of the peak

    """

    lst = list(y)
    if lst != []:
        if exp_dnu is not None:
            lst = list(np.absolute(x-exp_dnu))
            idx = lst.index(min(lst))
        else:
            idx = lst.index(max(lst))
    if index:
        return idx
    else:
        if idx is None:
            return [], []
        return x[idx], y[idx]


def bin_data(x, y, width, log=False, mode='mean'):
    """
    
    Bins data

    Parameters
        x : numpy.ndarray
            the x values of the data
        y : numpy.ndarray
            the y values of the data
        width : float
            bin width in muHz
        log : bool
            creates bins by using the log of the min/max values (i.e. not equally spaced in log if `True`)

    Returns
        bin_x : numpy.ndarray
            binned frequencies
        bin_y : numpy.ndarray
            binned power
        bin_yerr : numpy.ndarray
            standard deviation of the binned y data


    """
    if log:
        mi = np.log10(min(x))
        ma = np.log10(max(x))
        no = np.int(np.ceil((ma-mi)/width))
        bins = np.logspace(mi, mi+(no+1)*width, no)
    else:
        bins = np.arange(min(x), max(x)+width, width)

    digitized = np.digitize(x, bins)
    if mode == 'mean':
        bin_x = np.array([x[digitized == i].mean() for i in range(1, len(bins)) if len(x[digitized == i]) > 0])
        bin_y = np.array([y[digitized == i].mean() for i in range(1, len(bins)) if len(x[digitized == i]) > 0])
    elif mode == 'median':
        bin_x = np.array([np.median(x[digitized == i]) for i in range(1, len(bins)) if len(x[digitized == i]) > 0])
        bin_y = np.array([np.median(y[digitized == i]) for i in range(1, len(bins)) if len(x[digitized == i]) > 0])
    else:
        pass
    bin_yerr = np.array([y[digitized == i].std()/np.sqrt(len(y[digitized == i])) for i in range(1, len(bins)) if len(x[digitized == i]) > 0])

    return bin_x, bin_y, bin_yerr


def ask_int(question, n_trials, max_attempts=10, count=1, special=False):    
    """
    
    Asks for an integer user input -- this is specially formatted for the
    estimating module by requiring an integer number that corresponds to one
    of the (n_)trials or zero to provide :math:`\\rm \\nu_{max}` directly

    Parameters
        question : str
            the statement and/or question that needs to be answered
        range : List[float]
            if not `None`, provides a lower and/or upper bound for the selected integer
        max_attempts : int
            the maximum number of tries a user has before breaking
        count : int
            the user attempt number

    Returns
        result : int
            the user's integer answer or `None` if the number of attempts exceeds the allowed number


    """
    print()
    while count < max_attempts:
        answer = input(question)
        try:
            if special:
                try:
                    value = float(answer)
                except ValueError:
                    print('ERROR: please try again ')
                else:
                    return value
            elif float(answer).is_integer() and not special:
                if int(answer) == 0:
                    special = True
                    question = '\nWhat is your value for numax? '
                elif int(answer) >= 1 and int(answer) <= n_trials:
                    return int(answer)
                else:
                    print('ERROR: please select an integer between 1 and %d \n       (or 0 to provide your own value for numax)\n'%n_trials)
            else:
                print("ERROR: the selection must match one of the integer values \n")
        except ValueError:
            print("ERROR: not a valid response \n")
        count += 1
    return None


def get_results(file_idlsyd=SYDFILE, file_pysyd=PYSYDFILE, suffixes=['_idl', '_py'], max_numax=3200.,):
    """

    Load and compare results between `SYD` and `pySYD` pipelines

    Parameters
        file_idlsyd : str
            path to ``SYD`` ensemble results
        file_pysyd : str
            path to ``pySYD`` ensemble results
        suffixes : List[str]
            extensions to use when merging the two pipeline results
        max_numax : float, optional
            maximum values to use for numax comparison

    Returns
        df : pandas.DataFrame
            pandas dataframe with merged results

    """
    # load in both pipeline results
    idlsyd = pd.read_csv(file_idlsyd, skiprows=20, delimiter='|', names=get_dict('columns')['syd'])
    pysyd = pd.read_csv(file_pysyd)
    # make sure they can crossmatch
    idlsyd.KIC = idlsyd.KIC.astype(str)
    pysyd.star = pysyd.star.astype(str)
    # merge measurements from syd & pySYD catalogs
    df = pd.merge(idlsyd, pysyd, left_on='KIC', right_on='star', how='inner', suffixes=suffixes)
    df = df[df['numax_smooth'] <= max_numax]
    return df


def delta_nu(numax):
    """
    
    Estimates the large frequency separation using the numax scaling relation (add citation)

    Parameters
        numax : float
            the frequency corresponding to maximum power or numax

    Returns
        dnu : float
            the approximated frequency spacing, dnu

    """

    return 0.22*(numax**0.797)


def save_status(file, section, params):
    """

    Save pipeline status

    Parameters
        file : str 
            name of output config file
        section : str
            name of section in config file
        params : Dict() 
            dictionary of all options to populate in the specified section


    """
    import configparser
    config = configparser.ConfigParser()

    if os.path.isfile(file):
        config.read(file)

    if not config.has_section(section):
        config.add_section(section)

    for key, val in params.items():
        config.set(section, key, val)

    with open(file, 'w') as f:
        config.write(f)


def load_status(file):
    """

    Load pipeline status

    Parameters
        file : str
            name of output config file

    Returns
        config : configparser.ConfigParser
            config file with pipeline status

    """

    config = configparser.ConfigParser()
    gl = config.read(file)

    return config