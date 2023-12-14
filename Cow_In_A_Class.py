class Validator:
    '''Accepts a list of strings. 
       Checks if the elements are a valid, posititive integer,
       and returns a new list only containing the valid integers.
       As well as getting comments from a cow.
    '''
    def __init__(self):
        self.valid_list = []

    def validate_data(self, string_list):
        for elem in string_list:
            try:
                num = int(elem)
                if num > 0:
                    self.valid_list.append(num)
            except ValueError: 
                print(f"'The \N{Cow} say '{elem}' is not an integer.")
            assert all(isinstance(elem,int) and elem>0 for elem in self.valid_list)
        return self.valid_list
