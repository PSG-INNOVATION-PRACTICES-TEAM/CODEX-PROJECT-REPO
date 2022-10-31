#Replace Functions
#replaces the number in words with corresponding numbers
from ast import parse


def number_replacer(string):
    temp = string.replace(' zero ','0').replace(' one ','1').replace(' two ','2').replace(' three ','3').replace(' four ','4').replace(' five ','5').replace(' six ','6').replace(' seven ','7').replace(' eight ','8').replace(' nine ','9')
    temp = temp.replace('zero ','0').replace('one ','1').replace('two ','2').replace('three ','3').replace('four ','4').replace('five ','5').replace('six ','6').replace('seven ','7').replace('eight ','8').replace('nine ','9')
    temp = temp.replace(' zero','0').replace(' one','1').replace(' two','2').replace(' three','3').replace(' four','4').replace(' five','5').replace(' six','6').replace(' seven','7').replace(' eight','8').replace(' nine','9')
    temp = temp.replace('zero','0').replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')
    return temp

#replaces the operators with corresponding operators
def operator_replacer(string):
    temp = string.replace('equals equals','==').replace('less than equals','<=').replace('greater than equals','>=').replace('not equals','!=').replace('plus equals','+=').replace('minus equals','-=').replace('star equals','*=').replace('slash equals','/=').replace('and equals','&=').replace('xor equals','|=').replace('or equals','^=').replace('less than','<').replace('greater than','>').replace('equals','=').replace('plus','+').replace('minus','-').replace('slash slash','//').replace('slash','/').replace('star star','**').replace('star','*').replace('and','&').replace('xor','^').replace('or','|').replace('percent','%').replace('true','True').replace('false','False')
    return temp

def for_loop_replacer(string):
    if 'range of' in string:
        temp = string.replace('range of','range(')
        temp = temp+"):"
    return temp

def parse_statement(statement,key):
    temp = operator_replacer(number_replacer(statement))
    if key=='if':
        temp=temp+":"
    elif key=="else if":
        temp =temp.replace('else if','elsif')
        temp = temp+":"
    elif key=='loop declaration':
        temp = for_loop_replacer(number_replacer(statement))
    return temp

# print(parse_statement('for i in range of one eight three','for_loop_declaration'))