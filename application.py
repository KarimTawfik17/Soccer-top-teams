from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, League, Team

engine = create_engine('sqlite:///teams.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def mainPage():
	leagues = session.query(League).all()
	latest_teams = session.query(Team).order_by(Team.id.desc()).limit(2)
	return render_template('main.html', leagues=leagues, teams = latest_teams)

@app.route('/json')
def jsonTeams():
	teams = session.query(Team).all()
	return(jsonify(AllTeams=[team.serialize for team in teams]))


@app.route('/league/<int:league_id>')
def leaguePage(league_id):
	league = session.query(League).filter_by(id = league_id).first()
	teams = session.query(Team).filter_by(league_id = league_id).all()
	print (league.name)
	return render_template('league_page.html',league = league, teams = teams)

@app.route('/team/<int:team_id>')
def teamPage(team_id):
	team = session.query(Team).filter_by(id = team_id).first()
	return render_template('team_page.html' , team = team )

@app.route('/new_team', methods = ['GET','POST'])
def newTeam():
	if request.method == 'POST':
		new_team = Team(name = request.form['title'], info = request.form['info'], league_id=int(request.form['league']))
		session.add(new_team)
		session.commit()
		return redirect(url_for('mainPage'))
	else :
		leagues = session.query(League).all()
		return render_template('new_team.html', leagues=leagues)


@app.route('/edit_team/<int:team_id>', methods=['GET','POST'])
def editTeam(team_id):
	team = session.query(Team).filter_by(id = team_id).first()
	if request.method == 'POST' :
		team.name = request.form['title']
		team.info = request.form['info']
		team.league_id = int(request.form['league'])
		session.add(team)
		session.commit()
		return redirect(url_for('teamPage', team_id = team_id))
	else :
		leagues = session.query(League).all()
		return render_template('edit_team.html',leagues = leagues, team = team)




@app.route('/delete_team/<int:team_id>', methods=['GET','POST'])
def deleteTeam(team_id):
	team = session.query(Team).filter_by(id = team_id).first()
	if request.method == 'POST':
		team = session.query(Team).filter_by(id = team_id).first()
		session.delete(team)
		session.commit()
		return redirect(url_for('mainPage'))
	else:
		return render_template('delete_team.html', team = team )




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
