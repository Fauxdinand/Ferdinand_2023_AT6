class Validator:
    '''Accepts a list of strings. 
       Checks if the elements are a valid, posititive integer,
       and returns a new list only containing the valid integers.
    '''
    def __init__(self):
        self.v_l = []

    def validate_data(self, s_l):
        for _ in s_l:
            try:
                n = int(_)
                if n>0:
                    self.v_l.append(n)
            except ValueError: 
                pass
            assert all(isinstance(_,int) and _>0 for _ in self.v_l)
        return self.v_l
 
            


