# Name: Andrew Sevilla
# Student ID: s2010815T
# Code problems / unmet requirements: Display of the datasets file is incomplete. Ran out of time.. :(

# Analysis / Reflection of code explaining :- 
## 1) Design process: 
### a) How I came up with the program design : Again, it was an iterative process leveraging a technical session and reading through the spec multiple times to ensure everything was covered.
### b) How I started writing the code after the design process : I leveraged my previous assignment's code as a starting point, starting with reading in the file. I've kept some display_info functions which I've used in my testing as I want to continue with the next sections and feel it is worthwhile to keep it in there. I adapted some of the string printing formatting I had used in the last assignment to make life easier.
## 2) Challenges I met during code development : Formatting was a bit of a challenge this time around, as well as creating the list of objects within the list of objects and referencing them but it was easier this time around compared to the last assignment.

## I'm late and into the DI section and realised I should not have made the AlgorithmInfo and DatasetInfo classes and instead incorporated the data into them by adding optional variables with default values then setting the values with the datasets / algorithms files..  Grr... For now, I'll proceed and update it soon. Not sure that it'll be too much effort. We'll see.

# References: (Sources of info / websites / tools other than course contents directly under Canvas / Modules) : Nothing to reference, except Googling issues, so stack overflow, python docs and other Python blogs, etc. No code blocks were used / copied just troubleshooting assistance for my stupidity.

# Highest level attempted : DISTINCTION

import os
import sys

