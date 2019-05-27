import model
import bottle 

SKRIVNOST = "mojaskrivnost"

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie(
        "idigre", "idigre{0}".format(id_igre), secret= SKRIVNOST, path='/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(
        "idigre", secret=SKRIVNOST).split('e')[1])
    igra, poskus = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, poskus=poskus)

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie(
        'idigre', secret=SKRIVNOST).split('e')[1])
    crka = bottle.request.forms.getunicode("crka")
    vislice.ugibaj(id_igre, crka)
    bottle.redirect("/igra/")

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root="img")


bottle.run(reloader=True, debug=True)

























bottle.run(reloader=True, debug=True)
