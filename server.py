from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "9834uih98pouihng3sdfy435"


def sum(num):
    return session["sum"] + num
    

#===========================================
# Main Index
#===========================================

#* ===========================================
#? Root Route  <==> RENDER FORM - /
#* ===========================================
@app.route('/')
def index():
    print("hello")
    
    # Alert no user number chosen
    if "send_alert" in session:
       if session["send_alert"]:
           send_alert = True
       else:
           send_alert = False
    else:
        send_alert = False
        
    # Using the times two button
    if "times_two" in session:
        if "counter" in session:
            session["counter"] += 2
        else:
            session["counter"] = 2
        session.pop("times_two", None)
    
    elif "times_one" in session:
            if "counter" in session:
                session["counter"] += 1
            else:
                session["counter"] = 1
            session.pop("times_one", None)
        
        
    elif "user_chosen" in session:
        if "counter" in session:
            if "user-choice-num" in session:
                session["counter"] += int(session["user-choice-num"])
        else:
            if "user-choice-num" in session:
                session["counter"] = int(session["user-choice-num"])
 
    else:
        if "counter" in session:
            session["counter"] += 1
        else:
            session["counter"] = 0
            

    counter = session["counter"]
    print(session["counter"])
    return render_template("index.html", counter=counter, send_alert=send_alert)



#t- ===========================================
#? PROCESS FORM - /counter
#t- ===========================================
@app.route('/counter_btn', methods=['POST']) 
def counter():
    session["times_one"] = True
    return redirect("/")

#t- ===========================================
#? PROCESS FORM - /times-two
#t- ===========================================
@app.route('/times-two', methods=['POST']) 
def times_two():
    session["times_two"] = True
    return redirect("/")

#t- ===========================================
#? PROCESS FORM - /user-choice
#t- ===========================================
@app.route('/user-choice', methods=['POST']) 
def user_choice():
    print(request.form)
    if request.form["user-choice_num"] != "":
        session["user-choice-num"] = int(request.form["user-choice_num"])
        session["send_alert"] = False
    elif "user_chosen" in session:
            if session["user_chosen"]:
                return redirect("/")
            else:
                session["send_alert"] = True
                return redirect("/")
    else:
        session["send_alert"] = True
        session["user_chosen"] = False
        return redirect("/")
    session["user_chosen"] = True
    return redirect("/")

#t- ===========================================
#? PROCESS FORM - /destroy
#t- ===========================================
@app.route("/destroy", methods=['POST'])
def destroy():
    session.clear()
    print(session)
    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    print(session)
    return redirect("/")











#! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)
