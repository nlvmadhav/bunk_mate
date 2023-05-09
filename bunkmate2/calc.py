from flask import Flask,render_template,request

app = Flask(__name__,template_folder='templates',static_folder='staticFiles')

@app.route("/")
def display_page():
    return render_template("bunkmate.html")

@app.route("/percentage",methods = ["POST"])
def login():
    percent = request.form["Percent"]
    percent_req = request.form["Percent_req"]
    no_of_classes = request.form["classes"]
    try:
        percents = int(percent)
        if(percents>100):
            return render_template("bunkmate.html",message = "PERCENTAGE TAPPU ICCHAVU MAMA...\nMALLI IVVU...")
        else:
            if(percent_req>percent):
                a = (percent_req*no_of_classes)/100
                c = a-percent
                return render_template("bunkmate.html",message = "Inka Nuvvu "+c+" Classes attend avvali Mama "+percent_req+"%"+" ravadaniki")
    except:
        return render_template("bunkmate.html",message = "PERCENTAGE TAPPU ICCHAVU MAMA...\nMALLI IVVU...")
    return render_template("bunkmate.html",message = "hi")