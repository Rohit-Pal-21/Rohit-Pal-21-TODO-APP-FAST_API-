from fastapi import FastAPI,Depends
from database import engine
from routers import auth,todos
from company import companyapis,dependencies
import models
import uvicorn
app= FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(
    companyapis.router,
    prefix="/company",
    tags=["company"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={
        404:{"description":"Internal use only"}
    })

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)