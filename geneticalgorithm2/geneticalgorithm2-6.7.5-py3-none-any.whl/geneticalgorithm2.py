'''

Copyright 2021 Demetry Pascal (forked from Ryan (Mohammad) Solgi)

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.

'''


from typing import Callable, List, Tuple, Optional, Dict, Any, Union, Sequence, Set

import collections
import warnings
import operator


import sys
import time
import random


import numpy as np
from func_timeout import func_timeout, FunctionTimedOut

from OppOpPopInit import init_population, SampleInitializers, OppositionOperators, set_seed

#region INTERNAL IMPORTS

from .classes import AlgorithmParams, Generation, MiddleCallbackData, GAResult

from .initializer import Population_initializer
from .plotting_tools import plot_pop_scores, plot_several_lines

from .utils import can_be_prob, is_numpy, union_to_matrix

#endregion




class geneticalgorithm2:
    
    '''
    Genetic Algorithm (Elitist version) for Python
    
    An implementation of elitist genetic algorithm for solving problems with
    continuous, integers, or mixed variables.
    
    repo path https://github.com/PasaOpasen/geneticalgorithm2
    '''
    
    default_params = AlgorithmParams()
    PROGRESS_BAR_LEN = 20

    @property
    def output_dict(self):
        warnings.warn(
            "'output_dict' is deprecated and will be removed at version 7 \n use 'result' instead"
        )
        return self.result

    @property
    def needs_mutation(self):
        return self.prob_mut > 0 or self.prob_mut_discrete > 0

    #region INIT

    def __init__(
        self,
        function: Callable[[np.ndarray], float],
        dimension: int,
        variable_type: Union[str, Sequence[str]] = 'bool',
        variable_boundaries: Optional[Union[np.ndarray, Sequence[Tuple[float, float]]]] = None,

        variable_type_mixed = None,

        function_timeout: float = 10,
        algorithm_parameters: Union[AlgorithmParams, Dict[str, Any]] = default_params
    ):
        '''
        @param function <Callable[[np.ndarray], float]> - the given objective function to be minimized
        NOTE: This implementation minimizes the given objective function.
        (For maximization multiply function by a negative sign: the absolute
        value of the output would be the actual objective function)

        @param dimension <integer> - the number of decision variables

        @param variable_type <string> - 'bool' if all variables are Boolean;
        'int' if all variables are integer; and 'real' if all variables are
        real value or continuous. For mixed types use sequence of string of type for each variable

        @param variable_boundaries <Optional[Union[np.ndarray, Sequence[Tuple[float, float]]]]> - Default None; leave it
        None if variable_type is 'bool'; otherwise provide an array of tuples
        of length two as boundaries for each variable;
        the length of the array must be equal dimension. For example,
        np.array([0,100],[0,200]) determines lower boundary 0 and upper boundary 100 for first
        and upper boundary 200 for second variable where dimension is 2.

        @param variable_type_mixed -- deprecated

        @param function_timeout <float> - if the given function does not provide
        output before function_timeout (unit is seconds) the algorithm raise error.
        For example, when there is an infinite loop in the given function.

        @param algorithm_parameters <Union[AlgorithmParams, Dict[str, Any]]>:
            @ max_num_iteration <int> - stoping criteria of the genetic algorithm (GA)
            @ population_size <int>
            @ mutation_probability <float in [0,1]>
            @ elit_ratio <float in [0,1]>
            @ crossover_probability <float in [0,1]>
            @ parents_portion <float in [0,1]>
            @ crossover_type <string/function> - Default is 'uniform'; 'one_point' or 'two_point' (not only) are other options
            @ mutation_type <string/function> - Default is 'uniform_by_x'; see GitHub to check other options
            @ mutation_discrete_type <string/function> - mutation type for discrete variables
            @ selection_type <string/function> - Default is 'roulette'; see GitHub to check other options
            @ max_iteration_without_improv <int> - maximum number of successive iterations without improvement. If None it is ineffective


        for more details and examples of implementation please visit:
            https://github.com/PasaOpasen/geneticalgorithm2
  
        '''

        # input algorithm's parameters

        assert type(algorithm_parameters) in (dict, AlgorithmParams), "algorithm_parameters must be dict or AlgorithmParams object"
        if type(algorithm_parameters) != AlgorithmParams:
            algorithm_parameters = AlgorithmParams.from_dict(algorithm_parameters)

        algorithm_parameters._check_if_valid()
        self.crossover, self.real_mutation, self.discrete_mutation, self.selection = algorithm_parameters.get_CMS_funcs()

        self.param: AlgorithmParams = algorithm_parameters # if type(algorithm_parameters) == AlgorithmParams else AlgorithmParams.from_dict(algorithm_parameters)

        #############################################################
        # input function
        assert (callable(function)), "function must be callable!"
        self.f = function
        #Timeout
        self.funtimeout = float(function_timeout)

        #############################################################
        #dimension
        self.dim = int(dimension)
        assert self.dim > 0, f"dimension count must be int and >0, gotten {dimension}"

        if variable_type_mixed is not None:
            warnings.warn(
                f"argument variable_type_mixed is deprecated and will be removed at version 7\n use variable_type={tuple(variable_type_mixed)} instead"
            )
            variable_type = variable_type_mixed
        self.__set_types_indexes(variable_type)  # types indexes
        self.__set_var_boundaries(variable_type, variable_boundaries)  # input variables' boundaries

        
        ############################################################# 

        
        self.pop_s = int(self.param.population_size)
        self.__set_par_s(self.param.parents_portion)

        assert can_be_prob(self.param.mutation_probability)
        self.prob_mut = self.param.mutation_probability
        assert self.param.mutation_discrete_probability is None or can_be_prob(self.param.mutation_discrete_probability)
        self.prob_mut_discrete = self.param.mutation_discrete_probability or self.prob_mut

        self.prob_cross = self.param.crossover_probability

        self.__set_elit(self.pop_s, self.param.elit_ratio)
        assert(self.par_s >= self.num_elit), "\n number of parents must be greater than number of elits"

        self.__set_max_iterations()

        self._set_report()


    def __set_par_s(self, parents_portion: float):

        self.par_s = int(parents_portion*self.pop_s)
        assert self.par_s <= self.pop_s, f'parents count {self.par_s} cannot be less than population size {self.pop_s}'
        trl= self.pop_s - self.par_s
        if trl % 2 != 0:
            self.par_s += 1

    def __set_elit(self, pop_size: int, elit_ratio: float):
        trl = pop_size*elit_ratio
        if trl < 1 and elit_ratio > 0:
            self.num_elit = 1
        else:
            self.num_elit = int(trl)

    def __set_types_indexes(self, variable_type: Union[str, Sequence[str]]):

        indexes = np.arange(self.dim)
        self.indexes_int = np.array([])
        self.indexes_float = np.array([])

        VALID_STRINGS = ( 'bool', 'int', 'real')
        assert_message = f"\n variable_type must be 'bool', 'int', 'real' or a sequence with 'int' and 'real', got {variable_type}"

        if type(variable_type) == str:
            assert (variable_type in VALID_STRINGS), assert_message
            if variable_type == 'real':
                self.indexes_float = indexes
            else:
                self.indexes_int = indexes

        else:  # sequence case

            assert (len(variable_type) == self.dim), f"\n variable_type must have a length equal dimension. Should be {self.dim}, got {len(variable_type)}"
            assert 'bool' not in variable_type, "don't use 'bool' if variable_type is a sequence, for 'boolean' case use 'int' and specify boundary as (0,1)"
            assert all(v in VALID_STRINGS for v in variable_type), assert_message

            vartypes = np.array(variable_type)
            self.indexes_int = indexes[vartypes == 'int']
            self.indexes_float = indexes[vartypes == 'real']

    def __set_var_boundaries(
        self,
        variable_type: Union[str, Sequence[str]],
        variable_boundaries
    ):
        if variable_type == 'bool':
            self.var_bound = np.array([[0, 1]] * self.dim)
        else:

            if is_numpy(variable_boundaries):
                assert variable_boundaries.shape == (self.dim, 2), f"\n if variable_boundaries is numpy array, it must be with shape (dim, 2)"
            else:
                assert len(variable_boundaries) == self.dim and all((len(t) == 2 for t in variable_boundaries)), "\n if variable_boundaries is sequence, it must be with len dim and boundary for each variable must be a tuple of length two"

            for i in variable_boundaries:
                assert(i[0] <= i[1]), "\n lower_boundaries must be smaller than upper_boundaries [lower,upper]"

            self.var_bound = np.array(variable_boundaries)


    def __set_max_iterations(self):

        if self.param['max_num_iteration'] is None:
            iterate = 0
            for i in range(0, self.dim):
                if i in self.indexes_int:
                    iterate += (self.var_bound[i][1] - self.var_bound[i][0]) * self.dim * (100 / self.pop_s)
                else:
                    iterate += (self.var_bound[i][1] - self.var_bound[i][0]) * 50 * (100 / self.pop_s)
            iterate = int(iterate)
            if (iterate * self.pop_s) > 10000000:
                iterate = 10000000 / self.pop_s

            if iterate > 8000:
                iterate = 8000

            self.iterate = iterate

        else:
            self.iterate = int(self.param['max_num_iteration'])

        self.stop_mniwi = False  # is stopped cuz of no progress some iterations
        max_it = self.param['max_iteration_without_improv']
        if max_it is None:
            self.mniwi = self.iterate + 1
        else:
            self.mniwi = int(max_it)

    #endregion

    #region REPORT

    def _set_report(self):
        """
        creates default report checker
        """
        self.checked_reports = [
            # item 0 cuz scores will be sorted and min item is items[0]
            ('report', operator.itemgetter(0))
        ]

    def _clear_report(self):
        """
        removes all report objects
        """
        for attr in vars(self).keys():
            if attr.startswith('report'):
                delattr(self, attr)

    def _init_report(self):
        """
        makes empty report fields
        """
        for name, _ in self.checked_reports:
            setattr(self, name, [])

    def _update_report(self, scores: np.ndarray):
        """
        append report value to the end of field
        """
        for name, func in self.checked_reports:
            getattr(self, name).append(
                func(scores)
            )

    #endregion

    #region RUN METHODS

    def __progress(self, count: int, total: int, status: str = ''):

        part = count / total

        filled_len = round(geneticalgorithm2.PROGRESS_BAR_LEN * part)
        percents = round(100.0 * part, 1)
        bar = '|' * filled_len + '_' * (geneticalgorithm2.PROGRESS_BAR_LEN - filled_len)

        sys.stdout.write('\r%s %s%s %s' % (bar, percents, '%', status))
        sys.stdout.flush()

    def __str__(self):
        return f"Genetic algorithm object with parameters {self.param}"

    def __repr__(self):
        return self.__str__()

    def _simulate(self, sample: np.ndarray):

        obj = None
        eval_time = time.time()
        try:
            obj = func_timeout(
                self.funtimeout,
                lambda: self.f(sample)
            )
        except FunctionTimedOut:
            print("given function is not applicable")
        eval_time = time.time() - eval_time

        assert obj is not None, f"the given function was running like {eval_time} seconds and does not provide any output"

        tp = type(obj)
        assert (tp in (int, float) or np.issubdtype(tp, np.floating) or np.issubdtype(tp,
                                                                                      np.integer)), f"Minimized function should return a number, but got '{obj}' object with type {tp}"

        return obj, eval_time

    def __set_mutation_indexes(self, mutation_indexes):

        if mutation_indexes is not None:
            tmp_indexes = set(mutation_indexes)
            self.indexes_int_mut = np.array(list(set(self.indexes_int).intersection(tmp_indexes)))
            self.indexes_float_mut = np.array(list(set(self.indexes_float).intersection(tmp_indexes)))

            if self.indexes_float_mut.size == 0 and self.indexes_int_mut.size == 0:
                warnings.warn(f"No mutation dimensions!!! Check ur mutation indexes!!")

        else:
            self.indexes_float_mut = self.indexes_float
            self.indexes_int_mut = self.indexes_int


    def run(
        self,
        no_plot: bool = False,
        disable_progress_bar: bool = False,
        disable_printing: bool = False,

        set_function: Optional[Callable[[np.ndarray], np.ndarray]] = None,
        apply_function_to_parents: bool = False,
        start_generation: Union[str, Dict[str, np.ndarray], Generation, np.ndarray, Tuple[Optional[np.ndarray], Optional[np.ndarray]]] = Generation(),
        studEA: bool = False,
        mutation_indexes: Optional[Union[Sequence[int], Set[int]]] = None,

        init_creator: Optional[Callable[[], np.ndarray]] = None,
        init_oppositors: Optional[Sequence[Callable[[np.ndarray], np.ndarray]]] = None,

        duplicates_oppositor: Optional[Callable[[np.ndarray], np.ndarray]] = None,
        remove_duplicates_generation_step: Optional[int] = None,

        revolution_oppositor: Optional[Callable[[np.ndarray], np.ndarray]] = None,
        revolution_after_stagnation_step: Optional[int] = None,
        revolution_part: float = 0.3,

        population_initializer: Tuple[int, Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]] = Population_initializer(select_best_of = 1, local_optimization_step = 'never', local_optimizer = None),

        stop_when_reached: Optional[float] = None,
        callbacks: Optional[Sequence[Callable[[int, List[float],  np.ndarray, np.ndarray], None]]] = None,
        middle_callbacks: Optional[Sequence] = None, #+
        time_limit_secs: Optional[float] = None,
        save_last_generation_as: Optional[str] = None,
        seed: Optional[int] = None
    ):
        """
        @param no_plot <boolean> - do not plot results using matplotlib by default
        
        @param disable_progress_bar <boolean> - do not show progress bar
                
        @param set_function : 2D-array -> 1D-array function, which applyes to matrix of population (size (samples, dimention))
        to estimate their values
        
        @param apply_function_to_parents <boolean> - apply function to parents from previous generation (if it's needed)
                                                                                                         
        @param start_generation <dictionary/str/Generation object> - Generation object or a dictionary with structure {'variables':2D-array of samples, 'scores': function values on samples} or path to .npz file (str) with saved generation
        if 'scores' value is None the scores will be compute

        @param studEA <boolean> - using stud EA strategy (crossover with best object always)
        
        @param mutation_indexes <Optional[Union[Sequence[int], Set[int]]]> - indexes of dimensions where mutation can be performed (all dimensions by default)

        @param init_creator: Optional[Callable[[], np.ndarray]], the function creates population samples. By default -- random uniform for real variables and random uniform for int
        @param init_oppositors: Optional[Sequence[Callable[[np.ndarray], np.ndarray]]]t, the list of oppositors creates oppositions for base population. No by default
        @param duplicates_oppositor: Optional[Callable[[np.ndarray], np.ndarray]], oppositor for applying after duplicates removing. By default -- using just random initializer from creator
        @param remove_duplicates_generation_step: None/int, step for removing duplicates (have a sense with discrete tasks). No by default
        @param revolution_oppositor = Optional[Callable[[np.ndarray], np.ndarray]], oppositor for revolution time. No by default
        @param revolution_after_stagnation_step = None/int, create revolution after this generations of stagnation. No by default
        @param revolution_part: float, the part of generation to being oppose. By default is 0.3

        @param population_initializer (Tuple[int, Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]]) - object for actions at population initialization step to create better start population. See doc

        @param stop_when_reached (None/float) - stop searching after reaching this value (it can be potential minimum or something else)

        @param callbacks (Optional[Sequence[Callable[[int, List[float],  np.ndarray, np.ndarray], None]]]) - sequence of callback functions with structure: (generation_number, report_list, last_population, last_scores) -> do some action

        @param middle_callbacks (Optional[Sequence]) - sequence of functions made MiddleCallbacks class

        @param time_limit_secs (Optional[float] / number>0) - limit time of working (in seconds)

        @param save_last_generation_as (Optional[str]) - path to .npz file for saving last_generation as numpy dictionary like {'population': 2D-array, 'scores': 1D-array}, None if doesn't need to save in file

        @param seed (None/int) - random seed (None if doesn't matter)
        """

        start_generation = Generation.from_object(self.dim, start_generation)

        is_current_gen_number = lambda number: (number is None) or (type(number) == int and number > 0)

        assert is_current_gen_number(revolution_after_stagnation_step), "must be None or int and >0"
        assert is_current_gen_number(remove_duplicates_generation_step), "must be None or int and >0"
        assert can_be_prob(revolution_part), f"revolution_part must be in [0,1], not {revolution_part}"
        assert (stop_when_reached is None or type(stop_when_reached) in (int, float))
        assert (isinstance(callbacks, collections.abc.Sequence) or callbacks is None), "callbacks should be list of callbacks functions"
        assert (isinstance(middle_callbacks, collections.abc.Sequence) or middle_callbacks is None), "middle_callbacks should be list of MiddleCallbacks functions"
        assert (time_limit_secs is None or time_limit_secs > 0), 'time_limit_secs must be None of number > 0'

        self.__set_mutation_indexes(mutation_indexes)
        set_seed(seed)

        show_progress = (lambda t, t2, s: self.__progress(t, t2, status=s)) if not disable_progress_bar else (lambda t, t2, s: None)

        # gets indexes of 2 parents to crossover
        get_parents_inds = (lambda par_count: (0, random.randrange(1, par_count))) if studEA else (lambda par_count: tuple(np.random.randint(0, par_count, 2)))
        
        stop_by_val = (lambda best_f: False) if stop_when_reached is None else (lambda best_f: best_f <= stop_when_reached)

        t = 0
        fails = 0
        pop: np.ndarray = None
        scores: np.ndarray = None

        def get_data():
            """
            returns all important data about model
            """
            return MiddleCallbackData(
                last_generation=Generation(pop, scores),
                current_generation=t,
                report_list=self.report,

                mutation_prob=self.prob_mut,
                mutation_discrete_prob=self.prob_mut_discrete,
                crossover_prob=self.prob_cross,
                mutation=self.real_mutation,
                mutation_discrete=self.discrete_mutation,
                crossover=self.crossover,
                selection=self.selection,

                current_stagnation=fails,
                max_stagnation=self.mniwi,

                parents_portion=self.param.parents_portion,
                elit_ratio=self.param.elit_ratio,

                set_function=self.set_function,

                reason_to_stop=reason_to_stop
            )

        def set_data(data: MiddleCallbackData):
            """
            sets data to model
            """
            nonlocal pop, scores, fails, reason_to_stop

            pop, scores = data.last_generation.variables, data.last_generation.scores
            self.pop_s = pop.shape[0]

            self.param.parents_portion = data.parents_portion
            self.__set_par_s(data.parents_portion)

            self.param.elit_ratio = data.elit_ratio
            self.__set_elit(self.pop_s, data.elit_ratio)

            self.prob_mut = data.mutation_prob
            self.prob_mut_discrete = data.mutation_discrete_prob
            self.prob_cross = data.crossover_prob
            self.real_mutation = data.mutation
            self.discrete_mutation = data.mutation_discrete
            self.crossover = data.crossover
            self.selection = data.selection

            fails = data.current_stagnation
            reason_to_stop = data.reason_to_stop
            self.mniwi = data.max_stagnation

            self.set_function = data.set_function

        if callbacks is None or len(callbacks) == 0:
            total_callback = lambda g, r, lp, ls: None
        else:
            def total_callback(generation_number, report_list, last_population, last_scores):
                for cb in callbacks:
                    cb(generation_number, report_list, last_population, last_scores)

        if middle_callbacks is None or len(middle_callbacks) == 0:
            total_middle_callback = lambda: None
        else:
            def total_middle_callback():
                """
                applies callbacks and sets new data if there is a sence
                """
                data = get_data()
                flag = False
                for cb in middle_callbacks:
                    data, has_sense = cb(data)
                    if has_sense:
                        flag = True
                if flag:
                    set_data(data)  # update global date if there was real callback step


        start_time = time.time()
        time_is_done = (lambda: False) if time_limit_secs is None else (lambda: int(time.time() - start_time) >= time_limit_secs)

        ############################################################# 
        # Initial Population
        
        self.set_function = set_function or geneticalgorithm2.default_set_function(self.f)

        pop_coef, initializer_func = population_initializer
        
        # population creator by random or with oppositions
        if init_creator is None:
            # just uniform random
            self.creator = SampleInitializers.Combined(
                minimums = self.var_bound[:, 0],
                maximums= self.var_bound[:, 1],
                indexes = (
                    self.indexes_int,
                    self.indexes_float
                ),
                creator_initializers = (
                    SampleInitializers.RandomInteger,
                    SampleInitializers.Uniform
                )
            )
        else:
            assert callable(init_creator)
            self.creator = init_creator

        self.init_oppositors = init_oppositors
        self.dup_oppositor = duplicates_oppositor
        self.revolution_oppositor = revolution_oppositor

        # event for removing duplicates
        if remove_duplicates_generation_step is None:
            def remover(pop: np.ndarray, scores: np.ndarray, gen: int) -> Tuple[
                np.ndarray,
                np.ndarray
            ]:
                return pop, scores
        else:
            
            def without_dup(pop: np.ndarray, scores: np.ndarray):  # returns population without dups
                _, index_of_dups = np.unique(pop, axis=0, return_index=True)
                return pop[index_of_dups], scores[index_of_dups], scores.size - index_of_dups.size
            
            if self.dup_oppositor is None:  # if there is no dup_oppositor, use random creator
                def remover(pop: np.ndarray, scores: np.ndarray, gen: int) -> Tuple[
                    np.ndarray,
                    np.ndarray
                ]:
                    if gen % remove_duplicates_generation_step != 0:
                        return pop, scores

                    pp, sc, count_to_create = without_dup(pop, scores)  # pop without dups
                    
                    if count_to_create == 0: 
                        show_progress(t, self.iterate,
                                      f"GA is running...{t} gen from {self.iterate}. No dups!")
                        return pop, scores

                    pp2 = SampleInitializers.CreateSamples(self.creator, count_to_create)  # new pop elements
                    pp2_scores = self.set_function(pp2)  # new elements values
                    
                    show_progress(t, self.iterate, f"GA is running...{t} gen from {self.iterate}. Kill dups!")
                    
                    new_pop = np.vstack((pp, pp2))
                    new_scores = np.concatenate((sc, pp2_scores))

                    args_to_sort = new_scores.argsort()
                    return new_pop[args_to_sort], new_scores[args_to_sort]

            else:  # using oppositors
                assert callable(self.dup_oppositor)

                def remover(pop: np.ndarray, scores: np.ndarray, gen: int) -> Tuple[
                    np.ndarray,
                    np.ndarray
                ]:
                    if gen % remove_duplicates_generation_step != 0:
                        return pop, scores

                    pp, sc, count_to_create = without_dup(pop, scores)  # pop without dups

                    if count_to_create == 0: 
                        show_progress(t, self.iterate, f"GA is running...{t} gen from {self.iterate}. No dups!")
                        return pop, scores

                    if count_to_create > sc.size:
                        raise Exception(f"Too many duplicates at generation {gen} ({count_to_create} > {sc.size}), cannot oppose")

                    # oppose count_to_create worse elements
                    pp2 = OppositionOperators.Reflect(pp[-count_to_create:], self.dup_oppositor)  # new pop elements
                    pp2_scores = self.set_function(pp2)  # new elements values

                    show_progress(t, self.iterate,
                                  f"GA is running...{t} gen from {self.iterate}. Kill dups!")

                    new_pop = np.vstack((pp, pp2))
                    new_scores = np.concatenate((sc, pp2_scores))

                    args_to_sort = new_scores.argsort()
                    return new_pop[args_to_sort], new_scores[args_to_sort]


        # event for revolution
        if revolution_after_stagnation_step is None:
            def revolution(pop: np.ndarray, scores: np.ndarray, stagnation_count: int) -> Tuple[
                np.ndarray,
                np.ndarray
            ]:
                return pop, scores
        else:
            if revolution_oppositor is None:
                raise Exception(
                    f"How can I make revolution each {revolution_after_stagnation_step} stagnation steps if revolution_oppositor is None (not defined)?"
                )
            assert callable(revolution_oppositor)
            
            def revolution(pop: np.ndarray, scores: np.ndarray, stagnation_count: int) -> Tuple[
                np.ndarray,
                np.ndarray
            ]:
                if stagnation_count < revolution_after_stagnation_step:
                    return pop, scores
                part = int(pop.shape[0]*revolution_part)
                
                pp2 = OppositionOperators.Reflect(pop[-part:], self.revolution_oppositor)
                pp2_scores = self.set_function(pp2)

                combined = np.vstack((pop, pp2))
                combined_scores = np.concatenate((scores, pp2_scores))
                args = combined_scores.argsort()
                
                show_progress(t, self.iterate, f"GA is running...{t} gen from {self.iterate}. Revolution!")

                args = args[:scores.size]
                return combined[args], combined_scores[args]

        #
        #
        #  START ALGORITHM LOGIC
        #
        #

        # Report
        self._clear_report()  # clear old report objects
        self._init_report()


        # initialization of pop
        
        if start_generation.variables is None:

            real_pop_size = self.pop_s*pop_coef

            # pop = np.empty((real_pop_size, self.dim))
            scores = np.empty(real_pop_size)
            
            pop = init_population(
                samples_count=real_pop_size,
                creator=self.creator,
                oppositors=self.init_oppositors
            )
            
            time_counter = 0

            for p in range(0, real_pop_size):
                # simulation returns exception or func value -- check the time of evaluating
                value, eval_time = self._simulate(pop[p])
                scores[p] = value
                time_counter += eval_time
            
            if not disable_printing:
                print(f"\n\r Average time of function evaluating (secs): {time_counter/real_pop_size}\n")
                
        else:

            self.pop_s = start_generation.variables.shape[0]
            self.__set_elit(self.pop_s, self.param.elit_ratio)
            self.__set_par_s(self.param.parents_portion)

            # pop = np.empty((self.pop_s, self.dim+1))
            pop = start_generation.variables
            scores = start_generation.scores if start_generation.scores is not None else self.set_function(pop)

        
        # Initialization by select bests and local_descent
        
        pop, scores = initializer_func(pop, scores)

        self.pop_s = scores.size
        self.best_function = scores.min()

        t = 1
        fails = 0  # iterations without progress
        reason_to_stop: Optional[str] = None

        #  while no reason to stop
        while True:

            args_to_sort = scores.argsort()
            pop = pop[args_to_sort]
            scores = scores[args_to_sort]
            self._update_report(scores)

            if fails > self.mniwi:
                reason_to_stop = f"limit of fails: {fails}"
            elif t == self.iterate:
                reason_to_stop = f'limit of iterations: {t}'
            elif stop_by_val(self.best_function):
                reason_to_stop = f"stop value reached: {self.best_function} <= {stop_when_reached}"
            elif time_is_done():
                reason_to_stop = f'time is done: {time.time() - start_time} >= {time_limit_secs}'

            if reason_to_stop is not None:
                show_progress(t, self.iterate, f"GA is running... STOP! {reason_to_stop}")
                break

            show_progress(t, self.iterate, f"GA is running...{t} gen from {self.iterate}")


            if scores[0] < self.best_function:  # if there is progress
                fails = 0
                self.best_function = scores[0]
                
                show_progress(t,
                              self.iterate,
                              f"GA is running...{t} gen from {self.iterate}...best value = {self.best_function}"
                              )
            else:
                fails += 1

            # Select parents
            
            par = np.empty((self.par_s, self.dim))
            par_scores = np.empty(self.par_s)
            
            # elit parents
            elit_slice = slice(None, self.num_elit)
            # copy needs because generation wil be removed after parents selection
            par[elit_slice] = pop[elit_slice].copy()
            par_scores[elit_slice] = scores[elit_slice].copy()
                
            # non-elit parents indexes
            new_par_inds = self.selection(scores, self.par_s - self.num_elit).astype(np.int16)
            par_slice = slice(self.num_elit, self.par_s)
            par[par_slice] = pop[new_par_inds].copy()
            par_scores[par_slice] = scores[new_par_inds].copy()

            #  select parents for crossover
            ef_par_list = np.random.random(self.par_s) < self.prob_cross
            par_count = ef_par_list.sum()
            if par_count < 2:
                while par_count < 2:  # 2 parents at least
                    ef_par_list = np.random.random(self.par_s) <= self.prob_cross
                    par_count = np.sum(ef_par_list)
                 
            ef_par = par[ef_par_list].copy()

            # New generation
            pop = np.empty((self.pop_s, self.dim))
            scores = np.empty(self.pop_s)

            parents_slice = slice(None, self.par_s)
            pop[parents_slice] = par[parents_slice]
            scores[parents_slice] = par_scores[parents_slice]
                
            for k in range(self.par_s, self.pop_s, 2):
                r1, r2 = get_parents_inds(par_count)
                pvar1 = ef_par[r1]
                pvar2 = ef_par[r2]
                
                ch1, ch2 = self.crossover(pvar1, pvar2)
                
                if self.needs_mutation:
                    ch1 = self.mut(ch1)
                    ch2 = self.mut_middle(ch2, pvar1, pvar2)               

                pop[k] = ch1
                pop[k+1] = ch2

            if apply_function_to_parents:
                scores = self.set_function(pop)
            else:
                scores[self.par_s:] = self.set_function(pop[self.par_s:])
            
            # remove duplicates
            pop, scores = remover(pop, scores, t)
            # revolution
            pop, scores = revolution(pop, scores, fails)

            total_callback(t, self.report, pop, scores)
            total_middle_callback()

            t += 1

        if scores[0] < self.best_function:
            self.best_function = scores[0]

        last_generation = Generation(pop, scores)
        self.result = GAResult(last_generation)

        if save_last_generation_as is not None:
            last_generation.save(save_last_generation_as)

        if not disable_printing:
            show = ' '*200
            sys.stdout.write(f'\r{show}\n')
            sys.stdout.write(f'\r The best found solution:\n {pop[0]}')
            sys.stdout.write(f'\n\n Objective function:\n {self.best_function}\n')
            sys.stdout.write(f'\n Used generations: {len(self.report)}')
            sys.stdout.write(f'\n Used time: {time.time() - start_time:.3g} seconds\n')
            sys.stdout.flush() 
        
        if not no_plot:
            self.plot_results()

        if not disable_printing:
            if reason_to_stop is not None and 'iterations' not in reason_to_stop:
                sys.stdout.write(
                    f'\nWarning: GA is terminated because of {reason_to_stop}'
                )

        return self.result

    #endregion

    #region PLOTTING

    def plot_results(
        self,
        title: str = 'Genetic Algorithm',
        save_as: Optional[str] = None,
        dpi: int = 200,
        main_color: str = 'blue'
     ):
        """
        Simple plot of self.report (if not empty)
        """
        if len(self.report) == 0:
            sys.stdout.write("No results to plot!\n")
            return

        plot_several_lines(
            lines=[self.report],
            colors=[main_color],
            labels=['best of generation'],
            linewidths=[2],
            title=title,
            xlabel='Generation',
            ylabel='Minimized function',
            save_as=save_as,
            dpi=dpi
        )

    def plot_generation_scores(self, title: str = 'Last generation scores', save_as: Optional[str] = None):
        """
        Plots barplot of scores of last population
        """

        if not hasattr(self, 'result'):
            raise Exception("There is no 'result' field into ga object! Before plotting generation u need to run seaching process")

        plot_pop_scores(self.result.last_generation.scores, title, save_as)

    #endregion

    #region MUTATION
    def mut(self, x: np.ndarray):
        """
        just mutation
        """

        for i in self.indexes_int_mut:
            if random.random() < self.prob_mut_discrete:
                bounds = self.var_bound[i]
                x[i] = self.discrete_mutation(x[i], bounds[0], bounds[1])

        for i in self.indexes_float_mut:                
            if random.random() < self.prob_mut:
                bounds = self.var_bound[i]
                x[i] = self.real_mutation(x[i], bounds[0], bounds[1])
            
        return x

    def mut_middle(self, x: np.ndarray, p1: np.ndarray, p2: np.ndarray):
        """
        mutation oriented on parents
        """
        for i in self.indexes_int_mut:

            if random.random() < self.prob_mut_discrete:
                v1, v2 = p1[i], p2[i]
                if v1 < v2:
                    x[i] = random.randint(v1, v2)
                elif v1 > v2:
                    x[i] = random.randint(v2, v1)
                else:
                    bounds = self.var_bound[i]
                    x[i] = random.randint(bounds[0], bounds[1])
                        
        for i in self.indexes_float_mut:                
            if random.random() < self.prob_mut:
                v1, v2 = p1[i], p2[i]
                if v1 != v2:
                    x[i] = random.uniform(v1, v2)
                else:
                    bounds = self.var_bound[i]
                    x[i] = random.uniform(bounds[0], bounds[1])
        return x

    #endregion


    #region Set functions

    @staticmethod
    def default_set_function(function_for_set: Callable[[np.ndarray], float]):
        """
        simple function for creating set_function 
        function_for_set just applyes to each row of population
        """
        def func(matrix: np.ndarray):
            return np.array([function_for_set(matrix[i]) for i in range(matrix.shape[0])])
        return func

    @staticmethod
    def set_function_multiprocess(function_for_set: Callable[[np.ndarray], float], n_jobs: int = -1):
        """
        like function_for_set but uses joblib with n_jobs (-1 goes to count of available processors)
        """
        from joblib import Parallel, delayed
        def func(matrix: np.ndarray):
            result = Parallel(n_jobs=n_jobs)(delayed(function_for_set)(matrix[i]) for i in range(matrix.shape[0]))
            return np.array(result)
        return func
            
    #endregion













            
            