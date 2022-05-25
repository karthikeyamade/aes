from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/courses/{course_name}")
def read_course(course_name):
  s=course_name+'bye'
  return {"course_name": s}