class Records:

    _space = ' '    

    # I added the variable _current_directory here to potentially later expand into specifying another directory and play around with it. I didn't have the time this time around but I feel there's value there.
    def __init__(self):
        self.__algorithm_list = []
        self.__dataset_info_list = []
        self.__datasets_count = 0
        self.__longest_algorithm_name = 0        
        self._current_directory = os.path.dirname(os.path.abspath(__file__))

    # I decided to split the lines in the file and take the length of the longest algorithm name dynamically in case one of you crazy testing cats decided to throw a curveball with a longer name (or even shorter names). As the request was to have this fully OO a list of objects and a subsequent nested list of objects for the datasets was used.
    def read_results(self, results_filename):

        filepath = os.path.join(self._current_directory, results_filename)
        with open(filepath, 'r') as file_name:
            line = file_name.readline()
            while line:
                filedata_field = line.strip().split(",")
                new_algorithm_instance = Algorithm(filedata_field[0].strip())
                if len(filedata_field[0].strip()) > self.__longest_algorithm_name:
                    self.__longest_algorithm_name = len(filedata_field[0].strip())
                new_algorithms_full_dataset = filedata_field[1:]
                self.__datasets_count = 0
                for dataset_list_pair in new_algorithms_full_dataset:
                    dataset_data = dataset_list_pair.strip().split(":")
                    new_dataset = Dataset(dataset_data[0].strip(), dataset_data[1].strip())
                    new_algorithm_instance.get_dataset_list.append([new_dataset])
                    self.__datasets_count += 1                    
                line = file_name.readline()
                self.__algorithm_list.append(new_algorithm_instance)
        file_name.close()

        return None


    def read_datasets(self, datasets_filename):
        filepath = os.path.join(self._current_directory, datasets_filename)
        with open(filepath, 'r') as file_name:
            line = file_name.readline()
            while line:
                filedata_field = line.strip().split(",")
                new_dataset_info_instance = DatasetInfo(filedata_field[0].strip(), filedata_field[1].strip(), filedata_field[2].strip(), filedata_field[3].strip(), filedata_field[4].strip())
                if int(filedata_field[2].strip()) > 5:
                    print(f'Dataset {filedata_field[0]} was found to contain the complexity weight {filedata_field[2].strip()} which is greater than the allowable limit of 5. Exiting.')
                    sys.exit()
                self.__dataset_info_list.append(new_dataset_info_instance)
                line = file_name.readline()                
        file_name.close()

        return None
    
    def read_algorithms(self, algorithms_filename):
        filepath = os.path.join(self._current_directory, algorithms_filename)
        with open(filepath, 'r') as file_name:
            line = file_name.readline()
            while line:
                filedata_field = line.strip().split(",")
                filedata_field[0].strip()
                filedata_field[1].strip(), filedata_field[2].strip(), filedata_field[3].strip(), filedata_field[4:]
                line = file_name.readline()                
        file_name.close()

        return None    

    def display_results(self):

        _tab = 6
        _data_length = 4
        _nonexistent_count = 0
        _ongoing_count = 0
        _algorithm_count = 0
        _algorithms = '| Algorithms'
        length_to_pad = self.__longest_algorithm_name
        difference_in_padding = 0

        # This if/else statement was used to set the minimum padding to either the length of the variable _algorithms for the title of the table, or if not the length of the logest algorithm name to make the table dynamic.
        if len(_algorithms) < length_to_pad:
            difference_in_padding = length_to_pad - len(_algorithms)            
        elif len(_algorithms) > length_to_pad:
            length_to_pad = len(_algorithms)

        _length_of_border = length_to_pad + _data_length + (self.__datasets_count * (_tab + _data_length))        

        print('\nRESULTS')
        print(f'{"-" * _length_of_border}')
        print(f'{_algorithms}', (self._space * (difference_in_padding + 1)) , end = '')

        # As it was noted that the number of datasets was consistent among records I took that to just select the first algorithm object's dataset IDs and iterate through that list. A for loop was used as it works well with a list of objects.
        algorithm_object = self.__algorithm_list[0]
        for dataset_object in algorithm_object.get_dataset_list:
            dataset_object = dataset_object[0]
            dataset_value = dataset_object.get_dataset_ID
            print(f'{self._space:<{_tab}}{dataset_value}', end = '')

        print(' |')                
        print(f'{"-" * _length_of_border}')

        # For loops were used here, again, as they work well iterating through lists of objects. The else statement was added in case in testing an integer was used and that destroyed my beautiful formatted table.
        for algorithm_object in self.__algorithm_list:
            print(f'| {algorithm_object.get_algorithm_name}', end = '')
            temp_algorithm_len = length_to_pad - len(algorithm_object.get_algorithm_name)
            print(self._space * temp_algorithm_len, end = '')
            for dataset_object in algorithm_object.get_dataset_list:
                dataset_object = dataset_object[0]
                dataset_value = dataset_object.get_dataset_value
                if dataset_value == '':
                    dataset_value = '  XX'
                    _nonexistent_count += 1
                elif dataset_value == '404':
                    dataset_value = '  --'
                    _ongoing_count += 1
                else:
                    dataset_value = round(float(dataset_value), 1)
                print(f'{self._space:<{_tab}}{dataset_value}', end = '')
            print(f' |')
            _algorithm_count += 1
        print(f'{"-" * _length_of_border}\n')            
        print('RESULTS SUMMARY')
        print(f'There are {_algorithm_count} algorithms and {self.__datasets_count} datasets.')
        print(f'The number of nonexistent results is {_nonexistent_count} and on-going results is {_ongoing_count}.')


    def display_datasets(self):

        _tab = 6
        _data_length = 4
        _length_of_border = 107
        _most_difficult_dataset_average = 100
        _most_num_of_fails = 0
        _most_num_of_fails_dataset_name = ''
        _most_difficult_dataset_name = ''

        print('\nDATASET INFORMATION')
        print(f'{"-" * _length_of_border}')
        print(f'| DatasetID{self._space:<{_tab / 2}}Name{self._space:<{_tab * 2}}Type{self._space:<{_data_length}}Weight{self._space:<{_tab}}Ndata{self._space:<{_tab}}Source{self._space:<{_data_length}}Average{self._space:<{_tab * 2}}Range{self._space:<{_data_length}} Nfail |')            
        print(f'{"-" * _length_of_border}')

        algorithm_object = self.__algorithm_list[0]
        # For loops were used here, again, as they work well iterating through lists of objects. The else statement was added in case in testing an integer was used and that destroyed my beautiful formatted table.
        for dataset_info_object in self.__dataset_info_list:
            dataset_info_ID = dataset_info_object.get_dataset_info_ID
            dataset_name = dataset_info_object.get_dataset_info_name
            dataset_type = dataset_info_ID[-1]
            print(f'| {dataset_info_ID:<{(_tab * 2)}}{dataset_name:<{(_tab * 3) + 1}}{dataset_type}{self._space:<{(_tab + _data_length - 1)}}{dataset_info_object.get_complexity_weight}{dataset_info_object.get_num_of_data_pts:>{_tab * 2 - 1}}{dataset_info_object.get_published_source:>{_tab * 2}}', end = '')

            _num_of_fails = 0
            for dataset_object in algorithm_object.get_dataset_list:
                if dataset_object[0].get_dataset_ID == dataset_info_ID:
                    dataset_object = dataset_object[0]
                    algorithm_list_dataset_value = dataset_object.get_dataset_ID
                    _dataset_average = self.get_average(algorithm_list_dataset_value)
                    _num_of_fails = self.get_num_of_fails(algorithm_list_dataset_value)
                    dataset_range = self.get_dataset_range(algorithm_list_dataset_value)
                    print(f' {_dataset_average:>{_tab + _data_length}.1f}{float(dataset_range[0]):>{_tab + _data_length}.1f} - {float(dataset_range[1]):>{_data_length}.1f}{int(_num_of_fails):>{_tab + _data_length}}', end = '')
                    if _dataset_average < _most_difficult_dataset_average:
                        _most_difficult_dataset_average = _dataset_average
                        _most_difficult_dataset_name = dataset_name
                    if _num_of_fails > _most_num_of_fails:
                        _most_num_of_fails = _num_of_fails
                        _most_num_of_fails_dataset_name = dataset_name

            print(f' |')
        print(f'{"-" * _length_of_border}\n')            
        print('DATASET SUMMARY')
        print(f'The most difficult dataset is {_most_difficult_dataset_name} with an average result of {_most_difficult_dataset_average:.1f}.')
        print(f'The dataset with the most failures is {_most_num_of_fails_dataset_name} with the number of failures being {_most_num_of_fails}.')


    def display_algorithms(self):
        pass


    def print_dataset_to_reports(self):

        original_stdout = sys.stdout
        with open('reports.txt', 'w') as f:
            sys.stdout = f
            
            self.display_results()

            if len(sys.argv) == 3:
                self.display_datasets()            

                if len(sys.argv) == 4:
                    self.display_algorithms()
            sys.stdout = original_stdout             
        return None


    # This method gets all dataset values for a given dataset_ID that contain an actual value, and returns the average value by using a counter to to divide the result by.
    def get_average(self, search_value):
        _average_value = 0
        _value_counter = 0

        # For loops were used here, again, as they work well iterating through lists of objects. The else statement was added in case in testing an integer was used and that destroyed my beautiful formatted table.
        for algorithm_object in self.__algorithm_list:
            if search_value[0] == 'D' and search_value[1:-2].isnumeric() and (search_value[-1] == 'S' or search_value[-1] == 'A'):
                for dataset_object in algorithm_object.get_dataset_list:
                    if search_value == dataset_object[0].get_dataset_ID:
                        # This code is duplcated below and I don't like it. If I have time I'll look at refactoring it because I feel I shouldn't just be reusing a chunk like this. I think I could make an internal  method/function here to pass in the dataset_object[0].get_dataset_ID and return the _average_value / _value_counter but I tried it and it didn't work and I'm spinning the wheels so I'll move on.
                        temp_value = dataset_object[0].get_dataset_value
                        if temp_value != '404' and temp_value != '':
                            _average_value += float(temp_value)
                            _value_counter += 1
            else:
                if search_value == algorithm_object.get_algorithm_name:
                    for dataset_object in algorithm_object.get_dataset_list:
                        temp_value = algorithm_object[0].get_dataset_value
                        if temp_value != '404' and temp_value != '':
                            _average_value += float(temp_value)
                            _value_counter += 1


        if _value_counter != 0:
            return _average_value / _value_counter
        else:
            return 0


    # This method gets and returns the minimum and maximum values
    def get_dataset_range(self, dataset_ID):

        _min_max_dataset_values = [100, 0]

        for algorithm_object in self.__algorithm_list:
            for dataset_object in algorithm_object.get_dataset_list:
                if dataset_ID == dataset_object[0].get_dataset_ID:
                    temp_dataset_value = dataset_object[0].get_dataset_value
                    if temp_dataset_value != '404' and temp_dataset_value != '':
                        temp_dataset_value = float(temp_dataset_value)
                        if _min_max_dataset_values[0] > temp_dataset_value:
                            _min_max_dataset_values[0] = temp_dataset_value
                        if _min_max_dataset_values[1] < temp_dataset_value:
                            _min_max_dataset_values[1] = temp_dataset_value

        return _min_max_dataset_values


    # This method searches through any datasets and counts up the number of fails, those dataset objects that are not associated with a numberic value.
    def get_num_of_fails(self, dataset_ID):
        _number_of_dataset_fails = 0

        for algorithm_object in self.__algorithm_list:
            for dataset_object in algorithm_object.get_dataset_list:
                if dataset_ID == dataset_object[0].get_dataset_ID:
                    temp_dataset_value = dataset_object[0].get_dataset_value
                    if temp_dataset_value == '':
                        _number_of_dataset_fails += 1

        return _number_of_dataset_fails


