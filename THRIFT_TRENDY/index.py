from flask import Flask,session,url_for,redirect,render_template,request
from flask_mysqldb import MySQL
import random


app = Flask(__name__)
mydb = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD'] = 'GALGALLO10'
app.config['MYSQL_DB'] = 'THRIFTTRENDY'

app.secret_key = 'kcd'

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():

    return render_template('home.html')

@app.route('/topwears',methods =['GET','POST'])
def topwears():
    if request.method =='POST':
        global idfornow
        idfornow=str(request.form['id'])
        print(idfornow)
        cursor = mydb.connection.cursor()
        cursor.execute('SELECT * FROM PRODUCTINFO WHERE ID='+idfornow  )
        ALL = cursor.fetchall()
        
        for ali in ALL:
            pass

        return render_template('base.html',all=ali)
    else:
        return render_template('topwears.html')


@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method =='POST':
        type1=str(request.form['type']   )
        color=str(request.form['color']  ) 
        size=str(request.form['size']    )
        cost=str(request.form['cost']    )
        url=str(request.form['url'])     

        cursor = mydb.connection.cursor()
        cursor.execute('SELECT ID FROM PRODUCTINFO ORDER BY ID DESC')
        x=cursor.fetchall()
        bignum=x[0][0]
        id=int(bignum)+1
        id=str(id)
        print('added ',(int(id)-1),' to 1 and now it is ',id)
        cursor.execute('INSERT INTO PRODUCTINFO (ID,COST,TYPE,COLOR,SIZE,URL) VALUES(%s,%s,%s,%s,%s,%s) ',(id,cost,type1,color,size,url))
        mydb.connection.commit()
        return render_template('admin.html')
    else:
        return render_template('admin.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


if __name__ =='__main__':
    app.run(debug=True)