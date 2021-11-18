# I decided to write a code that generates data filtering object from a list of keyword parameters:

class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data
            if all(i(item) for i in self.functions)
        ]

# example of usage:
rang=range(100)


positive_even = Filter(lambda a: isinstance(a,int),lambda a: a > 0,lambda a: a % 2 == 0)
positive_even.apply(rang) #should return only even numbers from 0 to 99

assert positive_even.apply(['s','f','g','1','2',2,4,5])==[2,4]
assert positive_even.apply(rang)==[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        def keyword_filter_func(lst):
            try:
                return lst[key] == value
            except KeyError:
                return False
        filter_funcs.append(keyword_filter_func)
    return Filter(*filter_funcs)


sample_data  =  [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]


assert make_filter(name='polly', type='bird').apply(sample_data) == [{"is_dead": True,"kind": "parrot","type": "bird","name": "polly"}]  #should return only second entry from the list
assert make_filter(name='Bill', occupation='was here').apply(sample_data) == [{"name": "Bill","last_name": "Gilbert","occupation": "was here","type": "person"}]  #should return only first entry from the list

# object_filter = Filter(make_filter(name='polly', type='bird'))
# object_filter.apply(sample_data)
# There are multiple bugs in this code. Find them all and write tests for faulty cases.