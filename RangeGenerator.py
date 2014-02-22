class RangeGenerator:
    def generate(self, interval):
        begin_notation = interval[0]
        end_notation = interval[-1]

        number_list = interval[1:-1].split(",")
        begin_number = int(number_list[0])
        end_number = int(number_list[1])

        notation_type = begin_notation+end_notation

        result_set =(   
                        (notation_type == "()" and self.generate_begin_end(begin_number+1, end_number - 1)) or 
                        (notation_type == "(]" and self.generate_begin_end(begin_number+1, end_number)) or 
                        (notation_type == "[)" and self.generate_begin_end(begin_number, end_number - 1)) or 
                        (notation_type == "[]" and self.generate_begin_end(begin_number, end_number))
                    )
        
        return result_set
        
    def generate_begin_end(self, begin_number, end_number):
        return "{" + str(range(begin_number, end_number+1)).replace(' ',"")[1:-1] + "}"

    # def generator_factory(self, begin_notation, end_notation):
    #     GENERATOR_DICTIONARY = {
    #         "()" : lambda begin_number, end_number : self.generate_begin_end(begin_number+1, end_number - 1),
    #         "(]" : lambda begin_number, end_number : self.generate_begin_end(begin_number+1, end_number),
    #         "[)" : lambda begin_number, end_number : self.generate_begin_end(begin_number, end_number - 1),
    #         "[]" : lambda begin_number, end_number : self.generate_begin_end(begin_number, end_number),
    #     }

    #     return GENERATOR_DICTIONARY[begin_notation+end_notation]