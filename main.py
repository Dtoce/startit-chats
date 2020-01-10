from flask import Flask, render_template,jsonify, json, request



app = Flask('app')


@app.route('/')
def index_page():
  return render_template("index.html")

@app.route('/chats')
def chats_page():
  return render_template("chats.html")
#chata lapa 



@app.route('/healt')
def healt_check():
  return "ok"
# sistēmas dzīvības pārbaude


@app.route('/chats/lasi')
def ielasit_chatu():
  chata_rindas=[]
  with open("chats.txt", "r", encoding="utf-8") as f:
    for rinda in f:
      chata_rindas.append(rinda)

  return jsonify({"chats":chata_rindas}) 
# ielasīt čatu

@app.route('/chats/suuti', methods=['POST'])
def suti_zinju():
  dati=request.json
  with open("chats.txt", "a", newline="") as f:
    f.write(dati["chats"]+"\n")
  return ielasit_chatu()
# otrādā



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)