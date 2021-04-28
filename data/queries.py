from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_most_rated():
    # return data_manager.execute_select('select * from shows order by rating desc limit 15;')
    return data_manager.execute_select("select s.title, s.year, s.runtime, s.rating, STRING_AGG( gr.name, ' - ' ORDER BY gr.name) as genres, s.trailer, s.homepage  from shows as s inner join show_genres as sg on s.id = sg.show_id inner join genres as gr on sg.genre_id = gr.id group by s.id order by s.rating desc limit 15")