class Dataset:

    def __init__(self, dataset_ID, dataset_value):
        self.__dataset_ID = dataset_ID
        self.__dataset_value = dataset_value        
  
    @property
    def get_dataset_ID(self):
        return self.__dataset_ID

    @property
    def get_dataset_value(self):
        return self.__dataset_value
    

# This class was added to handle the new data loaded in by the dataset file
class DatasetInfo:
    def __init__(self, dataset_info_ID, dataset_info_name, complexity_weight, num_of_data_pts, published_source):
        self.__dataset_info_ID = dataset_info_ID
        self.__dataset_info_name = dataset_info_name
        self.__complexity_weight = complexity_weight
        self.__num_of_data_pts = num_of_data_pts
        self.__published_source = published_source
  
    @property
    def get_dataset_info_ID(self):
        return self.__dataset_info_ID

    @property
    def get_dataset_info_name(self):
        return self.__dataset_info_name

    @property
    def get_complexity_weight(self):
        return self.__complexity_weight

    @property
    def get_num_of_data_pts(self):
        return self.__num_of_data_pts

    @property
    def get_published_source(self):
        return self.__published_source


# This class was added to handle the new data loaded in by the algorithm file. I shouldn't be keeping both these AlgorithmInfo and DatasetInfo classes and instead add default variables then set the values once the files are read in but time...
class AlgorithmInfo:
    def __init__(self, algorithm_info_name, algorithm_type, year_invented, algorithm_authors, published_source):
        self.__algorithm_info_name = algorithm_info_name
        self.__algorithm_type = algorithm_type
        self.__year_invented = year_invented
        self.__algorithm_authors = algorithm_authors
        self.__published_source = published_source
  
    @property
    def get_algorithm_info_name(self):
        return self.__algorithm_info_name

    @property
    def get_algorithm_type(self):
        return self.__algorithm_type

    @property
    def get_year_invented(self):
        return self.__year_invented

    @property
    def get_algorithm_authors(self):
        return self.__algorithm_authors

    @property
    def get_published_source(self):
        return self.__published_source


