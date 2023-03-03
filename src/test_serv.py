from fastapi.testclient import TestClient
from fastapi import status
from main import app, get_db   
from sqlalchemy.orm import Session
from sqlalchemy import  create_engine
import models 

def test_create_posts():
    engine = create_engine(  
        "sqlite:///testing.db", connect_args={"check_same_thread": False}
    )
    models.Base.metadata.create_all(engine)   

    with Session(engine) as session:   
        def get_db_override():
            return session   

        app.dependency_overrides[get_db] = get_db_override   

        client = TestClient(app)

        response = client.post(
            "/create/" 
        )

        app.dependency_overrides.clear()
        data = response.json()
        assert response.status_code == 200













    

    