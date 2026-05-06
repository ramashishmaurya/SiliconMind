from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define data model
class PrintValues(BaseModel):
    name: str
    age: Optional[str] =None # this is use from the api is well 

# POST API
@app.post("/api")
def postvalues(data: PrintValues):
    return {
        "classvalues": data.model_dump()
    }

# should not need to assign  here 


