from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, League, Team

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def mainPage():
    return render_template('main.html')


@app.route('/league/<int:league_id>')
def leaguePage(league_id):
    return render_template('league_page.html')

@app.route('/team/<int:team_id>')
def team_page(team_id):
    return render_template('team_page.html')


@app.route('/new_team')
def newTeam():
    return render_template('new_team.html')


@app.route('/edit_team/<int:team_id>')
def editTeam(team_id):
    return render_template('edit_team.html')

@app.route('/delete_team/<int:team_id>')
def delete_team(team_id):
    return render_template('delete_team.html')



# # templeague = League(name = "spanish")
# # tempteam = Team(name= "real madrid", info="best ever !!!!", league=templeague)
# # session.add(templeague)
# # session.add(tempteam)
# # session.commit()
# print(session.query(League).first().name)
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
