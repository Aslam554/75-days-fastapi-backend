from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from students import student
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')

#home route /
# @app.get("/",response_class=HTMLResponse)
# def home():
#     return f"<h1>Welcome to Home Page</h1>"

#jinja2 templating for rendering html pages directly
@app.get("/", include_in_schema=False)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


#get all students details
@app.get("/api/students",response_class=HTMLResponse,include_scheme=False)
def get_students():
    data = ""
    for i in student:
       data+= f'''
        <div style='background-color:blue; color:white;padding:5px;width:40%'>
          <ul>
            <li>Id : {i['id']}</li>
            <li>Name : {i['name']}</li>
            <li>Age : {i['age']}</li>
            <li>Gender : {i['gender']}</li>
            <li>About : {i['about']}</li>
          </ul>
       </div>
       <hr/>
      '''
    return data

#get a single student data now
@app.get("/api/students/{id}",response_class=HTMLResponse)
def single_student(id:int):

    for i in student:
        if i['id']==id:
         return f'''
          <div style='background-color:blue; color:white;padding:5px;width:40%'>
            <ul>
                <li>Id : {i['id']}</li>
                <li>Name : {i['name']}</li>
                <li>Age : {i['age']}</li>
                <li>Gender : {i['gender']}</li>
                <li>About : {i['about']}</li>
            </ul>
          </div>
         '''
    return f'<h1>Student with {id} is not found here</h1>'