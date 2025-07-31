from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.responses import Response
from pydantic import BaseModel
from typing import List
from datetime import datetime


app = FastAPI();

class ListModal (BaseModel) :
    author : str
    title : str
    content : str
    creation_datetime : datetime

    
def serialized_stored_events():
    events_converted = []
    for event in events_store:
        events_converted.append(event.model_dump())
    return events_converted


@app.get("/ping")
def read_pong():
    return Response(f"pong", status_code=200)

@app.get("/home")
def read_welcome():
    with open("welcome.html", "r", encoding="utf-8") as file :
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")


@app.get("/{full_path:path}")
def not_found(full_path: str):
    with open("notfound.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=404, media_type="text/html")


@app.get("/posts")
def events_lists():
    return Response(serialized_stored_events(), status_code=200)


@app.post("/posts")
def new_events (event_payload : List[ListModal]):
    event_store.extend(event_payload)
    return Response(serialized_stored_events(), status_code=201)

@app.put("/posts")
def update_or_create_events(event_payload: List[ListModal]):
    global events_store
    for new_event in event_payload:
        found = False
        for i, existing_event in enumerate(events_store):
            if new_event.title == existing_event.title:
                events_store[i] = new_event
                found = True
                break
        if not found:
            events_store.append(new_event)
    return Response(serialized_stored_events())

