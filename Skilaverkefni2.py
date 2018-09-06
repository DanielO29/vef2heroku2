from sys import argv
import bottle
from bottle import *

bottle.debug(True)

@route("/")
def index():
    return """
    <h2> Verkefni 2. </h2>
    <p><a href="/a"> Liður A </a></p>
    <p><a href="/b"> Liður B </a></p>
    """

@route("/a")
def a():
    return """
        <h2> Verkefni 2.A </h2>
        <a href="/sidaA/1"> Síða 1. </a> -
        <a href="/sidaA/2"> Síða 2. </a> -
        <a href="/sidaA/3"> Síða 3. </a> -
        <a href="/"> Forsíða </a>
    """

@route("/sidaA/<id>")
def page(id):
    if id == "1":
        return """
        Þetta er síða 1.A<br><a href="/a"> Til baka </a>
        """
    elif id == "2":
        return """
        Þetta er síða 2.A<br><a href="/a"> Til baka </a>
        """
    elif id == "3":
        return """
        Þetta er síða 3.A<br><a href="/a"> Til baka </a>
        """
    else:
        abort(404, "<h2 style='color:red'>Þessi síða finnst ekki </h2>")

#-----------------------------------------------------------------------------------------------------------------------
@route("/b")
def b():
    return """
        <h2> Verkefni 2.B </h2>
        <a href="/"> Forsíða </a>
        <h4> Veldu mynd sem þér líkar við. </h4>
        <a href="/sida2?mynd=a"><img src='myndir/A.png'></a>
        <a href="/sida2?mynd=b"><img src='myndir/B.png'></a>
        <a href="/sida2?mynd=c"><img src='myndir/C.png'></a>
        <a href="/sida2?mynd=d"><img src='myndir/D.png'></a>
    """

@route("/sida2")
def page():
    l = request.query.mynd
    if l == 'a':
        return "<h3>Þú valdir þessa mynd:</h3> <img src='myndir/A.png'>"
    l = request.query.mynd
    if l == 'b':
        return "<h3>Þú valdir þessa mynd:</h3> <img src='myndir/B.png'>"
    l = request.query.mynd
    if l == 'c':
        return "<h3>Þú valdir þessa mynd:</h3> <img src='myndir/C.png'>"
    l = request.query.mynd
    if l == 'd':
        return "<h3>Þú valdir þessa mynd:</h3> <img src='myndir/D.png'>"


#-----------------------------------------------------------------------------------------------------------------------

@route('/myndir/<skra>')
def static_skra(skra):
    return static_file(skra, root='myndir')


@error(404)
def villa(error):
    return """
        <h2 style='color:red'>Þessi síða finnst ekki </h2>
    """

#run(host="localhost", port=8060)
bottle.run(host="0.0.0.0", port=argv[1])
