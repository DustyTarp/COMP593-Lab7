

def main():

    #initialize complex data structure
    person_info = {
        'name': 'Riley',
        'student_id': '10256790',
        'pizza_toppings': [
            'chicken', 
            'bacon', 
            'peppers'
        ],
        'movies': [
            {'Title': 'The Gentleman',
            'genre': 'action',
            },
            {'Title': 'Grandma\'s Boy',
            'genre': 'comedy'
            }
        ]
    }

    #add a movie 
    new_movie = {'Title': 'Vice', 'genre': 'drama' }
    person_info['movies'].append(new_movie)

    new_toppings = ('mushrooms', 'olives', 'chilis')
    add_pizza_topping(person_info, new_toppings)


    print(person_info['pizza_toppings'])

    print_info(person_info)

    pass


def add_pizza_topping(person_info, new_toppings):

    for t in new_toppings:
        person_info['pizza_toppings'].append(t)



def print_info(person_info):
    sentence_1 = 'Hi Joe, my name is ' + person_info['name'] + ', and my student ID is ' + person_info['student_id'] + '.'
    sentence_2 = 'My ideal pizza has '

    for i,g in enumerate(person_info['pizza_toppings']):
        sentence_2 += g
        if i < len(person_info['pizza_toppings']) - 2:
            sentence_2 += ', '
        elif i < len(person_info['pizza_toppings']) and i < len(person_info['pizza_toppings']) - 1:
            sentence_2 += ' and '    
        else:
            sentence_2 += '.'

    sentence_3 = 'I like to watch ' 

    for i,g in enumerate(person_info['movies']):
        sentence_3 += g['genre']
        if i < len(person_info['movies']) - 2:
            sentence_3 += ', '
        elif i < len(person_info['movies']) and i < len(person_info['movies']) - 1:
            sentence_3 += ' and '
        else:
            sentence_3 += ' movies.'

    sentence_4 = 'Some of my favourite are '

    for i,g in enumerate(person_info['movies']):
        sentence_4 += g['Title']
        if i < len(person_info['movies']) - 2:
            sentence_4 += ', '
        elif i < len(person_info['movies']) and i < len(person_info['movies']) - 1:
            sentence_4 += ' and '
        else:
            sentence_4 += '!'

    print(sentence_1, sentence_2,  sentence_3, sentence_4, sep='\n')



main()

