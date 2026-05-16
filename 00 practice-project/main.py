from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from students import student

app = FastAPI()

templates = Jinja2Templates(directory="templates")


# Home Route
@app.get("/", include_in_schema=False)
def home(request: Request):

    return templates.TemplateResponse(request,"index.html")


# Get All Students
@app.get(
    "/api/students",
    response_class=HTMLResponse,
    include_in_schema=False
)
def get_students():

    data = ""

    for i in student:

        data += f"""
        <div style='background-color:blue; color:white; padding:5px; width:40%'>
          <ul>
            <li>Id : {i['id']}</li>
            <li>Name : {i['name']}</li>
            <li>Age : {i['age']}</li>
            <li>Gender : {i['gender']}</li>
            <li>About : {i['about']}</li>
          </ul>
        </div>

        <hr/>
        """

    return data


# Get Single Student By ID
@app.get("/api/students/{id}", response_class=HTMLResponse)
def single_student(id: int):

    for i in student:

        if i["id"] == id:

            return f"""
            <div style='background-color:blue; color:white; padding:5px; width:40%'>

                <ul>
                    <li>Id : {i['id']}</li>
                    <li>Name : {i['name']}</li>
                    <li>Age : {i['age']}</li>
                    <li>Gender : {i['gender']}</li>
                    <li>About : {i['about']}</li>
                </ul>

            </div>
            """

    return f"<h1>Student with ID {id} not found</h1>"