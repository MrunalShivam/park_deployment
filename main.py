from flask import Flask, render_template, request,session,logging,flash,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
# with open('config.json', 'r') as c:
#     params = json.load(c)["params"]
import joblib
local_server = True
app = Flask(__name__,template_folder='templates')


@app.route("/pred", methods = ['GET','POST'])
def pred():
    if(request.method=='POST'):
        # import pdb;pdb.set_trace();
        Fo=float(request.form['Fo'])
        Fhi=float(request.form['Fhi']) 
        Flo=float(request.form['Flo']) 
        per=float(request.form['per']) 
        Abs=float(request.form['Abs'])
        rap=float(request.form['rap'])  
        ppq=float(request.form['ppq']) 
        ddp=float(request.form['ddp']) 
        shim=float(request.form['shim'])
        db=float(request.form['db'])
        apq3=float(request.form['apq3']) 
        apq5=float(request.form['apq5'])  
        apq=float(request.form['apq']) 
        dda=float(request.form['dda']) 
        nhr=float(request.form['nhr']) 
        hnr=float(request.form['hnr']) 
        rpde=float(request.form['rpde'])
        dfa=float(request.form['db'])
        s1=float(request.form['s1']) 
        s2=float(request.form['s2'])
        d2=float(request.form['d2'])    
        ppe=float(request.form['ppe']) 
        

        model=joblib.load('extra.pkl')
        result=model.predict([[Fo,Fhi,Flo,per,Abs,rap,ppq,ddp,shim,db,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,s1,s2,d2,ppe]])[0]
        result=int(result)
        if result==1:
        	output="patient is PD infected"
        else:
        	output="patient is safe"
        # pred_args=[T,TM,Tm,SLP, H,VV,V,VM]
        # print(pred_args)

        # pred_args=[float(x) for x in request.form.values()]
        # print(pred_args)


        return render_template('crop.html',output=output)
    return render_template('crop.html')



if __name__ == "__main__":
    
    app.run(debug=True)
