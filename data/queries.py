from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_most_rated():
    return data_manager.execute_select('select * from shows order by rating desc limit 15;')