class Algorithm:

    def __init__(self, algorithm_name, type = '', year_invented = 0, algorithm_authors = []):
        self.__algorithm_name = algorithm_name
        self.__dataset_list = []
        self.__type = type
        self.__year_invented = year_invented
        self.__algorithm_authors = algorithm_authors

    @property
    def get_algorithm_name(self):
        return self.__algorithm_name
            
    @property
    def get_dataset_list(self):
        return self.__dataset_list
    
    @property
    def get_type(self):
        return self.__type
            
    @property
    def get_year_invented(self):
        return self.__year_invented

    @property
    def get_algorithm_authors(self):
        return self.__algorithm_authors

    def set_algorithm_type(self, type_update_value):
        self.__type = type_update_value
        return self.__type

    def set_year_invented(self, year_update_value):
        self.__year_invented = year_update_value
        return self.__year_invented

    def set_year_invented(self, algorithm_authors_list):
        self.__algorithm_authors = algorithm_authors_list
        return self.__algorithm_authors


    # I initially had this display function for testing purposes and have left it as I've found it useful, as well as for sentimental value
    def display_info(self):
        print(f'Algorithm_name: {self.get_algorithm_name}\nList:')
        for dataset_list_item in self.__dataset_list:
            dataset_object = dataset_list_item[0]
            dataset_ID = dataset_object.get_dataset_ID
            dataset_value = dataset_object.get_dataset_value
            print(f'{dataset_ID}:{dataset_value},')


if __name__ == "__main__":
  #  try:
        new_Records_instance = Records()
        new_Records_instance.read_results(sys.argv[1])
        new_Records_instance.display_results()
        # Might need to add in if len(sys.argv) < 5 here and throw an error..
        if len(sys.argv) > 2:
            new_Records_instance.read_datasets(sys.argv[2])
            new_Records_instance.display_datasets()
            if len(sys.argv) == 4:
                new_Records_instance.read_algorithms(sys.argv[3])
                new_Records_instance.display_algorithms(sys.argv[3])
        new_Records_instance.print_dataset_to_reports()                
#    except:
 #       print('[Usage:] python my_record.py <results file>')
