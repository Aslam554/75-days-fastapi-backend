from fastapi import FastAPI
from data import post
from fastapi.responses import HTMLResponse


app = FastAPI()



@app.get("/",response_class=HTMLResponse,include_in_schema=False)
@app.get("/posts",response_class=HTMLResponse,include_in_schema=False)
def home():
    # return {"message":"Welcome to FastAPI backend dev bro..."}
    dt = ""
    for i in post:
       dt +=f"""
       <div>
       <h1>Title : {i['title']}</h1>
       <p> Content :{i['content']}</p>
       <hr>
       </div>\n
       """
    return dt

@app.get("/api/posts")
def get_posts():
    return post